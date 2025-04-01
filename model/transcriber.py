import whisper


model = whisper.load_model("base")

class TranscriberModel:
    @staticmethod
    def getScript(path):
        result = model.transcribe(path, language="vi")
        return result







