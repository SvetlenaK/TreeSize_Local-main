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
