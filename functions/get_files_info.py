import os

from google.genai import types


def get_files_info(working_directory, directory=None):
    abs_wd = os.path.abspath(working_directory)
    target_dir = abs_wd
    if directory:
        path = os.path.join(working_directory, directory)
        target_dir = os.path.abspath(path)
    if not target_dir.startswith(abs_wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
    if not os.path.isdir(target_dir):
        return f'"{directory} is not a directory.'

    try:
        files_info = []
        for content in os.listdir(target_dir):
            path = os.path.join(target_dir, content)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files_info.append(
                f"- {content}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
