import copy

from Classes import MermaidBlock
from Classes import Pseudocode as PseudocodeClass
from Constants import TAB, VAR_SUFFIX, VARIABLE, PRINT, SCAN, FUNC_SUFFIX, FUNCTION, MATH_OPERATION


def get_pseudocode(mermaid_blocks: [MermaidBlock]) -> PseudocodeClass.Pseudocode:
    blocks: [MermaidBlock] = copy.deepcopy(mermaid_blocks)
    block: MermaidBlock = __get_first_block(mermaid_blocks)

    variables: {} = {}
    functions: [] = []
    pseudocode: [str] = []
    next_blocks: [MermaidBlock]
    tab_index: int = 0

    if not ("inicio" or "start") in block.text:
        tab_index = 1
        pseudocode.append("function {}".format(block.text.rstrip()))

    while len(blocks) > 0:
        next_blocks = __get_next_block(blocks, block)

        if len(next_blocks) == 0:
            break
        elif len(next_blocks) == 1:
            if "decision" not in block.object_type or "start_end" not in block.object_type:
                line: str = __block_operation(block, variables, functions)
                line = __add_tabs(line, tab_index)
                pseudocode.append(line)
            elif "decision" in block.object_type:
                # todo: hacer la operativa del condicional
                __conditional_block_operation(block, next_blocks, variables, functions)
            block = next_blocks[0]
        else:
            # todo: hacer la operativa del condicional
            block = next_blocks[0]
            for next_block in next_blocks:
                if "start_end" in next_block.object_type:
                    blocks.append(next_block)

    pseudocode.append(__add_variables(variables))

    pseudocode_class = PseudocodeClass.Pseudocode(pseudocode, functions, variables)

    return pseudocode_class


def __get_first_block(mermaid_blocks: [MermaidBlock]) -> MermaidBlock:
    first_block: MermaidBlock = None
    for block in mermaid_blocks:
        if len(block.previous_blocks) == 0:
            first_block = block
            break
    mermaid_blocks.remove(first_block)
    return first_block


def __get_next_block(mermaid_blocks: [MermaidBlock], actual_block: MermaidBlock) -> [MermaidBlock]:
    next_blocks: [MermaidBlock] = []
    if len(actual_block.next_blocks) > 0:
        next_blocks = [x for x in mermaid_blocks if x.block_name in actual_block.next_blocks]
        for block in next_blocks:
            mermaid_blocks.remove(block)
        return next_blocks

    return next_blocks


def __block_operation(mermaid_block: MermaidBlock, variables: {}, functions: []) -> str:
    line: str = ""
    if "scan" in mermaid_block.object_type:
        line = __scan_operation(mermaid_block, variables)
    elif "print" in mermaid_block.object_type:
        line = __print_operation(mermaid_block, variables)
    elif "process" in mermaid_block.object_type:
        line = __process_operation(mermaid_block, variables, functions)

    return line


def __conditional_block_operation(conditional_block: MermaidBlock, next_blocks: [MermaidBlock],
                                  variables: {}, functions: []) -> []:
    print("todo")


def __scan_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    code_line: str = SCAN
    if VAR_SUFFIX in mermaid_block.text:
        var: str = mermaid_block.text.replace(VAR_SUFFIX, "")
        if var not in variables:
            variables[var] = "string"
            code_line += var
    else:
        variables[mermaid_block.text] = "string"
        code_line += mermaid_block.text
    code_line = code_line.rstrip()

    return code_line


def __print_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    code_line: str = PRINT
    text: [str] = mermaid_block.text.split()
    for word in text:
        if VAR_SUFFIX in word:
            var: str = word.replace(VAR_SUFFIX, "")
            code_line += "{}{} ".format(VARIABLE, var)
            if var not in variables:
                variables[var] = "string"
        elif word != '+':
            code_line += "{} ".format(word)
    code_line = code_line.rstrip()

    return code_line


def __process_operation(mermaid_block: MermaidBlock, variables: {}, functions: []) -> str:
    code_line: str = ""
    text: [str] = mermaid_block.text.split()

    # Process with function
    if FUNC_SUFFIX in mermaid_block.text:
        func: str = mermaid_block.text.replace(FUNC_SUFFIX, "")
        if func in functions:
            code_line += "{}{}".format(FUNCTION, func)
        else:
            functions.append(func)
            code_line += "{}{}".format(FUNCTION, func)
    # Process with math operation
    elif ('+' or '-' or '*' or '/') in mermaid_block.text:
        code_line += MATH_OPERATION
        for word in text:
            if VAR_SUFFIX in word:
                var: str = word.replace(VAR_SUFFIX, "")
                code_line += "{}{} ".format(VARIABLE, var)
                variables[var] = "int"
            else:
                code_line += "{} ".format(word)

    code_line = code_line.rstrip()
    return code_line


def __add_tabs(line: str, tab_number: int) -> str:
    tabs: str = ""
    for x in range(tab_number):
        tabs += TAB
    return tabs + line


def __add_variables(variables: {}) -> [str]:
    var_lines: [str] = []
    for x in variables.keys():
        var_lines.append("{}{}".format(VARIABLE, x))
    return var_lines
