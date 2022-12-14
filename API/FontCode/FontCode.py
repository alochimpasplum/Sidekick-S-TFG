import Pseudocode
from Classes import Block
from Classes import Pseudocode as PseudocodeClass


class FontCode:
    blocks: [Block]
    pseudocode: PseudocodeClass.Pseudocode

    def __init__(self, blocks: [Block]):
        self.blocks = blocks
        self.pseudocode = Pseudocode.get_pseudocode(self.blocks)
