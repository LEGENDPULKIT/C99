import os
import shutil

#get the source and the detination
source=input("Enter Source folder path: ")
destination=input("Enter destination folder path: ")

source=source+'/'
destination=destination+'/'

#get the list of all files inside source folder
list_of_files=os.listdir(source)

for file in list_of_files:
    shutil.copy((source+file),destination)
