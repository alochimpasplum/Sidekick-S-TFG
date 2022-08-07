from flask import Flask, jsonify, request, send_file
from PIL import Image
from FlowchartObjectDetection import detect


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
    files = request.files.get('image')

    detect(Image.open(files))

    return send_file("./TestStuff/HelloWorld.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
