from flask import Flask,request, jsonify
from controller.transcriber_controller import get_script_controller
from io import BytesIO
import librosa
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Nhung!"})

@app.route('/', methods=['POST'])
def getTranscript():
    if request.method == 'POST':
        file = request.files['file']
        audio_file = file.read()  
        
      
        audio_stream = BytesIO(audio_file)
        audio= librosa.load(audio_stream, sr=16000, mono=True) 
        result=get_script_controller(audio);
        return jsonify(result)

if __name__ == '__main__':
    from os import environ
    port = int(environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
