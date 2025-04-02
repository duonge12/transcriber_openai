import whisper


model = whisper.load_model("tiny")

class TranscriberModel:
    @staticmethod
    def getScript(path):
        result = model.transcribe(path, language="en")
        return result







