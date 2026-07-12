import os
import shutil

from langchain_core.tools import tool

from config import Config


@tool
def create_project(project_name: str) -> str:
    """
    Create a new project folder.
    """

    project_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name
    )

    os.makedirs(project_path, exist_ok=True)

    return project_path


@tool
def create_file(
    project_name: str,
    file_name: str,
    content: str
) -> str:
    """
    Create a file inside the project folder.
    """

    project_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name
    )

    os.makedirs(project_path, exist_ok=True)

    file_path = os.path.join(
        project_path,
        file_name
    )

    # Create parent directories if they don't exist
    parent_dir = os.path.dirname(file_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Created {file_path}"


@tool
def read_file(
    project_name: str,
    file_name: str
) -> str:
    """
    Read file contents.
    """

    file_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name,
        file_name
    )

    if not os.path.exists(file_path):
        return "File not found."

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


@tool
def write_file(
    project_name: str,
    file_name: str,
    content: str
) -> str:
    """
    Overwrite an existing file.
    """

    file_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name,
        file_name
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return "File Updated."


@tool
def delete_file(
    project_name: str,
    file_name: str
) -> str:
    """
    Delete a file.
    """

    file_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name,
        file_name
    )

    if os.path.exists(file_path):
        os.remove(file_path)
        return "Deleted."

    return "File not found."



@tool
def list_files(project_name: str) -> list:
    """
    List all files inside the project.
    """

    project_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name
    )

    if not os.path.exists(project_path):
        return []

    return os.listdir(project_path)


@tool
def delete_project(project_name: str) -> str:
    """
    Delete entire project folder.
    """

    project_path = os.path.join(
        Config.PROJECTS_DIR,
        project_name
    )

    if os.path.exists(project_path):
        shutil.rmtree(project_path)
        return "Project Deleted."

    return "Project not found."