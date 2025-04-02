from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

if __name__ == '__main__':
    from os import environ
    port = int(environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
