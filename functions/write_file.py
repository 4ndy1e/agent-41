from path_validation import validate_path

def write_file(working_directory, file_path, content):
    validationMessage = validate_path(working_directory, file_path)
    
    if validationMessage:
        return validationMessage