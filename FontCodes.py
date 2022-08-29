import MermaidOperations
import Base64
from Classes import MermaidBlock
from JsonOperations import json_to_mermaid_blocks, json_to_string_list


def get_font_codes(raw_mermaid_blocks: [str], raw_languages: [str]) -> {}:
    response: {} = {}
    mermaid_blocks: [MermaidBlock] = json_to_mermaid_blocks(raw_mermaid_blocks)
    languages: [str] = json_to_string_list(raw_languages)
    for language in languages:
        if language == 'mermaid':
            response['mermaid'] = Base64.encode(MermaidOperations.mermaid_blocks_to_mermaid_code(mermaid_blocks))

    return response
