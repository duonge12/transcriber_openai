# from model.transcriber.transcriber import transcriber_model
from model.transcriber import TranscriberModel
def get_script_controller(urls):
    try:
        response = TranscriberModel.getScript(urls)
        return {"status": "success", "data": response['text']}
    except Exception as e:
        raise Exception(f"Failed to transcribe file {response.status_code}");
