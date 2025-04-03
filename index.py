from flask import Flask,request, jsonify
from controller.transcriber_controller import get_script_controller
from ultilities.request_file import getFile
app = Flask(__name__)



@app.route('/', methods=['POST'])
def getTranscript():
    if request.method == 'POST':
        try:
            data=request.get_json()
            if not data or "url" not in data:
                raise Exception("Data is missing url.");
            url=data['url']
            file= getFile(url)
            result=get_script_controller(file);
            return result;
        except Exception as e:
            return {"status": "error", "message": str(e)}

if __name__ == '__main__':
    from os import environ
    port = int(environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)