import copy

from PIL import Image

import Enums
from Classes.Block import Block
from Classes.Text import Text
from Enums import LABEL
from ocr import get_text
from Image_Correction import correct_image

import Debug
import torch
import json
import Constants
import Math_Calcs


def detect_blocks(img: Image, ocr_system: Enums.OCR) -> [Block]:
    blocks: [Block] = __get_blocks(img)

    # Debug.get_detections(blocks, img).show()

    blocks = get_text(img, blocks, ocr_system=ocr_system)
    blocks = __sort_arrows(blocks)
    # Debug.get_detections(blocks, img).show()
    blocks = __find_neighbours(blocks)
    blocks = __sort_blocks(blocks)
    blocks = __remove_arrows(blocks)

    # Debug.get_detections(blocks, img).show()

    return blocks


def __get_blocks(img: Image) -> [Block]:
    image: Image = correct_image(copy.deepcopy(img))

    # Model
    model = torch.hub.load('./yolov5', 'custom', source='local', path=Constants.block_detection_model, force_reload=True)

    # Inference
    results = model(image)

    serialized_json = results.pandas().xyxy[0].to_json(orient="records")

    deserialized_json = json.loads(serialized_json)

    results_list: [Block] = []

    for i, entry in enumerate(deserialized_json):
        if entry['confidence'] > Constants.CONFIDENCE_THRESHOLD:
            temp: Block = Block(i, entry['xmin'], entry['ymin'], entry['xmax'],
                                entry['ymax'], entry['confidence'], entry['name'])
            results_list.append(temp)

    results_list = __remove_duplicates(results_list)

    return results_list


def __remove_duplicates(blocks: [Block]) -> [Block]:
    ids: [int] = []

    for block_a in blocks:
        temp: Block = block_a
        for block_b in blocks:
            if block_a != block_b:
                if __check_if_same_position(block_a, block_b):
                    temp = __block_best_confidence(block_a, block_b)

        if not (temp.id in ids):
            ids.append(temp.id)

    result: [Block] = []

    for item in blocks:
        if item.id in ids:
            result.append(item)

    return result


def __check_if_same_position(block_a: Block, block_b: Block) -> bool:
    is_same_or_not: bool = False

    x_min: float = block_a.x_min - block_b.x_min
    if x_min < 0:
        x_min *= -1

    x_max: float = block_a.x_max - block_b.x_max
    if x_max < 0:
        x_max *= -1

    y_min: float = block_a.y_min - block_b.y_min
    if y_min < 0:
        y_min *= -1

    y_max: float = block_a.y_max - block_b.y_max
    if y_max < 0:
        y_max *= -1

    if (x_min < Constants.DUPLICATE_THRESHOLD) and (x_max < Constants.DUPLICATE_THRESHOLD) and (
            y_min < Constants.DUPLICATE_THRESHOLD) and (y_max < Constants.DUPLICATE_THRESHOLD):
        is_same_or_not = True

    return is_same_or_not


def __block_best_confidence(block_a: Block, block_b: Block) -> Block:
    if block_a.confidence >= block_b.confidence:
        return block_a
    if block_a.confidence < block_b.confidence:
        return block_b


def __sort_arrows(blocks: [Block]) -> [Block]:
    """Get sides of all arrows with pointer aid"""
    arrows: [Block] = []
    pointers: [Block] = []
    result: [Block] = []

    for block in blocks:
        if block.object_type == LABEL.pointer:
            pointers.append(block)
        elif "arrow" in block.object_type.name:
            arrows.append(block)
        else:
            result.append(block)

    for arrow in arrows:
        for pointer in pointers:
            is_inside: bool = __is_block_inside(arrow, pointer)
            if is_inside:
                arrow.object_type = __get_arrow_side(arrow, pointer)
                result.append(arrow)

    # TODO: Remove duplicates
    # TODO: Add a system which improve pointer detection in order to avoid double pointers in the same arrow
    return result


def __is_block_inside(block_outside: Block, block_inside: Block) -> bool:

    inside_center_x: float = (block_inside.x_max + block_inside.x_min) / 2
    inside_center_y: float = (block_inside.y_max + block_inside.y_min) / 2

    x_inside: bool = (inside_center_x > block_outside.x_min) and (inside_center_x < block_outside.x_max)
    y_inside: bool = (inside_center_y > block_outside.y_min) and (inside_center_y < block_outside.y_max)

    return x_inside and y_inside


def __get_arrow_side(arrow: Block, pointer: Block) -> LABEL:
    pointer_inside_x: float = (pointer.x_max + pointer.x_min) / 2
    pointer_inside_y: float = (pointer.y_max + pointer.y_min) / 2
    distances = {
        LABEL.arrow_line_up: ((arrow.y_max + arrow.y_min) / 2) - pointer_inside_y,
        LABEL.arrow_line_down: pointer_inside_y - ((arrow.y_max + arrow.y_min) / 2),
        LABEL.arrow_line_right: pointer_inside_x - ((arrow.x_max + arrow.x_min) / 2),
        LABEL.arrow_line_left: ((arrow.x_max + arrow.x_min) / 2) - pointer_inside_x
    }
    distances_list = sorted(distances.items(), key=lambda x: x[1])
    return distances_list[3][0]


def __find_neighbours(blocks: [Block]) -> [Block]:
    block: Block
    for block in blocks:
        if "arrow" in block.object_type.name:
            neighbours: [[int], [int]] = __find_block_neighbours(block, blocks)
            block.Next_Blocks = neighbours[0]
            block.Previous_Blocks = neighbours[1]
    return blocks


def __find_block_neighbours(block: Block, blocks: [Block]) -> [[int], [int]]:
    previous_neighbour: {int, int} = {}
    next_neighbour: {int, int} = {}
    neighbour: Block
    for neighbour in blocks:
        if neighbour != block:
            a: [int, int]
            b: [int, int]
            p: [int, int]
            if block.object_type == LABEL.arrow_line_down:
                # C, D => bottom limit => Previous block
                a = (neighbour.x_min, neighbour.y_max)
                b = (neighbour.x_max, neighbour.y_max)
                p = ((block.x_max + block.x_min) / 2, block.y_min)
                previous_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

                # A, B => upper limit => Next block
                a = (neighbour.x_min, neighbour.y_min)
                b = (neighbour.x_max, neighbour.y_min)
                p = ((block.x_max + block.x_min) / 2, block.y_max)
                next_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

            if block.object_type == LABEL.arrow_line_up:
                # A, B => upper limit => Previous block
                a = (neighbour.x_min, neighbour.y_min)
                b = (neighbour.x_max, neighbour.y_min)
                p = ((block.x_max + block.x_min) / 2, block.y_max)
                previous_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

                # C, D => bottom limit => Next block
                a = (neighbour.x_min, neighbour.y_max)
                b = (neighbour.x_max, neighbour.y_max)
                p = ((block.x_max + block.x_min) / 2, block.y_min)
                next_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

            if block.object_type == LABEL.arrow_line_left:
                # C, D => bottom limit => Next block
                a = (neighbour.x_max, neighbour.y_min)
                b = (neighbour.x_max, neighbour.y_max)
                p = (block.x_min, (block.y_min + block.y_max) / 2)
                next_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

                # C, D => bottom limit => Previous block
                a = (neighbour.x_min, neighbour.y_min)
                b = (neighbour.x_min, neighbour.y_max)
                p = (block.x_max, (block.y_min + block.y_max) / 2)
                previous_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

            if block.object_type == LABEL.arrow_line_right:
                # C, D => bottom limit => Next block
                a = (neighbour.x_min, neighbour.y_min)
                b = (neighbour.x_min, neighbour.y_max)
                p = (block.x_max, (block.y_min + block.y_max) / 2)
                next_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

                # C, D => bottom limit => Previous block
                a = (neighbour.x_max, neighbour.y_min)
                b = (neighbour.x_max, neighbour.y_max)
                p = (block.x_min, (block.y_min + block.y_max) / 2)
                previous_neighbour[neighbour.id] = Math_Calcs.distance_point_to_segment(a, b, p)

    if block.id == 35:
        print("a")

    next_neighbour = [sorted(next_neighbour.items(), key=lambda x: x[1])[0][0]]
    previous_neighbour = [sorted(previous_neighbour.items(), key=lambda x: x[1])[0][0]]

    return [next_neighbour, previous_neighbour]


def __sort_blocks(blocks: [Block]) -> [Block]:
    block: Block

    # Get next blocks
    for block in blocks:
        if "arrow" in block.object_type.name and len(block.Previous_Blocks) > 0:
            prev_temp: [Block] = [x for x in blocks if x.id == block.Previous_Blocks[0]]
            if "arrow" not in prev_temp[0].object_type.name:
                is_found: bool = False
                loops: int = Constants.DO_WHILE_LOOPS
                index: int = block.Next_Blocks[0]
                next_temp: [Block] = []
                while loops > 0:
                    next_temp = [x for x in blocks if x.id == index]
                    if "arrow" not in next_temp[0].object_type.name:
                        loops = 0
                        is_found = True
                    else:
                        index = next_temp[0].Next_Blocks[0]
                        loops -= 1

                if is_found:
                    temp_blocks: [int] = [x for x in prev_temp[0].Next_Blocks]
                    temp_blocks.append(next_temp[0].id)
                    prev_temp[0].Next_Blocks = temp_blocks
                    if len(block.Texts) > 0:
                        temp_text: [Text] = [x for x in block.Texts]
                        temp_dict = copy.deepcopy(prev_temp[0].Next_Blocks_Conditionals)
                        temp_dict[next_temp[0].id] = temp_text[0].text
                        prev_temp[0].Next_Blocks_Conditionals = copy.deepcopy(temp_dict)

    # Get previous blocks
    for block in blocks:
        if "arrow" not in block.object_type.name:
            for next_block_id in block.Next_Blocks:
                next_blocks: [Block] = [x for x in blocks if x.id == next_block_id]
                if len(next_blocks) > 0:
                    temp = copy.deepcopy(next_blocks[0].Previous_Blocks)
                    temp.append(block.id)
                    next_blocks[0].Previous_Blocks = temp

    return blocks


def __remove_arrows(blocks: [Block]) -> [Block]:
    return [x for x in blocks if "arrow" not in x.object_type.name]
