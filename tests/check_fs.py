import os
import datetime
import time
import json


import sys

def get_files_after_date(dir_path, date):
    file_list = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if modification_time > date:
                #file_list.append(filename)
                file_list.append(file_path)
    return file_list

def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
    return total_size

def get_inf_file(directory):
    # get a list of all files in the directory
    files = os.listdir(directory)
    print("FOLDER:",files)
    os.path.getsize(directory)

    # loop through the list of files and access their data
    for file in files:
        # specify the file path
        file_path = os.path.join(directory, file)
        print("     FILE:",os.path.isfile(file_path))

        # get the absolute path
        abs_path = os.path.abspath(file_path)
        print("Absolute path:", abs_path)

        # get the base name
        base_name = os.path.basename(file_path)
        print("Base name:", base_name)

        # get the directory name
        dir_name = os.path.dirname(file_path)
        print("Directory name:", dir_name)

        # check if the file exists
        if os.path.exists(file_path):
            print("File exists")
            # check if it's a file
            if os.path.isfile(file_path):
                print("It's a file")
                # get the modification time
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                print("Modification time:", mod_time)

                # get the creation time of the file
                ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                print("Creation datetime:", ctime) #time.ctime(ctime))

                # get the file size
                file_size = os.path.getsize(file_path)
                print("File size:", file_size, "bytes")
            else:
                print("It's not a file")
        else:
            print("File doesn't exist")



#-- ???
def get_dir_size(path):
    return sum(os.path.getsize(os.path.join(path, filename)) for filename in os.listdir(path) if os.path.isfile(os.path.join(path, filename)))

#####################################


def get_inf_file(directory):
    # get a list of all files in the directory
    files = os.listdir(directory)
    print("FOLDER:",files)
    os.path.getsize(directory)

def  get_info(path):
    # loop through the list of files and access their data
    for file in files:
        # specify the file path
        file_path = os.path.join(directory, file)
        print("     FILE:",os.path.isfile(file_path))

        # get the absolute path
        abs_path = os.path.abspath(file_path)
        print("Absolute path:", abs_path)

        # get the base name
        base_name = os.path.basename(file_path)
        print("Base name:", base_name)

        # get the directory name
        dir_name = os.path.dirname(file_path)
        print("Directory name:", dir_name)

        # check if the file exists
        if os.path.exists(file_path):
            print("File exists")
            # check if it's a file
            if os.path.isfile(file_path):
                print("It's a file")
                # get the modification time
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                print("Modification time:", mod_time)

                # get the creation time of the file
                ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                print("Creation datetime:", ctime) #time.ctime(ctime))

                # get the file size
                file_size = os.path.getsize(file_path)
                print("File size:", file_size, "bytes")
            else:
                print("It's not a file")
        else:
            print("File doesn't exist")



class Directory:
    def __init__(self, path):
        self.path = path

    def get_file_data(self):
        files = []
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            if os.path.isfile(file_path):
                file_data = {
                    "filename": filename,
                    "path": file_path,
                    "size": os.path.getsize(file_path),
                }
                files.append(file_data)
        return files

    def get_file_data_all(self):
        files = []
        if os.path.isfile(self.path):
            file_data = {
                "filename": filename,
                "path": file_path,
                "size": os.path.getsize(file_path),
            }
            files.append(file_data)
            #total_size = os.path.getsize(self.path)
        elif os.path.isdir(self.path):
            for dirpath, dirnames, filenames in os.walk(self.path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    #total_size += os.path.getsize(fp)
                    file_data = {
                        "dirpath" : dirpath,
                        "dirnames": dirnames,
                        "filename": f,
                        "path": fp,
                        "size": os.path.getsize(fp),
                    }
                    files.append(file_data)
        return files


# full path / file name/ create date/ modifine date / size KB
dir_path = "c:/_temp/a"

# create an instance of the class
directory = Directory(dir_path)

files = directory.get_file_data_all()
file_json = json.dumps(files)
print(files)

# get the file data
#files = directory.get_file_data()
#print(files)
sys.exit() ## **********************************

#file_json = json.dumps(file.__dict__)
#print("JSON:", file_json)

# print the file data
for file in files:
    print("Filename:", file['filename'])
    print("Path:", file['path'])
    print("Size:", file['size'], "bytes")
    print("")





# convert the class instance to a JSON string
#file_json = json.dumps(file.__dict__)
#print("JSON:", file_json)


get_inf_file(dir_path)
# files = os.listdir(dir_path)
# print(files)
# a=os.path.getsize(dir_path)
# print(a)

sys.exit() ## **********************************

date = datetime.datetime(2022, 1, 1)
files = get_files_after_date(dir_path, date)
print(files)

size = get_size(dir_path)
print("Size:", size, "bytes")

size = get_dir_size(dir_path) ## not true
print("SizeDir:", size, "bytes")


