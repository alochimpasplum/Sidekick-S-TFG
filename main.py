from flask import Flask, jsonify, request, send_file
from PIL import Image

import Debug
from Classes.Block import Block

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


if __name__ == '__main__':
    app.run(debug=True)
