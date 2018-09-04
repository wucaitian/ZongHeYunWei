from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
from StatusCheck.LoginSer.logins import SshLogin

def checkSer(request):
    return render(request,'checkSer.html')

def checkServer(request):
    import os
    OneServerStatus_html = os.getcwd()+os.sep+'templates'+os.sep+'OneServerStatus.html'
    ip = request.POST.get('ip')
    port = request.POST.get('post')
    user = request.POST.get('user')
    commands = request.POST.get('Command')
    results = {}

    get_ssh_login = SshLogin(agrv_ip=ip,agrv_port=port,agrv_user=user,agrv_command=commands) #类实例化

    result = get_ssh_login.ssh_run()
    results[ip] = result
    if not os.path.exists(OneServerStatus_html):
        with open(OneServerStatus_html,'w') as f:
            f.write(result)

    return render(request,'OneServerStatus.html')

def OneClickCheck(request):
    import os
    port = 22
    user = 'root'
    results = {}
    result = []
    #批量执行远程服务器运行状态
    for ips in open(os.getcwd()+"/StatusCheck/server_ip"):
        for commands in open(os.getcwd()+"/StatusCheck/query_commands"):
            get_ssh_login = SshLogin(agrv_ip=ips,agrv_port=port,agrv_user=user,agrv_command=commands)
            each_result = get_ssh_login.ssh_run()
            each_result_str = "".join(each_result) #列表转为字符串
            result.append(each_result_str)

        results[ips] = result
        result = []

    #for key in results:
        #print(key,results[key])
    return render(request,'serverStatus.html',locals())
