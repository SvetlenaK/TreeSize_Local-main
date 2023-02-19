import logging
import sys
import os
from datetime import datetime
import json
import time

from src import utils_fs
from src import copy_to_gcp

#from . import utils_fs

#print("__INIT__ HELLO")
#__all__ = ["utils_fs"] # if use this => not work IMPORT os ... !!!

sw_break_run = 0
PROJECT_PATH = utils_fs.Path(__file__).absolute().parent.parent
path_log = f'{PROJECT_PATH}\log.log'
print(f'Log File:{path_log}')

''' Create LOGGER '''
logging.basicConfig(filename = path_log, format='%(asctime)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %I:%M:%S', level=logging.INFO)
logging.basicConfig(filename = path_log, format='%(asctime)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %I:%M:%S', level=logging.ERROR)
logging.info('******************* BEGIN _INIT_ *********************')
#logging.warning('And this, too')
#logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def get_param_ini(param_name,file_ini):
    dic_ini=[]
    res_nm = ""
    try:
        with open(file_ini) as f:
            dic_ini = json.loads(f.read())
            try:
                res_nm = dic_ini[param_name]
            except Exception as error:
                logging.error(f'f:get_param_ini({param_name}) PARAM_NOT_FOUND IN FILE {file_ini}..Unexpected {error=}, {type(error)=})')
                res_nm = "ERROR"
    except Exception as error:
        logging.error(f'f:get_param_ini({file_ini}) File not fount or error JSON data ..Unexpected {error=}, {type(error)=}")')
        res_nm = "ERROR"

    return res_nm

#print("HHHH:",os.path.dirname(__file__))
#print("h1:",Path(__file__).absolute().parent.parent)
#print("a1:",os.path.abspath(os.curdir))

FILE_INI = os.path.join(PROJECT_PATH, r"init\init.ini")
LOCAL_COMP_FILENAME_INI = get_param_ini("LOCAL_COMP_FILENAME_INI", FILE_INI)
FOLDER_OUT = get_param_ini("FOLDER_OUT", FILE_INI)
LOCAL_COMP_FILENAME_LASTRUN  = get_param_ini("LOCAL_COMP_FILENAME_LASTRUN", FILE_INI)

## from local computer
COMPUTE_NAME_RUN = get_param_ini("COMPUTER_NAME", LOCAL_COMP_FILENAME_INI)
DISC_DRIVE_NAME = get_param_ini("DISC_DRIVE_NAME", LOCAL_COMP_FILENAME_INI)
FOLDERS_LIST_SRC = get_param_ini("FOLDERS_LIST_SRC", LOCAL_COMP_FILENAME_INI)

if LOCAL_COMP_FILENAME_INI == "ERROR" or FOLDER_OUT == "ERROR" or FILE_INI == "ERROR" or LOCAL_COMP_FILENAME_LASTRUN == "ERROR" or COMPUTE_NAME_RUN == "ERROR" or DISC_DRIVE_NAME == "ERROR" or FOLDERS_LIST_SRC == "ERROR":
    sw_break_run = 1

now = utils_fs.datetime.now()
FORMAT_NOW = "%Y-%m-%d %H:%M:%S"
RUNTIME_NOW = now.strftime("%Y_%m_%d_%H%M%S")
FILENAME_RUNTIME = f"{COMPUTE_NAME_RUN}_{RUNTIME_NOW}_"

LAST_RUN = get_param_ini("LAST_RUN",LOCAL_COMP_FILENAME_LASTRUN)
if LAST_RUN == "FILE_NOT_FOUND":
    LAST_RUN = "1950-01-01 23:59:59"
    utils_fs.write_last_run(LOCAL_COMP_FILENAME_LASTRUN, LAST_RUN)

#print("LAST_RUN=>",LAST_RUN)
logging.info(f'LAST_RUN:{LAST_RUN}')
