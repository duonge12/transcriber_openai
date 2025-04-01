import os
from flask import Flask, request, jsonify
from controller.transcriber_controller import get_script_controller

app = Flask(__name__)

@app.route('/', methods=['POST'])
def getScript():
    data = request.get_json()
    if data and 'url' in data:
        return get_script_controller(data['url'])
    else:
        return 'Invalid request', 400

@app.route('/')
def hello():
    return "Nhung"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for production