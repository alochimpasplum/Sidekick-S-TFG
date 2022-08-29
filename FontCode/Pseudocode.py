from Classes import MermaidBlock
from Constants import TAB, NEWLINE


def get_pseudocode(mermaid_blocks: [MermaidBlock]) -> None:
    block: MermaidBlock = __get_first_block(mermaid_blocks)
    pseudocode: [str] = [str]
    blocks_checked: bool = False
    tab_level: int = 1

    pseudocode.append("function {}".format(block.text))

    while not blocks_checked:
        if len(block.next_blocks) > 0:
            if block.object_type.name != 'decision':
                block = block.next_blocks[0]
                # todo: continuar aqui
        else:
            blocks_checked = True


def __get_first_block(mermaid_blocks: [MermaidBlock]) -> MermaidBlock:
    first_block: MermaidBlock = None
    for block in mermaid_blocks:
        if len(block.Previous_Blocks) > 0:
            first_block = block
            break

    return first_block
