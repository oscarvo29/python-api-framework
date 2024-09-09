from pathlib import Path

def checkIfFileNameEndsWithHtml(file_name: str) -> str:
    if file_name.__contains__(".html"):
        return file_name
    else:
        if file_name.__contains__("."):
            return "err: The file have a wrong file extension."
        
        return f"{file_name}.html"


def findHtmlFilePath(html_file_name: str) -> str:
    file_name = checkIfFileNameEndsWithHtml(html_file_name)

    # Define the relative path to your HTML file
    relative_path = Path(f"./html/{file_name}")

    # Resolve the absolute path (to avoid issues with relative paths)
    absolute_path = relative_path.resolve()
    
    if absolute_path.exists():
       return absolute_path
    else:
        return "err: file does not exsist"

def get_html_file(file_name: str) -> str:
    file_path = findHtmlFilePath(file_name)

    if str(file_path)[:3] == "err":
        return file_path

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = "".join(file.readlines())
        return content
    except FileNotFoundError:
            return f"err: the file at {file_path} was not found"
    except Exception as e:
            return f"err: error occured: {e}"
