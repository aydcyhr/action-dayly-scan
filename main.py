import requests


rsp = requests.get("http://www.baidu.com", stream=True)

ip_baidu = rsp.raw._connection.sock.getpeername()[0]
ip_local = rsp.raw._connection.sock.getsockname()[0]
requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=done'+'&desp='+ip_local+'%0D%0A%0D%0A%0D%0A'+ip_baidu)
