from Classes.MermaidBlock import MermaidBlock
from Enums import mermaid_delete_characters, block_open, block_close
import Constants
import base64


def mermaid_blocks_to_mermaid_code(blocks: [MermaidBlock]) -> str:
    mermaid: str = "flowchart TD\n"
    block: MermaidBlock
    for block in blocks:
        if len(block.text) > 0:
            text: str = block.text
            for char in mermaid_delete_characters:
                text = text.replace(char, '')
            mermaid += "\t{}{}{}{}\n".format(block.block_name, block_open[block.object_type],
                                             text, block_close[block.object_type])
        else:
            mermaid += "\t{}{}{}{}\n".format(block.block_name, block_open[block.object_type],
                                             block.block_name, block_close[block.object_type])

    for block in blocks:
        if block.object_type == "decision":
            for key, value in block.next_blocks_conditionals.items():
                mermaid += "\t{}--{}-->{}{}\n".format(block.block_name, value, Constants.BLOCK_PREFIX, key)
        else:
            for next_block in block.next_blocks:
                mermaid += "\t{}-->{}\n".format(block.block_name, next_block)

    graphbytes = mermaid.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string
