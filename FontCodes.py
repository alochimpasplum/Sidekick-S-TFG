import MermaidOperations
import Base64
from Classes import MermaidBlock
from FontCode import Pseudocode as PseudocodeGenerator
from Classes import Pseudocode
from JsonOperations import json_to_mermaid_blocks, json_to_string_list


def get_font_codes(raw_mermaid_blocks: [str], raw_languages: [str]) -> {}:
    response: {} = {}
    mermaid_blocks: [MermaidBlock] = json_to_mermaid_blocks(raw_mermaid_blocks)
    languages: [str] = json_to_string_list(raw_languages)
    pseudocode: Pseudocode = PseudocodeGenerator.get_pseudocode(mermaid_blocks)
    if 'mermaid' in languages:
        response['mermaid'] = Base64.encode(MermaidOperations.mermaid_blocks_to_mermaid_code(mermaid_blocks))
    if 'pseudo_language' in languages:
        response['pseudo_language'] = Base64.encode(pseudocode.to_pseudocode())

    return response
