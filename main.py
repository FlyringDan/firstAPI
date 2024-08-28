import base64
from flask import Flask, send_file, request, jsonify, render_template
from Recognizer import recognize_the_text
import requests

app = Flask(__name__)

PATH_TO_DEC_IMG = 'C:/Users/danii/Desktop/DanFolder/pythonProjects/homeWorkNex/API/Files/png_folder/decoded_image.png'


@app.route('/', methods=['GET', 'POST'])
def process_file():
    base64_string = request.json.get('image_base64')
    if not base64_string:
        return jsonify({"error": "No base64_string provided"}), 400
    image_data = base64.b64decode(base64_string)
    with open(PATH_TO_DEC_IMG, 'wb') as file:
        file.write(image_data)
    recognize_the_text(PATH_TO_DEC_IMG)

    # return send_file('Files/png_folder/data.json', mimetype='application/json')


@app.route('/load', methods=['GET'])
def load_file():
    return send_file('Files/png_folder/data.json', mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=False)
# http://127.0.0.1:80/load
