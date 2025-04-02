from flask import Flask,request, jsonify
from controller.transcriber_controller import get_script_controller
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Nhung!"})

@app.route('/', methods=['POST'])
def getTranscript():
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'temp_file.mp4'
        file.save(file_path)
        result=get_script_controller(file);
        # Return the response with the received message
        return jsonify(result)

if __name__ == '__main__':
    from os import environ
    port = int(environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
