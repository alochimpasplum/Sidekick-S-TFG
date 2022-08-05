# Functions in this file handles everything related to flowchart object detection
from Classes import Block
from Debug import show_detections
from Enums import LABEL
from PIL import Image, ImageOps
import torch
import json
import Constants


def detect(img: Image, make_tests: bool = False) -> None:
    img = _improve_image(img)
    blocks: [Block] = _get_blocks(img)
    blocks = _sort_arrows(blocks)
    # distancia de un punto a una recta!!!!

    if make_tests:
        show_detections(blocks, img).show()


def _improve_image(img: Image) -> Image:
    temp: Image = ImageOps.grayscale(img)
    return temp


def _get_blocks(image: Image) -> [Block]:
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./TestStuff/best(L).pt', force_reload=True)

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

    results_list = _remove_duplicates(results_list)

    return results_list


def _remove_duplicates(blocks: [Block]) -> [Block]:
    ids: [int] = []

    for block_a in blocks:
        temp: Block = block_a
        for block_b in blocks:
            if block_a != block_b:
                if _check_if_same_position(block_a, block_b):
                    temp = _block_best_confidence(block_a, block_b)

        if not (temp.id in ids):
            ids.append(temp.id)

    result: [Block] = []

    for item in blocks:
        if item.id in ids:
            result.append(item)

    return result


def _check_if_same_position(block_a: Block, block_b: Block) -> bool:
    is_same_or_not: bool = False

    x_min: int = block_a.x_min - block_b.x_min
    if x_min < 0:
        x_min *= -1

    x_max: int = block_a.x_max - block_b.x_max
    if x_max < 0:
        x_max *= -1

    y_min: int = block_a.y_min - block_b.y_min
    if y_min < 0:
        y_min *= -1

    y_max: int = block_a.y_max - block_b.y_max
    if y_max < 0:
        y_max *= -1

    if (x_min < Constants.DUPLICATE_THRESHOLD) and (x_max < Constants.DUPLICATE_THRESHOLD) and (
            y_min < Constants.DUPLICATE_THRESHOLD) and (y_max < Constants.DUPLICATE_THRESHOLD):
        is_same_or_not = True

    return is_same_or_not


def _block_best_confidence(block_a: Block, block_b: Block) -> Block:
    if block_a.confidence >= block_b.confidence:
        return block_a
    if block_a.confidence < block_b.confidence:
        return block_b


def _sort_arrows(blocks: [Block]) -> [Block]:
    arrows: [Block] = []
    pointers: [Block] = []
    result: [Block] = []

    for block in blocks:
        if block.objet_type == LABEL.pointer:
            pointers.append(block)
        elif (block.objet_type == LABEL.arrow_line_down) or (block.objet_type == LABEL.arrow_line_up) or (
                block.objet_type == LABEL.arrow_line_left) or (block.objet_type == LABEL.arrow_line_right):
            arrows.append(block)
        else:
            result.append(block)

    for arrow in arrows:
        for pointer in pointers:
            is_inside: bool = _is_block_inside(arrow, pointer)
            if is_inside:
                arrow.objet_type = _get_arrow_side(arrow, pointer)
                result.append(arrow)

    return result


def _is_block_inside(block_outside: Block, block_inside: Block) -> bool:

    inside_center_x: int = (block_inside.x_max + block_inside.x_min) / 2
    inside_center_y: int = (block_inside.y_max + block_inside.y_min) / 2

    x_inside: bool = (inside_center_x > block_outside.x_min) and (inside_center_x < block_outside.x_max)
    y_inside: bool = (inside_center_y > block_outside.y_min) and (inside_center_y < block_outside.y_max)

    return x_inside and y_inside


def _get_arrow_side(arrow: Block, pointer: Block) -> LABEL:
    pointer_inside_x: int = (pointer.x_max + pointer.x_min) / 2
    pointer_inside_y: int = (pointer.y_max + pointer.y_min) / 2
    distances = {
        LABEL.arrow_line_up: arrow.y_max - pointer_inside_y,
        LABEL.arrow_line_down: pointer_inside_y - arrow.y_min,
        LABEL.arrow_line_right: pointer_inside_x - arrow.x_min,
        LABEL.arrow_line_left: arrow.x_max - pointer_inside_x
    }
    distances_list = sorted(distances.items(), key=lambda x:x[1])
    return distances_list[3][0]
