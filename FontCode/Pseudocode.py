import copy

from Classes import MermaidBlock
from Constants import TAB, NEWLINE, VAR_SUFFIX, VARIABLE_START, VARIABLE_END


def get_pseudocode(mermaid_blocks: [MermaidBlock]) -> str:
    blocks: [MermaidBlock] = copy.deepcopy(mermaid_blocks)
    block: MermaidBlock = __get_first_block(blocks)
    blocks.remove(block)

    variables: {} = {}
    pseudocode: [str] = []
    next_blocks: [MermaidBlock]

    pseudocode.append("function {}".format(block.text.rstrip()))
    while len(blocks) > 0:
        next_blocks = __get_next_block(blocks, block)
        if len(next_blocks) == 0:
            break
        elif len(next_blocks) == 1:
            block = next_blocks[0]
            if "decision" not in block.object_type:
                line: str = __block_operation(block, variables)
                pseudocode.append(line)
            else:
                __conditional_block_operation(block, next_blocks, variables)
        else:
            # todo: hacer la operativa del condicional
            block = next_blocks[0]
            for next_block in next_blocks:
                if "start_end" in next_block.object_type:
                    blocks.append(next_block)
    print(pseudocode)
    return "abc"


def __get_first_block(mermaid_blocks: [MermaidBlock]) -> MermaidBlock:
    first_block: MermaidBlock = None
    for block in mermaid_blocks:
        if len(block.previous_blocks) == 0:
            first_block = block
            break
    return first_block


def __get_next_block(mermaid_blocks: [MermaidBlock], actual_block: MermaidBlock) -> [MermaidBlock]:
    next_blocks: [MermaidBlock] = [x for x in mermaid_blocks if x.block_name in actual_block.next_blocks]
    for block in next_blocks:
        mermaid_blocks.remove(block)
    return next_blocks


def __block_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    line: str = ""
    if "scan" in mermaid_block.object_type:
        __scan_operation(mermaid_block, variables)
    elif "print" in mermaid_block.object_type:
        line = __print_operation(mermaid_block, variables)
    elif "process" in mermaid_block.object_type:
        __process_operation(mermaid_block, variables)

    return line


def __conditional_block_operation(conditional_block: MermaidBlock, next_blocks: [MermaidBlock], variables: {}) -> None:
    print("todo")


def __scan_operation(mermaid_block: MermaidBlock, variables: {}) -> None:
    print("todo")


def __print_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    code_line: str = "print("
    text: [str] = mermaid_block.text.split()
    for word in text:
        if VAR_SUFFIX in word:
            var: str = word.replace(VAR_SUFFIX, "")
            code_line += "{}{}{} ".format(VARIABLE_START, var, VARIABLE_END)
            if var not in variables:
                variables[var] = "string"
        elif word != '+':
            code_line += "{} ".format(word)

    code_line = code_line.rstrip()
    code_line += ")"
    return code_line


def __process_operation(mermaid_block: MermaidBlock, variables: {}) -> None:
    print("todo")
