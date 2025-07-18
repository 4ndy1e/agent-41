import os
from config import max_chars
from path_validation import validate_path

def get_file_content(working_directory, file_path):
    validationMessage = validate_path(working_directory, file_path)
    
    if validationMessage:
        return validationMessage
    
    full_path = os.path.join(working_directory, file_path)
    full_abs_path = os.path.abspath(full_path)
    
    # read the contents of the file 
    try:
        with open(full_abs_path, "r") as f:
            file_contents = f.read(max_chars)
            
            if len(file_contents) > max_chars:
                file_contents += f"[...File '{file_path}' trauncated at 10000 characters]."
            
            return file_contents
    except Exception as error:
        return f"Error: {error}"
    
    
        
    