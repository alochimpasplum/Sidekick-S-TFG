from FontCode import Pseudocode
from Classes import Block
from Classes import Pseudocode as PseudocodeClass
from FontCode.ANTLR4_Parser import Antlr4


class FontCode:
    blocks: [Block] = []
    pseudocode: PseudocodeClass.Pseudocode

    def __init__(self, blocks: [Block]):
        self.blocks = blocks
        self.pseudocode = Pseudocode.get_pseudocode(self.blocks)

        Antlr4.antlr4_operation(self.pseudocode.to_antlr4_pseudocode())
