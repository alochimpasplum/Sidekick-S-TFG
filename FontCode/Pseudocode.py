import copy
import Constants

from Classes import MermaidBlock
from Classes import Pseudocode as PseudocodeClass


def get_pseudocode(mermaid_blocks: [MermaidBlock]) -> PseudocodeClass.Pseudocode:
    blocks: [MermaidBlock] = copy.deepcopy(mermaid_blocks)
    block: MermaidBlock = __get_first_block(mermaid_blocks)

    variables: {} = {}
    functions: [] = []
    pseudocode: [str] = []
    next_blocks: [MermaidBlock] = []
    tab_index: int = 0

    # todo: fix this with "or" statement
    if not ("start" in block.text):
        if not ("inicio" in block.text):
            tab_index = 1
            pseudocode.append("{} {}".format(Constants.MAIN_FUNCTION, block.text.rstrip()))
    pseudocode.append(Constants.VARIABLE_DECLARATIONS)

    next_blocks = __get_next_block(blocks, block)
    block = next_blocks[0]
    while len(blocks) > 0:
        next_blocks = __get_next_block(blocks, block)

        if len(next_blocks) == 0:
            break
        elif len(next_blocks) == 1:
            if ("decision" not in block.object_type) or ("start_end" not in block.object_type):
                line: str = __block_operation(block, variables, functions)
                line = __add_tabs(line, tab_index)
                pseudocode.append(line)

            block = next_blocks[0]
        elif len(next_blocks) > 1:
            conditional_operation = __conditional_block_operation(block, next_blocks, mermaid_blocks,
                                                              variables, functions)
            next_lines: [str] = conditional_operation[0]
            block = conditional_operation[1]
            for line in next_lines:
                line = line.rstrip()
                if len(line) > 0:
                    line = __add_tabs(line, tab_index)
                    pseudocode.append(line)

    pseudocode.append(Constants.END_CODE)

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
        """
        for block in next_blocks:
            if block in mermaid_blocks:
                mermaid_blocks.remove(block)
        """
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
                                  mermaid_blocks: [MermaidBlock], variables: {}, functions: [])\
                                    -> [[str], MermaidBlock]:
    """Return [0] -> Code lines\n
    Return [1] -> Final conditional's block"""
    lines: [str] = []
    next_block: MermaidBlock
    next_blocks_side: [MermaidBlock] = []
    final_conditional_block: MermaidBlock = __check_final_conditional_block(next_blocks, mermaid_blocks)

    # If statement
    if len(next_blocks) == 2:

        if_statement: str = "{}{}{}".format(Constants.IF, conditional_block.text, Constants.IF_TRUE_START)
        if Constants.VAR_SUFFIX in if_statement:
            if_statement = if_statement.replace(Constants.VAR_SUFFIX, "")
            if_statement = "{}{}".format(Constants.VARIABLE, if_statement)
        lines.append(if_statement)

        next_block_name: str = "Block"
        for key, value in conditional_block.next_blocks_conditionals.items():
            if value == "yes":
                next_block_name = "Block{}".format(key)
        next_block = [x for x in mermaid_blocks if x.block_name == next_block_name][0]

        while next_block != final_conditional_block:
            if not ("decision" in next_block.object_type):
                if not ("start-end" in next_block.text):
                    line: str = __block_operation(next_block, variables, functions)
                    line = __add_tabs(line, 1)
                    lines.append(line)
                    next_blocks_side = __get_next_block(mermaid_blocks, next_block)
                    next_block = next_blocks_side[0]

        lines.append("{}{}".format(Constants.IF_TRUE_END, Constants.IF_FALSE_START))
        for key, value in conditional_block.next_blocks_conditionals.items():
            if value == "no":
                next_block_name = "Block{}".format(key)
        next_block = [x for x in mermaid_blocks if x.block_name == next_block_name][0]
        while next_block != final_conditional_block:
            if not ("decision" in next_block.object_type):
                if not ("start-end" in next_block.text):
                    line: str = __block_operation(next_block, variables, functions)
                    line = __add_tabs(line, 1)
                    lines.append(line)
                    next_blocks_side = __get_next_block(mermaid_blocks, next_block)
                    next_block = next_blocks_side[0]

        lines.append("{}".format(Constants.IF_FALSE_END))

    return [lines, final_conditional_block]


def __scan_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    code_line: str = Constants.SCAN
    if Constants.VAR_SUFFIX in mermaid_block.text:
        var: str = mermaid_block.text.replace(Constants.VAR_SUFFIX, "")
        if var not in variables:
            variables[var] = "string"
            code_line += var
    else:
        variables[mermaid_block.text] = "string"
        code_line += mermaid_block.text
    code_line = code_line.rstrip()

    return code_line


def __print_operation(mermaid_block: MermaidBlock, variables: {}) -> str:
    code_line: str = Constants.PRINT
    text: [str] = mermaid_block.text.split()
    for word in text:
        if Constants.VAR_SUFFIX in word:
            var: str = word.replace(Constants.VAR_SUFFIX, "")
            code_line += "{}{} ".format(Constants.VARIABLE, var)
            if var not in variables:
                variables[var] = "string"
        elif word != "+":
            code_line += "{} ".format(word)
    code_line = code_line.rstrip()

    return code_line


def __process_operation(mermaid_block: MermaidBlock, variables: {}, functions: []) -> str:
    code_line: str = ""
    text: [str] = mermaid_block.text.split()

    # Process with function
    if Constants.FUNC_SUFFIX in mermaid_block.text:
        func: str = mermaid_block.text.replace(Constants.FUNC_SUFFIX, "")
        if func in functions:
            code_line += "{}{}".format(Constants.FUNCTION, func)
        else:
            functions.append(func)
            code_line += "{}{}".format(Constants.FUNCTION, func)
    # Process with math operation
    # elif ("+" or "-" or "*" or "/" or "=") in text:
    elif ("-" in text) or ("+" in text) or ("*" in text) or ("/" in text) or ("=" in text):
        code_line += Constants.MATH_OPERATION
        for word in text:
            if Constants.VAR_SUFFIX in word:
                var: str = word.replace(Constants.VAR_SUFFIX, "")
                code_line += "{}{} ".format(Constants.VARIABLE, var)
                variables[var] = "int"
            else:
                code_line += "{} ".format(word)

    code_line = code_line.rstrip()
    return code_line


def __add_tabs(line: str, tab_number: int) -> str:
    tabs: str = ""
    for x in range(tab_number):
        tabs += Constants.TAB
    return tabs + line


def __add_variables(variables: {}) -> [str]:
    var_lines: [str] = []
    for x in variables.keys():
        var_lines.append("{}{}".format(Constants.VARIABLE, x))
    return var_lines


def __check_final_conditional_block(next_blocks: [MermaidBlock],
                                    mermaid_blocks: [MermaidBlock]) -> MermaidBlock:
    next_blocks_side: [MermaidBlock] = []
    initial_next_blocks: [MermaidBlock] = next_blocks
    final_blocks: [MermaidBlock] = []
    next_block: MermaidBlock
    next_block_side: MermaidBlock

    for next_block in initial_next_blocks:
        next_block_side = next_block

        while len(next_block_side.previous_blocks) < 2:
            next_blocks_side = __get_next_block(mermaid_blocks, next_block_side)
            next_block_side = next_blocks_side[0]

        final_blocks.append(next_block_side)

    return final_blocks[0]
