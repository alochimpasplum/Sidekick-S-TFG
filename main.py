import json
from Enums import supported_languages
from flask import Flask, jsonify, request, send_file, abort
from PIL import Image

import Debug
import MermaidOperations
from Classes.Block import Block
from Classes.MermaidBlock import MermaidBlock

import FlowchartObjectDetection
import JsonOperations
import ImgbbUploadFile


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/helloWorld', methods=['GET'])
def hello_world():
    name = request.args.get('name', "")
    response = {'message': 'hello world ' + name}
    return jsonify(response)


@app.route('/getDetectedImage', methods=['GET'])
def get_detected_image():
    try:
        files = request.files.get('image')
        img: Image = Image.open(files)
        img = FlowchartObjectDetection.get_detected_image(img)

        return send_file(img, mimetype='image/jpeg')
    except BaseException as error:
        print(error)
        err: str = "Error during image inferring"
        return err, 400


@app.route('/getBlocksFromImage', methods=['POST'])
def get_detected_blocks():
    try:
        files = request.files.get('image')
        img: Image = Image.open(files)
        blocks: [Block] = FlowchartObjectDetection.get_blocks(img)

        return JsonOperations.block_list_to_block_json(blocks)
    except BaseException as error:
        print(error)
        err: str = "Error during image inferring"
        return err, 400


@app.route('/getMermaidFromImage', methods=['POST'])
def get_detected_mermaid():
    try:
        files = request.files.get('image')
        img: Image = Image.open(files)
        blocks: [Block] = FlowchartObjectDetection.get_blocks(img)
        image_with_detections: str
        try:
            image_with_detections = ImgbbUploadFile.upload_image(Debug.get_detections(blocks, img))
        except BaseException as error:
            print("No se ha podido subir la imagen \n {}".format(error))
            image_with_detections = ""

        return JsonOperations.block_list_to_mermaid_json(blocks, image_with_detections)
    except BaseException as error:
        print(error)
        err: str = "Error during image inferring"
        return err, 400


@app.route('/getMermaidImage', methods=['GET'])
def get_mermaid_img():
    query: str = request.args.get("MermaidBlocks", "")
    if query != "":
        url: str = JsonOperations.json_to_mermaid_image(query)
        return {'image_mermaid': url}
    else:
        abort(400)


@app.route('/getSupportedLanguages', methods=['GET'])
def get_supported_languages():
    return {'SupportedLanguages': supported_languages}


@app.route('/getCode', methods=['GET'])
def get_code():
    languajes: str = request.args.get("Languages", "")
    mermaid_blocks: str = request.args.get("MermaidBlocks", "")
    print(languajes)
    print(mermaid_blocks)
    return {'message': "hello world"}


if __name__ == '__main__':
    app.run(debug=True)
