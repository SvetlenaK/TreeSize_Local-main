import logging
import os
import sys
import psutil  # pip install psutil
from pathlib import Path
from datetime import datetime

def test_d():
    print("test_d: OK")
    return

def get_tree_size(path):
    """Return total size of files in given path and subdir. ( bytes )"""
    logging.info(f'f:get_tree_size({path})')
    total = 0
    for entry in os.scandir(path):

        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_tree_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size

        except Exception as error:
            #msg_err = f'Error calling stat(): {error} f:{entry.path}'
            logging.error(f'f:get_tree_size({path}) ..Unexpected {error=}, {type(error)=})')

    return total

def get_machine_storage(path_disc): ## not use
    logging.info(f'f:get_machine_storage({path_disc})')
    result = os.statvfs(path_disc)
    block_size = result.f_frsize
    total_blocks = result.f_blocks
    free_blocks = result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size = total_blocks*block_size/giga
    free_size = free_blocks*block_size/giga
    print('total_size = %s' % total_size)
    print('free_size = %s' % free_size)
    return

class disc_info:
    def __init__(self,disk_name, comp_name, now_str):
        logging.info(f'f:disc_info({disk_name},{comp_name})')
        self.disc_name = disk_name
        self.now = now_str
        self.computer_name = comp_name
        hdd = psutil.disk_usage(self.disc_name)
        #self.hdd= hdd
        self.disc_total = hdd.total # in BYTES
        self.disc_used = hdd.used
        self.disc_free = hdd.free
        self.disc_type = "WIN"

    def print_info(self):
        print(f'''    
            TOTAL DISK SPACE : {round(self.disc_total / (1024.0 ** 3), 4)} GiB
            USED DISK SPACE  : {round(self.disc_used / (1024.0 ** 3), 4)} GiB
            FREE DISK SPACE  : {round(self.disc_free / (1024.0 ** 3), 4)} GiB
            ''')

def write_file(folder_name,file_name, data):
    """ Write data to exists file """
    logging.info(f'f:write_file({folder_name},{file_name}..)')
    if os.path.exists(folder_name):
        file = open(f'{folder_name}{file_name}', 'w')
        file.write(data)
        file.close()
        return "OK"
    else:
        return "FOLDER_NOT_EXIST"

def write_last_run(file_name, data):
    """ Create / recreate log file and write data """
    logging.info(f'f:write_last_run({file_name}..)')
    data_str = '{ "LAST_RUN":"'+str(data)+'"}'
    file = open(f'{file_name}', 'w')
    file.write(data_str)
    file.close()
    return "OK"

def get_file_data(file_name):
    """ Read file """
    logging.info(f'f:get_file_data({file_name})')
    if os.path.isfile(file_name):
        file = open(f'{file_name}', 'r')
        res = file.read()
        file.close()
        return res
    else:
        return "FILE_NOT_FOUND"


def get_sorted_list_files_time(dirpath):
    logging.info(f'f:get_sorted_list_files_time({dirpath})')
    #os.path.getmtime => Date Modified
    files = sorted(Path(dirpath).iterdir(), key=os.path.getmtime,reverse=True)
    return files

def filter_files_bydata(files, difftime_str, format_time):
    logging.info(f'f:filter_files_bydata(..)')

    #FORMAT_NOW = "%Y-%m-%d %H:%M:%S"
    difftime = datetime.strptime(difftime_str,format_time)

    for f in files[:]:  # Note the [:] after "files"
        tLog = os.path.getmtime(f)
        tLog_f = datetime.fromtimestamp(tLog).strftime(format_time)

        #print( "checking ", f, type(tLog))#, datetime.datetime.fromtimestamp(tLog))
        if f.is_file() and  difftime > datetime.strptime(tLog_f,format_time): # '%d/%M/%Y'):
            print("Date modified is smaller than LAST_RUN ", "removing ", f , datetime.strptime(tLog_f,format_time))
            files.remove(f)
    return files

#-----------------------
class FoldersInfo:
    def __init__(self, computer_name,chk_from_date, now_run):
        self.folders_info = []
        self.computer_name = computer_name
        self.chk_from_date = chk_from_date
        self.now_run = now_run

    def add_path(self, path, file_name_list):
        f = {
            "computer_name": self.computer_name,
            "folder_name": path,
            "folder_size": get_tree_size(path),
            "fnm_with_last_change": file_name_list,
            "chk_from_date": self.chk_from_date,
            "now_run": self.now_run
        }
        self.folders_info.append(f)

class Directory:
    def __init__(self, path):
        logging.info(f'f:Directory({path})')
        self.path = path
        self.count_files = 0
        self.count_all_files = 0

    def get_file_data(self):
        ''' Data about files in current directory .. not use'''
        files = []
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            if os.path.isfile(file_path):
                file_data = {
                    "filename": filename,
                    "path": file_path,
                    "size": os.path.getsize(file_path),
                    "date_modified": os.path.getmtime(file_path),
                    "date_created": os.path.getctime(file_path)
                }
                files.append(file_data)
        return files

    def get_file_data_all(self, difftime_str, format_time):
        ''' Data about all files in all sub directories '''
        logging.info(f'f:Directory.get_file_data_all({difftime_str},{format_time})')
        difftime = datetime.strptime(difftime_str, format_time)
        self.count_files = 0
        self.count_all_files = 0
        files = []
        # if os.path.isfile(self.path):
        if os.path.isdir(self.path):
            for dirpath, dirnames, filenames in os.walk(self.path):

                for f in filenames:
                    self.count_all_files += 1
                    fp = os.path.join(dirpath, f)
                    d_mod = datetime.fromtimestamp(os.path.getmtime(fp)).strftime(format_time)
                    if difftime < datetime.strptime(d_mod, format_time):
                        self.count_files += 1
                        d_cr = datetime.fromtimestamp(os.path.getctime(fp)).strftime(format_time)
                        #total_size += os.path.getsize(fp)
                        file_data = {
                            "dirpath": dirpath,
                            "filename": f,
                            "size": os.path.getsize(fp),
                            "date_modified": d_mod,
                            "date_created": d_cr
                        }
                        files.append(file_data)
            logging.info(f'f:Directory.get_file_data_all - return(len files:{len(files)})')
            return files

