
import os
import paramiko # pip3 install paramiko

def send_file(file_path, hostname,port, username, password, remote_path):
    """
    send file to gcp instance
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=port, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(file_path, remote_path)
    sftp.close()
    ssh.close()

#def main():
if __name__ == '__main__':
    """
    main function
    """
    file_nm = 'Svetlana_k_2023_02_12_175618___dir_2.txt'
    file_path = os.path.join(os.getcwd(), "C:/PROJECT_OUT/"+file_nm )
    print(type(file_path))
    hostname = '34.27.16.243'
    #hostname = '35.202.85.169'             # my
    port = 122
    username = 'naya'
    password = 'naya'
    remote_path = "/tmp/pycharm_project_781/kafka/json_files/"+file_nm
    #remote_path = '/home/naya/dataFiles/'+file_nm          # my
    send_file(file_path, hostname, port, username, password, remote_path)
