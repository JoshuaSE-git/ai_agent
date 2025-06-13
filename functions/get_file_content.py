import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f"Error: File not found or is not a regular file: {file_path}"

    try:
        with open(abs_file_path, "r") as file:
            contents = file.read(MAX_CHARS)
            if len(contents) == MAX_CHARS:
                contents += (
                    f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return contents
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read in {MAX_CHARS} characters from the specified file path and return contents, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read file from, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
