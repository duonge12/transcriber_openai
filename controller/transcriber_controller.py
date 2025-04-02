# from model.transcriber.transcriber import transcriber_model
from model.transcriber import TranscriberModel
def get_script_controller(file):
    try:
        response = TranscriberModel.getScript(file)
        return {"status": "success", "data": response['text']}
    except Exception as e:
        return {"status": "error", "message": str(e)}
