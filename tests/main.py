# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from pathlib import Path
import os
#import datetime
from datetime import datetime
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getSortedListFiles_Time(dirpath):
    #os.path.getmtime => Date Modified
    paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime,reverse=True)
    return paths

def get_tree_size(path):
    """Return total size of files in given path and subdirs. ( bytes )"""
    total = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            total += get_tree_size(entry.path)
        else:
            total += entry.stat(follow_symlinks=False).st_size
    return total

def get_tree_size_2(path):
    """Return total size of files in path and subdirs. If
    is_dir() or stat() fails, print an error message to stderr
    and assume zero size (for example, file has been deleted).
    """
    total = 0
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if is_dir:
            total += get_tree_size(entry.path)
        else:
            try:
                total += entry.stat(follow_symlinks=False).st_size
            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)
    return total

def get_convertdata(filePath):
    # Convert seconds since epoch to Date only
    modificationTime = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(filePath)))
    print("Last Modified Time : ", modificationTime)

def get_sorted_list_files_time(dirpath):
    #os.path.getmtime => Date Modified
    paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime,reverse=True)
    return paths

def filter_files_bydata(files, difftime, format_time):
    for f in files[:]:  # Note the [:] after "files"
        tLog = os.path.getmtime(f)
        tLog_f = datetime.fromtimestamp(tLog).strftime('%d/%m/%Y')

        #print( "checking ", f, type(tLog))#, datetime.datetime.fromtimestamp(tLog))
        if f.is_file() and  difftime < datetime.strptime(tLog_f,format_time)# '%d/%M/%Y'):
            print("difftime is smaller than tLog", "removing ", f)
            files.remove(f)
    return files

def get_machine_storage():
    result=os.statvfs('/')
    block_size=result.f_frsize
    total_blocks=result.f_blocks
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size=total_blocks*block_size/giga
    free_size=free_blocks*block_size/giga
    print('total_size = %s' % total_size)
    print('free_size = %s' % free_size)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    home = Path.home() ## home directory for current USER
    print(home)
#    prj_absolute = Path(home, "My_Project_1", "MyProject_BOT.zip")
#    print(prj_absolute)

    file_dir_home = "C:/SEVA/home/BigData_Naya_Kurs/BIG_DATA_ENG/13_PYCHARM_BigDATA/PyCharm_PROJECTS/FinalProject_BIGDATA"
    curr_file_dir = Path(file_dir_home,"Example_Dir/")
    print(len(list(curr_file_dir.glob('**/*.txt'))) )
    print(len(list(curr_file_dir.glob('**/*')))) ##count file + dir
    print( get_tree_size(curr_file_dir), 'bytes')
    print(get_tree_size(curr_file_dir)/(10**6), 'MB')

    print('get_tree_size_2 *************')
    print(get_tree_size_2(curr_file_dir) / (10 ** 6), 'MB')

    files = get_sorted_list_files_time(curr_file_dir)
    print("files-------------------------:")
    for x in  files:
        print(x)
    print("del files-------------------------:")
    format_time = '%d/%M/%Y'
    new_list_files = filter_files_bydata(files,  datetime.strptime('01/02/2023', format_time), format_time)
    print("new_list_files-------------------------:")
    for x in new_list_files:
        print(x)

    sys.exit()

    # dirs=directories  --- option 1
    for (root, dirs, file) in os.walk(curr_file_dir):
        print("dir root :",root)
        print("sub dir exist in root :",dirs)
        print("list file:", file)
        print("******")

        #for f in file:
        #    if f:
            #print(f)

    print(" dir scan => option 2 " )
    path = curr_file_dir
    obj = os.scandir(path)
    print("Files and Directories in '% s':" % path)

    fd = lambda x : 'file:' if x else 'folder:'
    for entry in obj:
        #entry.getctime
        if entry.is_dir() or entry.is_file():
            print( fd(entry.is_file()),entry.name)

    sys.exit()


    print(curr_file_dir)
    print("---------------iterdir => print all dir")
    p=Path(file_dir_home)#Path('.')
    for x in  p.iterdir():
        if x.is_dir():
            print(x)

    print("---------------iterdir list")
    lst_x=[x for x in p.iterdir() if x.is_dir()]
    print(list(lst_x))

    print(len(list(p.glob('**/*.py'))) )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
