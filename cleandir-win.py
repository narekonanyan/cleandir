# This is a Python script for Windows that groups different file types into folders.
# The script runs in the folder where it is located

import os
import shutil

EXT_AUDIO = ['.wav', '.mp3', '.wma']
EXT_VIDEO = ['.mp4', '.m4a', '.m4v', '.mov', '.avi', '.wmv', '.fiv', '.mkv', '.flv', '.mpeg']
EXT_IMAGES = ['.jpeg', '.jpg', '.png', '.svg', '.gif', '.bmp', '.tiff', '.tif', '.psd', '.ai', '.xcf', '.cdr', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2']
EXT_DOCUMENTS = ['.txt', '.pdf', '.doc', '.docx', '.xlsx', '.csv', '.ppt', '.pptx', '.htm', '.html', '.vsdx', '.accdb']
EXT_SOFTWARE = ['.exe', '.msi', '.dmg', '.iso', '.bin']
EXT_COMPRESSED = ['.zip', '.rar', '.gzip', '.7z', '.tar', '.tg']
EXT_SCRIPTS = ['.bas', '.ps1']

print('DOWNLOADS FOLDER CLEANUP')
print('Current Directory: {}'.format(os.getcwd()))
print

files = os.listdir()

# Create directories if they don't exist
DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Folders', 'Software', 'Compressed', 'Other']
if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))

    print('Directories created successfully.')

# Run main script
for f in files:
    name, extension = os.path.splitext(f)

    if extension in EXT_AUDIO:
        shutil.move(f, './Audio/{}'.format(f))
    elif extension in EXT_VIDEO:
        shutil.move(f, './Video/{}'.format(f))
    elif extension in EXT_IMAGES:
        shutil.move(f, './Images/{}'.format(f))
    elif extension in EXT_DOCUMENTS:
        shutil.move(f, './Documents/{}'.format(f))
    elif extension in EXT_SOFTWARE:
        shutil.move(f, './Software/{}'.format(f))
    elif extension in EXT_COMPRESSED:
        shutil.move(f, './Compressed/{}'.format(f))
    elif extension in EXT_SCRIPTS:
        shutil.move(f, './Scripts/{}'.format(f))
    else:
        if os.path.isdir(name):
            if name not in DIRS:
                shutil.move(f, './Folders/{}'.format(f))
            else:
                if f != 'cleandir.py':
                    shutil.move(f, './Other/{}'.format(f))

print('CLEANUP COMPLETED')