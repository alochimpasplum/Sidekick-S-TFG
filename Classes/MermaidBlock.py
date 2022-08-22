from Classes.Block import Block
from Classes.Text import Text
import Constants
import copy


class MermaidBlock:
    """This class is used to exchange block information between frontend and backend"""
    block_name: str = ""
    text: str = ""
    previous_blocks: [] = []
    next_blocks: [] = []
    next_blocks_conditionals: {} = {}
    object_type: str = ""

    def __init__(self, block: Block):
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
