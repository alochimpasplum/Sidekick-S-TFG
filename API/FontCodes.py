import MermaidOperations
import Base64
from Classes import MermaidBlock, Pseudocode
from FontCode import Pseudocode as PseudocodeGenerator
from FontCode.Python import Python
from JsonOperations import json_to_mermaid_blocks, json_to_string_list


def get_font_codes(raw_mermaid_blocks: [str], raw_languages: [str]) -> {}:
    response: {} = {}
    mermaid_blocks: [MermaidBlock] = json_to_mermaid_blocks(raw_mermaid_blocks)
    languages: [str] = json_to_string_list(raw_languages)
    pseudocode: Pseudocode = PseudocodeGenerator.get_pseudocode(mermaid_blocks)
    if 'mermaid' in languages:
        font_code: str = MermaidOperations.mermaid_blocks_to_mermaid_code(mermaid_blocks)
        print("--- MERMAID ---")
        print(font_code)
        response['mermaid'] = Base64.encode(font_code)
    if 'pseudo_language' in languages:
        font_code: str = pseudocode.to_pseudocode()
        print("--- PSEUDOCODE ---")
        print(font_code)
        response['pseudo_language'] = Base64.encode(font_code)
    if 'python' in languages:
        python: Python = Python(pseudocode)
        font_code: str = python.to_pseudocode()
        print("--- PYTHON ---")
        print(font_code)
        response['python'] = Base64.encode(font_code)

    return response
