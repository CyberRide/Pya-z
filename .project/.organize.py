import os
import shutil
import platform
import os
if platform.system() == "Windows":
    os.chdir("C:\downloads")
    files = os.listdir()
    extenstions={
        "images": [".jpg", ".png", ".jpeg", ".gif"],
        "videos": [".mp4", ".mkv"],
        "musics": [".mp3", ".wav"],
        "zip": [".zip", ".tgz", ".rar", ".tar"],
        "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
        "setup": [".msi", ".exe"],
        "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
        "design": [".xd", ".psd"]
    }
    def sorting(file):
        keys = list(extentions.keys())
        for key in keys:
            for ext in extentions[key]:
                # print(ext)
                if file.endswith(ext):
                    return key
        for file in files:
             dist = sorting(file)
             if dist:
                try:
                    shutil.move(file, "download-sorting/" + dist)
                except:
                    print(file + " is already exist")
                else:
                    try:
                        shutil.move(file, "download-sorting/others")
                    except:
                        print(file + " is already exist")
    
elif platform.system() == "Linux" or platform.system() == "Linux2" or platform.system() == "Darwin":
    from pathlib import Path
    download = str(os.path.join(Path.home(), "Downloads"))
    os.chdir(download)
    files = os.listdir()
    extenstions={
        "images": [".jpg", ".png", ".jpeg", ".gif"],
        "videos": [".mp4", ".mkv"],
        "musics": [".mp3", ".wav"],
        "zip": [".zip", ".tgz", ".rar", ".tar"],
        "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
        "setup": [".msi", ".exe"],
        "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
        "design": [".xd", ".psd"]
    }
    def sorting(file):
        keys = list(extentions.keys())
        for key in keys:
            for ext in extentions[key]:
                # print(ext)
                if file.endswith(ext):
                    return key
        for file in files:
             dist = sorting(file)
             if dist:
                try:
                    shutil.move(file, "../download-sorting/" + dist)
                except:
                    print(file + " is already exist")
                else:
                    try:
                        shutil.move(file, "../download-sorting/others")
                    except:
                        print(file + " is already exist")
else:
    print("Os not supported!")



