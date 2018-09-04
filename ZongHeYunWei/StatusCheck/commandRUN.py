from LoginSer.logins import SshLogin
ip = '172.16.3.43'
port = 22
user = 'root'
command = 'ls /tmp | grep or'

get_ssh_login = SshLogin(agrv_ip=ip,agrv_port=port,agrv_user=user) #类实例化
get_ssh_client,get_ssh_session = get_ssh_login.ssh_login() #获取ssh客户端和ssh会话状态


def ssh_command_run(commands):
    try:
        if get_ssh_session.active:
            get_ssh_session.exec_command(commands+'\n')
            stdin,stdout,stderr = get_ssh_client.exec_command(commands+'\n')
            return stdout.readlines()
    except BaseException as err:
        print(err)

results = ssh_command_run(commands=command)
for result in results:
    print(result,end='')
