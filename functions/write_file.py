import os

def write_file(working_directory, file_path, content):
    abs_wd = os.path.abspath(working_directory)
    target_fp = os.path.abspath(os.path.join(abs_wd, file_path))
    if not target_fp.startswith(abs_wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_fp):
        try:
            os.makedirs(os.path.dirname(target_fp), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_fp) and os.path.isdir(target_fp):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(target_fp, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
