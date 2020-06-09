def get_file_extension(track, lang):
    ext = {
        "java": ".java",
        "java7": ".java",
        "java8": ".java",
        "python": ".py",
        "python3": ".py",
        "python2": ".py",
        "csharp": ".cs",
        "javascript": ".js",
        "c": ".c",
        "cpp14": ".cpp",
        "cpp": ".cpp",
        "sql": ".sql",
        "mysql": ".sql",
        "oracle": ".sql",
        "ruby": ".rb",
        "hashkell": ".hs",
        "bash": "",
        "shell": ""
    }
    if ext.get(lang) is not None:
        return ext.get(lang)
    elif ext.get(track) is not None:
        return ext.get(track)
    else:
        return ""

def setupPath():
    from constants import BASE_DIR, WEBDRIVER_DIR
    from tracks import TRACKS
    from pathlib import Path

    BASE_DIR = Path(BASE_DIR)
    WEBDRIVER_DIR = Path(WEBDRIVER_DIR)
    BASE_DIR.mkdir(exist_ok=True)

    for track in TRACKS:
        (BASE_DIR / track).mkdir(exist_ok=True)
    
    if not WEBDRIVER_DIR.exists():
        print("Please check that {} is present in {}".format(
            WEBDRIVER_DIR.name,
            WEBDRIVER_DIR.resolve())
            )
