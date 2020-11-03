import requests
import os
from flask import Flask
import socket


#requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=server'+'&desp=ip%0D%0A%0D%0A%0D%0A'+str(a))
requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=done'+'&desp='+str(socket.gethostbyname(socket.gethostname()))
os.system('python -m http.server')
requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=done'+'&desp=ip%0D%0A%0D%0A%0D%0Aflask')
