from Classes.Block import Block
from Classes.Text import Text
from Classes.MermaidBlock import MermaidBlock
import MermaidOperations
import json
import os


def block_list_to_block_json(blocks: [Block]) -> str:
    response: [] = []

    for block in blocks:
        if "arrow" not in block.objet_type.name:
            block_response: {} = {}
            block_response['id'] = str(block.id)
            block_response['object_type'] = block.objet_type.name
            block_response['x_min'] = str(block.x_min)
            block_response['x_max'] = str(block.x_max)
            block_response['y_min'] = str(block.y_min)
            block_response['y_max'] = str(block.y_max)
            block_response['confidence'] = str(block.confidence)

            texts: [Text] = [x for x in block.Texts]
            texts_response: [] = []
            for text in texts:
                block_text: {} = {}
                block_text['id'] = str(text.id)
                block_text['x_min'] = str(text.x_min)
                block_text['x_max'] = str(text.x_max)
                block_text['y_min'] = str(text.y_min)
                block_text['y_max'] = str(text.y_max)
                block_text['confidence'] = str(text.confidence)
                block_text['text'] = text.text
                texts_response.append(block_text)

            block_response['texts'] = texts_response
            block_response['next_blocks'] = [str(x) for x in block.Next_Blocks]
            block_response['previous_blocks'] = [str(x) for x in block.Previous_Blocks]
            block_response['conditionals'] = block.Next_Blocks_Conditionals

            response.append(block_response)

    return json.dumps(response)


def block_list_to_mermaid_json(blocks: [Block], image_with_detections: str) -> str:
    response: {} = {}
    mermaid_blocks: [] = []
    mermaid_blocks_json: [] = []

    block: Block
    for block in blocks:
        if "arrow" not in block.objet_type.name:
            block_response: MermaidBlock = MermaidBlock(block)
            mermaid_blocks.append(block_response)
            mermaid_blocks_json.append(block_response.to_json())

    response['mermaid_blocks'] = mermaid_blocks_json
    response['mermaid_code'] = MermaidOperations.mermaid_blocks_to_mermaid_code(mermaid_blocks)
    response['image_with_detections'] = image_with_detections
    return json.dumps(response)
