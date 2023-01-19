import os
import shutil

destination = "C:/Users/aleyh/Downloads"
source = "C:/Users/aleyh/Desktop/abc/document files"

list = os.listdir(source)

for i in list:
    name, ext = os.path.splitext(i)
    if ext=="":
        continue
    if ext in   ['.text', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1, path3)

        else: 
            os.makedirs(path2)
            print("moving")
            shutil.move(path1, path3)

