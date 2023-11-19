import sys
import time
import random 

import os
import shutil 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="/Users/sooryadharshinishanmugaraj/Downloads/source_folder"
to_dir="/Users/sooryadharshinishanmugaraj/Downloads/destination_folder"

dir_tree={
    "Image_Files":[".gif",".png",".jpg",".jpeg",".jfif",".avif"],
    "PDF_Files":[".pdf"],
    "PPT_Files":[".pptx"],
    "ZIP_Files":[".zip"],
    "CSV_Files":[".csv"],
}

#Blue print/ mould(predefined class)
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        #check the extension(split the file name and ext)
        name,extension=os.path.splitext(event.src_path)
        #put the program to sleep 
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name

                if os.path.exists(path2):
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()

