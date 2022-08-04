# Functions in this file handles everything related to flowchart object detection
from Classes import Block
from Debug import show_detections
import torch
import json
import Constants


def detect(img: str, make_tests: bool = False) -> [Block]:
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./TestStuff/best(L).pt', force_reload=True)

    # Inference
    results = model(img)

    serialized_json = results.pandas().xyxy[0].to_json(orient="records")

    deserialized_json = json.loads(serialized_json)

    results_list: [Block] = []

    for i, entry in enumerate(deserialized_json):
        if entry['confidence'] > Constants.CONFIDENCE_THRESHOLD:
            temp: Block = Block(i, entry['xmin'], entry['ymin'], entry['xmax'],
                                entry['ymax'], entry['confidence'], entry['name'])
            results_list.append(temp)

    results_list = _remove_duplicates(results_list, make_tests)

    if make_tests:
        show_detections(results_list, img)

    return results_list


def _remove_duplicates(blocks: [Block], make_tests: bool) -> [Block]:
    result: [Block] = []

    for block_a in blocks:
        for block_b in blocks:
            if block_a != block_b:
                if _check_if_is_same_block(block_a, block_b, make_tests):
                    temp: Block = _block_best_confidence(block_a, block_b)
                    append_or_not: bool = True
                    for block in result:
                        if block.id == temp.id:
                            append_or_not = False

                    if make_tests:
                        print(block_a.objet_type, block_b.objet_type, temp.objet_type, append_or_not, "\n")

                    if append_or_not:
                        result.append(temp)
                else:
                    result.append(block_a)

    return result


def _check_if_is_same_block(block_a: Block, block_b: Block, make_tests: bool) -> bool:
    x_min: int = block_a.x_min - block_b.x_min
    is_same_or_not: bool = False

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

    if (x_min < Constants.DUPLICATE_THRESHOLD) and (x_min < Constants.DUPLICATE_THRESHOLD) and (
            x_min < Constants.DUPLICATE_THRESHOLD) and (x_min < Constants.DUPLICATE_THRESHOLD):
        is_same_or_not = True

    if make_tests:
        print(is_same_or_not)
        print("A: ", block_a.to_string())
        print("B: ", block_b.to_string())
        print("x_min:", x_min, "x_max:", x_max, "y_min:", y_min, "y_max:", y_max, "\n")

    return is_same_or_not


def _block_best_confidence(block_a: Block, block_b: Block) -> Block:
    if block_a.confidence >= block_b.confidence:
        return block_a
    if block_a.confidence < block_b.confidence:
        return block_b
