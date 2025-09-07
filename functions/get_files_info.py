import os

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)
    path_to_dir = os.path.abspath(path)
    path_to_working_dir = os.path.abspath(working_directory)

 
    if path_to_working_dir not in path_to_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        if directory == ".":
            result = f"Result for current directory:"
        else:
            result = f"Result for '{directory}' directory:"

        try:
            for item in os.listdir(path_to_dir):
                result += f"\n - {item}: file_size={os.path.getsize(os.path.join(path_to_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(path_to_dir, item))}"
            return result
        except Exception as e:
            return f"Error: {e}"
