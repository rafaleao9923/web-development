import os

def get_folder_structure(folder_path):
    structure = {}
    for root, dirs, files in os.walk(folder_path):
        relative_path = os.path.relpath(root, folder_path)
        if relative_path == ".":
            relative_path = ""
        structure[relative_path] = {"folders": dirs, "files": files}
    return structure


if __name__ == "__main__":
    folder_path = "/home/hung/Public/leao/web-development/books/fastapi-build-full-stack-projects"
    structure = get_folder_structure(folder_path)
    print(structure)