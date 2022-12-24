import copy
import Constants
import re

from Classes import Block
from Classes import Pseudocode as PseudocodeClass


def get_pseudocode(blocks: [Block]) -> PseudocodeClass.Pseudocode:
    blocks: [Block] = copy.deepcopy(blocks)
    block: Block = __get_first_block(blocks)

    variables: {} = {}
    functions: [] = []
    pseudocode: [str] = []
    next_blocks: [Block] = []
    tab_index: int = 0

    if ("START" in block.Texts[0].text) or ("INICIO" in block.Texts[0].text):
        tab_index = 1
        # pseudocode.append("{} {}".format(Constants.MAIN_FUNCTION, block.Texts[0].text.rstrip()))
        pseudocode.append(Constants.MAIN_FUNCTION)

    next_blocks = __get_next_block(blocks, block)
    block = next_blocks[0]
    while len(blocks) > 0:
        next_blocks = __get_next_block(blocks, block)

        if len(next_blocks) == 0:
            break
        elif len(next_blocks) == 1:
            if ("decision" not in block.object_type.name) or ("start_end" not in block.object_type.name):
                line: str = __block_operation(block, variables, functions)
                line = __add_tabs(line, tab_index)
                pseudocode.append(line)

            block = next_blocks[0]
        elif len(next_blocks) > 1:
            conditional_operation = __conditional_block_operation(block, next_blocks, blocks, variables, functions)
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


def __get_first_block(mermaid_blocks: [Block]) -> Block:
    first_block: Block = None
    block: Block
    for block in mermaid_blocks:
        if len(block.Previous_Blocks) == 0:
            first_block = block
            break
    mermaid_blocks.remove(first_block)
    return first_block


def __get_next_block(mermaid_blocks: [Block], actual_block: Block) -> [Block]:
    next_blocks: [Block] = []
    if len(actual_block.Next_Blocks) > 0:
        next_blocks = [x for x in mermaid_blocks if x.id in actual_block.Next_Blocks]
        """
        for block in next_blocks:
            if block in mermaid_blocks:
                mermaid_blocks.remove(block)
        """
        return next_blocks

    return next_blocks


def __block_operation(mermaid_block: Block, variables: {}, functions: []) -> str:
    line: str = ""
    if "scan" in mermaid_block.object_type.name:
        line = __scan_operation(mermaid_block, variables)
    elif "print" in mermaid_block.object_type.name:
        line = __print_operation(mermaid_block, variables)
    elif "process" in mermaid_block.object_type.name:
        line = __process_operation(mermaid_block, variables, functions)

    return line


# todo: implementar
def __conditional_block_operation(conditional_block: Block, next_blocks: [Block],
                                  mermaid_blocks: [Block], variables: {}, functions: [])\
                                    -> [[str], Block]:
    """Return [0] -> Code lines\n
    Return [1] -> Final conditional's block"""
    lines: [str] = []
    next_block: Block
    next_blocks_side: [Block] = []
    final_conditional_block: Block = __check_final_conditional_block(next_blocks, mermaid_blocks)

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


# todo: implementar
def __scan_operation(mermaid_block: Block, variables: {}) -> str:
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


def __print_operation(mermaid_block: Block, variables: {}) -> str:
    code_line: str = Constants.PRINT
    text: [str] = mermaid_block.Texts[0].text.split()
    for word in text:
        if word in variables:
            code_line += word
        else:
            code_line += Constants.STRING
            code_line += word
    code_line = code_line.rstrip()

    return code_line


def __process_operation(mermaid_block: Block, variables: {}, functions: []) -> str:
    code_line: str = ""
    text: [str] = mermaid_block.Texts[0].text.split()
    local_variables: {} = {}

    # Process with function
    # todo: cambiar la palabra dedicada "_func" por la terminación "()" en el texto OCR reconocido
    if Constants.FUNC_SUFFIX in mermaid_block.Texts[0].text:
        func: str = mermaid_block.Texts[0].text.replace(Constants.FUNC_SUFFIX, "")
        if func in functions:
            code_line += "{}{}".format(Constants.FUNCTION, func)
        else:
            functions.append(func)
            code_line += "{}{}".format(Constants.FUNCTION, func)
    # Process with math operation
    # elif ("+" or "-" or "*" or "/" or "=") in text:
    # todo: eliminar la necesidad de indicar que es una variable en el texto OCR escrito
    elif ("-" in text) or ("+" in text) or ("*" in text) or ("/" in text) or ("=" in text):
        for t in text:
            # compruebo si se trata de una variable
            if re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", t):
                # todo: cambiar este valor por defecto cuando se acepten strings
                # local_variables[t] = Constants.STRING
                local_variables[t] = Constants.INTEGER
                code_line += t
            else:
                code_line += t
        # todo: agregar limitación, solo se aceptan operaciones matemáticas, nada de STRINGS
        if ("-" in text) or ("+" in text) or ("*" in text) or ("/" in text):
            for key, value in local_variables.items():
                local_variables[key] = Constants.INTEGER
    # todo: ¿que pasa si no hay ninguna operación dentro del bloque de proceso?

    if len(local_variables) > 0:
        for key, value in local_variables.items():
            variables[key] = value

    code_line = code_line.rstrip()
    return code_line


def __add_tabs(line: str, tab_number: int) -> str:
    tabs: str = ""
    for x in range(tab_number):
        tabs += Constants.TAB
    return tabs + line
    # return line


def __check_final_conditional_block(next_blocks: [Block],
                                    mermaid_blocks: [Block]) -> Block:
    next_blocks_side: [Block] = []
    initial_next_blocks: [Block] = next_blocks
    final_blocks: [Block] = []
    next_block: Block
    next_block_side: Block

    for next_block in initial_next_blocks:
        next_block_side = next_block

        while len(next_block_side.previous_blocks) < 2:
            next_blocks_side = __get_next_block(mermaid_blocks, next_block_side)
            next_block_side = next_blocks_side[0]

        final_blocks.append(next_block_side)

    return final_blocks[0]
