from PIL import Image
from Classes.MermaidBlock import MermaidBlock
from Enums import mermaid_delete_characters, block_open, block_close
import Constants
import Base64
import requests
import io
import ImgbbUploadFile


def mermaid_blocks_to_mermaid_code(blocks: [MermaidBlock]) -> str:
    mermaid: str = "flowchart LR\n"
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

    return mermaid


def get_mermaid_img(blocks: [MermaidBlock]) -> str:
    base64_string = Base64.encode(mermaid_blocks_to_mermaid_code(blocks))
    image_with_detections: str
    try:
        print('https://mermaid.ink/img/' + base64_string)
        img = Image.open(io.BytesIO(requests.get('https://mermaid.ink/img/' + base64_string).content))
        image_with_detections = ImgbbUploadFile.upload_image(img)
    except BaseException as error:
        print("No se ha podido subir la imagen \n {}".format(error))
        image_with_detections = ""

    return image_with_detections
