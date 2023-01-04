from Enums import supported_languages
from FontCode import Pseudocode
from Classes import Block
from Classes import Pseudocode as PseudocodeClass
from FontCode.ANTLR4_Parser import Antlr4
from FontCode.ANTLR4_Parser.Languages.Language import Language


class FontCode:
    blocks: [Block] = []
    pseudocode: PseudocodeClass.Pseudocode
    lines: [str] = []

    def __init__(self, blocks: [Block], language: supported_languages):
        self.blocks = blocks
        self.pseudocode = Pseudocode.get_pseudocode(self.blocks)

        # print(self.pseudocode.to_string())
        # print(self.pseudocode.to_antlr4_pseudocode())

        self.lines = Antlr4.antlr4_operation(self.pseudocode.to_antlr4_pseudocode(), language)
