import os
import shutil
from datetime import datetime

LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

today = datetime.today().date() 

today = today.strftime("%m%d%Y")

drive = "C:"

# C:\Users\khani\Downloads
folder_path = "/Users/khani/Downloads/"

c_path = os.path.join(drive, folder_path)

archive_folder = f"downloads_archive_{today}"

if not os.path.exists(c_path + archive_folder):
    os.mkdir(c_path + archive_folder)

# Need a Dictionary to match folder with file extension
dirs_map = {
    "Android Files" : ".apk",
    "Disk Images Files" : ".iso",
    "MP3 Files" : ".mp3",
    "Word Files": ".docx",
    "PDF Files": ".pdf",
    "PPT Files": ".pptx",
    "Text Files": ".txt",
    "JSON Files": ".json",
    "Software": [".exe", ".msi"],
    "Zip Files": [".zip", ".rar", ".tgz", ".gz"],
    "Excel Files": ".xlsx",
    "CSV Files": ".csv",
    "Video Files": ".mp4",
    "Image Files": [".jpeg", ".png", ".jpg"],
    "PowerBI Files": ".pbix",
    "SQL Files": [".SQL", ".sql"],
    "Log Files": ".log",
    "Other Files": ".*"
}

files_list = []

def create_folders():
    '''
    Create folders for respective files types.
    '''
    for dir in dirs_map.keys():
        if os.path.exists(c_path + dir) != True:
            os.mkdir(c_path + dir)


def files_sorter(dir, extn):
    '''
    Moves files to respective folders.
    '''
    # print(dir, extn)
    for file in files_list:
        file = str(file).lower()
        if os.path.isfile(c_path + file):
            file_extn = "." +  file.split(".")[-1]
            if file_extn == extn or file_extn in extn:
                print(f"Copying file.. {file}")
                shutil.copy(c_path + file, c_path + dir)
                shutil.move(c_path + file, c_path + archive_folder)


def folders_sorter():
    '''
    Sorts folders
    '''
    pre_folders = dirs_map.keys() 
    folders = os.listdir(os.path.join(drive, folder_path))
    for folder in folders:
        if folder not in pre_folders:
            shutil.move(c_path + folder, c_path + archive_folder)


if __name__ == "__main__":
    print("Create Folders --")
    create_folders()
    print(f"Created Folders in {c_path}")
    print("Copy and Archive -- ")
    for dir, extn in dirs_map.items():
        files_list.extend(os.listdir(os.path.join(drive, folder_path)))
        files_sorter(dir, extn)
        files_list.clear()
    folders_sorter()
    print(end=LINE_CLEAR)
    print("******************************* Done Sorting Files and Folders *********************************************")
