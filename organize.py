from importlib.resources import path
import os
import shutil

from_dir="/Users/sooryadharshinishanmugaraj/Downloads/source_folder"
to_dir="/Users/sooryadharshinishanmugaraj/Downloads/destination_folder"

#list the files inside the folder
list_of_files=os.listdir(from_dir)
print(list_of_files)

#step 1- seperate the file name and extension for all files
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    
    #Step2 - checking if it is an image file 
    if extension=="":
        continue
    if extension in[".gif",".png",".jpg",".jpeg",".jfif",".avif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"Image_Files"
        path3=to_dir+"/"+"Image_Files"+"/"+file_name
        
       #step3 - check if the folder exsists and move the file 
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    
    if extension in[".pdf"]:
        path1=from_dir+"/"+file_name #"/Users/sooryadharshinishanmugaraj/Downloads/source_folder/abc.pdf"
        path2=to_dir+"/"+"PDF_Files" #"/Users/sooryadharshinishanmugaraj/Downloads/destination_folder/PDF_Files"
        path3=to_dir+"/"+"PDF_Files"+"/"+file_name #"/Users/sooryadharshinishanmugaraj/Downloads/destination_folder/PDF_Files/abc.pdf"
        
       #step3 - check if the folder exsists and move the file 
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            
        
        


