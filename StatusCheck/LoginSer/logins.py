import paramiko

class SshLogin:
    private_key_path = '/Users/Chatin/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_path)
    ip = ''
    port = ''
    user = ''
    command = ''
    def __init__(self,agrv_ip,agrv_port,agrv_user,agrv_command):
        self.ip = agrv_ip
        self.port = agrv_port
        self.user = agrv_user
        self.command = agrv_command


    def ssh_run(self):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(self.ip,self.port,self.user,self.key)
            ssh_session = ssh_client.get_transport().open_session()
            if ssh_session.active:
                ssh_session.exec_command(self.command+'\n')
                stdin,stdout,stderr = ssh_client.exec_command(self.command+'\n')
                return stdout.readlines()
        except BaseException as error:
            print(error,self.ip)

if __name__ == '__main__':
    pass
