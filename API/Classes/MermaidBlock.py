from Classes.Block import Block
from Classes.Text import Text
import Constants
import copy
import json


class MermaidBlock:
    """This class is used to exchange block information between frontend and backend"""
    block_name: str = ""
    text: str = ""
    previous_blocks: [] = []
    next_blocks: [] = []
    next_blocks_conditionals: {} = {}
    object_type: str = ""

    def __init__(self, block: Block = None, json_dictionary: {str, str}=None):
        if json_dictionary is None:
            self.block_name = "{}{}".format(Constants.BLOCK_PREFIX, str(block.id))
            texts: [Text] = [x for x in block.Texts]
            texts_response: [] = []
            for text in texts:
                texts_response.append(text.text)
            if len(texts_response) > 0:
                self.text = texts_response[0]
            self.previous_blocks = [str("{}{}".format(Constants.BLOCK_PREFIX, x)) for x in block.Previous_Blocks]
            self.next_blocks = [str("{}{}".format(Constants.BLOCK_PREFIX, x)) for x in block.Next_Blocks]
            # todo: comprobar que funciona en cualquier situación (más condicionales)
            # todo: incluir en la documentación la información de deepcopy
            self.next_blocks_conditionals = copy.deepcopy(block.Next_Blocks_Conditionals)
            self.object_type = block.objet_type.name
        else:
            self.block_name = json_dictionary['block_name']
            self.text = json_dictionary['text']
            self.previous_blocks = json_dictionary['previous_blocks']
            self.next_blocks = json_dictionary['next_blocks']
            self.next_blocks_conditionals = json_dictionary['next_blocks_conditionals']
            self.object_type = json_dictionary['object_type']

    def to_string(self) -> str:
        response: str = ""
        response += "Block name: {}\n".format(self.block_name)
        response += "Type: {}\n".format(self.object_type)
        response += "Text: {}\n".format(self.text)
        response += "Previous blocks: {}\n".format(len(self.previous_blocks))
        for i, block in enumerate(self.previous_blocks):
            response += "Previous block {}: {}\n".format(i, block)
        response += "Next blocks: {}\n".format(len(self.next_blocks))
        for i, block in enumerate(self.next_blocks):
            response += "Next block {}: {}\n".format(i, block)
        if "decision" in self.object_type:
            response += "Conditional next neigbours: {}\n".format(len(self.next_blocks_conditionals))
            response += json.dumps(self.next_blocks_conditionals)
            response += "\n"
        return response

    def to_json(self) -> {}:
        block_response: {} = {
            'block_name': self.block_name,
            'text': self.text,
            'previous_blocks': self.previous_blocks,
            'next_blocks': self.next_blocks,
            'next_blocks_conditionals': self.next_blocks_conditionals,
            'object_type': self.object_type
        }
        return block_response
