# from model.transcriber.transcriber import transcriber_model
from model.transcriber import TranscriberModel
def get_script_controller(path):
    try:
        response = TranscriberModel.getScript(path)
        return {"status": "success", "data": response['text']}
    except Exception as e:
        return {"status": "error", "message": str(e)}
