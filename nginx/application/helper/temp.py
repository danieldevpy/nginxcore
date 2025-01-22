
import tempfile

def create_file(content: str, delete=False):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content.encode())
        return temp_file.name
    

