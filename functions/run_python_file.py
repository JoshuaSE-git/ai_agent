import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_wd, file_path))
    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    commands = ["python3", abs_path]
    if args:
        commands.extend(args)
    try:
        result = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_wd,
        )
        output = []
        if result.stdout:
            output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR:\n{result.stderr}')
        if result.returncode != 0:
            output.append(f"Process executed with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: executing Python file: {e}'