#import src.utils_fs as utils_fs
#from src import DISC_DRIVE_NAME
#from src import get_param_ini ## use function from __INIT__.py
from src import *

    # result = os.statvfs('C:')
    # block_size = result.f_frsize
    # total_blocks = result.f_blocks
    # free_blocks = result.f_bfree
    # # giga=1024*1024*1024
    # giga=1000*1000*1000
    # total_size = total_blocks*block_size/giga
    # free_size = free_blocks*block_size/giga
    # print('total_size = %s' % total_size)
    # print('free_size = %s' % free_size)
    #

print(dir())
print(os.path.dirname(__file__))

#import os
print("File location using os.getcwd():\n",os.getcwd())
sys.exit()

print(get_param_ini("DISC_DRIVE_NAME",r"..\init\init.ini"))
print(DISC_DRIVE_NAME)
print(utils_fs.test_d())

#---------------------
print(utils_fs.get_machine_storage(DISC_DRIVE_NAME))

print("File location using os.getcwd():",os.getcwd())
print(DISC_DRIVE_NAME)
