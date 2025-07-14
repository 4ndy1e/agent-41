import os

def get_files_info(working_directory, directory=None): 
    full_path = os.path.join(working_directory, directory)
    working_directory_abs = os.path.abspath(working_directory)
    full_path_abs = os.path.abspath(full_path)
    
    contents = "Results for current directory:\n"
    
    # condtional checks
    # check if directory is outside the working_directory
    if not full_path_abs.startswith(working_directory_abs):
        contents += f"Error: Cannot list '{directory}' as it is outside the permitted working directory\n"
        return contents
    
    # check if directory is a valid directory
    if not os.path.isdir(full_path_abs):
        contents += f"Error: '{directory}' is not a directory\n"
        return contents
    
    # generate the contents for the directory if conditonals satisfied
    directory_content_names = os.listdir(full_path)
    
    for name in directory_content_names:
        # get current file path and information
        try: 
            file_path = os.path.join(os.path.join(full_path, name))
            
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            
            contents += f" - {name}: file_size={file_size} bytes, is_dir={is_dir}\n"
        except Exception as error:
            return f"Error: {error}"
            
        
    return contents
    
    

    