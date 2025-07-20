import os 

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    working_directory_abs_path = os.path.abspath(working_directory)
    full_abs_path = os.path.abspath(full_path)    
    
    if not full_abs_path.startswith(working_directory_abs_path):
        return f"Error: Cannot write to '{file_path} as it is outside the permitted working directory"
    
    try:         
        directory_name = os.path.dirname(full_abs_path)
        
        # create file_path if it does not exist 
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            
        # overwrite into the file 
        with open(full_abs_path, "w") as f:
            f.write(content)
            
        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"
        
    except Exception as e:
        return f"Error: {e}"