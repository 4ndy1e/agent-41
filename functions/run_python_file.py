import os 
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    working_directory_abs_path = os.path.abspath(working_directory)
    full_abs_path = os.path.abspath(full_path)
    
    if not full_abs_path.startswith(working_directory_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(args=["uv", "run", full_path] + args, capture_output=True, timeout=30)
        
        result = f"STDOUT: {completed_process.stdout} \nSTDERR: {completed_process.stderr}\n"
        
        if completed_process.returncode != 0:
            result += f"Process exited with code {completed_process.returncode}"
        else:
            result += f"No output produced."
        
        return result
        
    except Exception as e:
        return f"Error: executing Python file: {e}"