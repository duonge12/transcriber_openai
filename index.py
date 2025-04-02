import os
from flask import Flask, request, jsonify
from controller.transcriber_controller import get_script_controller

app = Flask(__name__)

@app.route('/')
def hello():
    return "Nhung"




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for production