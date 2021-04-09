import os
import shutil

path = input("Enter the name of your directory")
# This will create a properly organised list of all the file names that is there in the directory.
list_of_files = os.listdir(path)
for x in list_of_files:
    name,ext = os.path.splitext(x)
    ext = ext[1:]
# This forces the next iteration, if it is the directory
    if ext == '':
        continue
# This will move the file to the directory # where the name 'ext' already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path+'/'+x, path+'/'+ext+'/'+x)
# This will create a new directory, # if the directory does not already exist
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path+'/'+x, path+'/'+ext+'/'+x)

