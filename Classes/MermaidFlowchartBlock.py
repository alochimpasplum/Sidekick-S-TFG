from Enums import LABEL
from Classes.Block import Block
from Classes.Text import Text
import Constants


class MermaidFlowchartBlock:
    block_name: str
    text: [str] = []
    previous_blocks: [] = []
    next_blocks: [str] = []
    next_blocks_conditionals: {int, str} = {}
    object_type: str

    object_type_conversion = {
        "scan": LABEL.scan,
        "decision": LABEL.decision,
        "print": LABEL.print,
        "process": LABEL.process,
        "arrow_line_up": LABEL.arrow_line_up,
        "arrow_line_down": LABEL.arrow_line_down,
        "arrow_line_right": LABEL.arrow_line_right,
        "arrow_line_left": LABEL.arrow_line_left,
        "pointer": LABEL.pointer
    }

    def __init__(self, block: Block):
        self.block_name = "{}{}".format(Constants.BLOCK_PREFIX, str(block.id))
        texts: [Text] = [x for x in block.Texts]
        for text in texts:
            self.text.append(text.text)
        self.previous_blocks = [str(x) for x in block.Previous_Blocks]
        self.next_blocks = [str(x) for x in block.Next_Blocks]
        self.next_blocks_conditionals = block.Next_Blocks_Conditionals
        self.object_type = block.objet_type.name

    def to_dict(self) -> {}:
        response: {} = {}
        response['block_name'] = self.block_name
        response['text'] = self.text
        response['previous_blocks'] = self.previous_blocks
        response['next_blocks'] = self.next_blocks
        response['next_blocks_conditionals'] = self.next_blocks_conditionals
        response['object_type'] = self.object_type
        return response
    # TODO: revisar que pasa con las asignaciones de memoria
