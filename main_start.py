import logging
''' TEST 2'''
from src import *
start_time = time.time()

if sw_break_run == 1:
    logging.error(f'EXIT AFTER ERROR ...')
    print("EXIT AFTER ERROR ...")
    sys.exit()

# get disc info in json format
d_info = utils_fs.disc_info(DISC_DRIVE_NAME,COMPUTE_NAME_RUN,now.strftime("%Y-%m-%d %H:%M:%S"))
file_json = json.dumps(d_info.__dict__)
print(file_json)

# write disc info to FOLDER_OUT
f_name =f'{FILENAME_RUNTIME}__INFO.txt'
res = utils_fs.write_file(FOLDER_OUT,f_name,file_json)
print(res)

# print(LAST_RUN)
# print(datetime.strptime('1950-01-01 23:59:00', '%Y-%m-%d %H:%M:%S'))
# print(datetime.strptime(LAST_RUN, FORMAT_NOW))

# for dir_name in FOLDERS_LIST_SRC.split(","):
#     files_all = utils_fs.get_sorted_list_files_time(dir_name)
#     files = utils_fs.filter_files_bydata(files_all,LAST_RUN,FORMAT_NOW )
#     print(" ==>", files)

i = 0
folders_info = utils_fs.FoldersInfo(COMPUTE_NAME_RUN, LAST_RUN, now.strftime(FORMAT_NOW))
for dir_name in FOLDERS_LIST_SRC.split(","):
    #print("dir_name:",dir_name)
    i += 1
    f_name = f'{FILENAME_RUNTIME}__dir_{i}.txt'
    folders_info.add_path(dir_name, f_name)

    dic_w = utils_fs.Directory(dir_name)
    files = dic_w.get_file_data_all(LAST_RUN,FORMAT_NOW )
    logging.info(f'{dic_w.count_files} of {dic_w.count_all_files}')

    file_json = json.dumps(files)
    res = utils_fs.write_file(FOLDER_OUT, f_name, file_json)
    logging.info(f'List Files in Folder {FOLDER_OUT}/{f_name}')
    #print(file_json)

## Folders Global Information
file_json = json.dumps(folders_info.folders_info)
#print(file_json)
f_name =f'{FILENAME_RUNTIME}__F_INFO.txt'
res = utils_fs.write_file(FOLDER_OUT,f_name,file_json)
logging.info(f'Folders Global Info : {FOLDER_OUT}/{f_name}')

## לשמור \ לעדכן LAST_RUN + לבדוק מחיקה לאחר שידור ....

# dic_w = utils_fs.Directory("C:/_TEMP/a")
# files = dic_w.get_file_data_all(LAST_RUN,FORMAT_NOW )
# print(" ==>", files)

end_time = time.time()
print(f"END:{end_time - start_time}")
logging.info(f'******************* END (seconds {end_time - start_time}) *********************')
sys.exit()

#print("dir=>",dir())
#a=d_info.print_info()




