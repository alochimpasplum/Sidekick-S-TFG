from Classes.Block import Block
from Classes.Text import Text
from Enums import LABEL
import Constants
import json


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


def block_list_to_mermaid_json(blocks: [Block]) -> str:
    response: [] = []
    block: Block
    for block in blocks:
        if "arrow" not in block.objet_type.name:
            block_response: {} = {}
            block_response['block_name'] = "{}{}".format(Constants.BLOCK_PREFIX, str(block.id))
            texts: [Text] = [x for x in block.Texts]
            texts_response: [] = []
            for text in texts:
                block_text: {} = {}
                block_text['text'] = text.text
                texts_response.append(block_text)
            block_response['text'] = texts_response
            block_response['previous_blocks'] = [str(x) for x in block.Previous_Blocks]
            block_response['next_blocks'] = [str(x) for x in block.Next_Blocks]
            block_response['next_blocks_conditionals'] = block.Next_Blocks_Conditionals
            block_response['object_type'] = block.objet_type.name

            response.append(block_response)

    return json.dumps(response)
