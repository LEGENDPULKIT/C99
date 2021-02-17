import os
import shutil

#give the path
path=input("enter the name of the directory to be sorted : ")

list_of_files=os.listdir(path)

#go through each and every file 
for file in list_of_files:
    name,ext=os.path.splitext(file)

    #store the ext
    ext=ext[1:]

    if ext=='':
        continue

    #move the file 
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
