from flask import Flask, jsonify, request, send_file
from PIL import Image

import Debug
from Classes.Block import Block

import FlowchartObjectDetection


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
        img.show()

        return send_file(img, mimetype='image/jpeg')
    except BaseException as error:
        print(error)
        err: str = "Fallo en la "
        return err, 400


if __name__ == '__main__':
    app.run(debug=True)
