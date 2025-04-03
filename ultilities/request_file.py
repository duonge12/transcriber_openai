import requests
import io
import tempfile

def getFile(url):
    try:
        response = requests.get(url, stream=True);
        temp_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False); 
        temp_file.write(response.content);
        temp_file.close();
        return temp_file.name;
    except Exception as e:
        raise Exception(f"Failed to download file. HTTP {response.status_code}");
       