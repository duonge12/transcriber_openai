import whisper


model = whisper.load_model("large")

class TranscriberModel:
    @staticmethod
    def getScript(urls):
        result = model.transcribe(urls, language="vi")
        return result







