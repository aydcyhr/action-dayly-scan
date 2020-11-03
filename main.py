import requests
import os
from requests.exceptions import Timeout, ConnectionError
import socket
#局域网ip
rsp = requests.get("http://www.baidu.com", stream=True)
ip_baidu = rsp.raw._connection.sock.getpeername()[0]
ip_local = rsp.raw._connection.sock.getsockname()[0]
requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=done'+'&desp='+ip_local+'%0D%0A%0D%0A%0D%0A'+ip_baidu)

#公网ip
urls = ["http://whatismyip.akamai.com/", "http://wgetip.com/"]
def _verify_address(addr):
	try:
		socket.inet_aton(addr)
		return True
	except (socket.error, UnicodeEncodeError, TypeError):
		return False

def _fetch_data(urls):
	for url in urls:
		try:
			req = requests.get(url, timeout=5)
			if req.status_code == 200:
				data = req.text.strip()
				if data is None or not _verify_address(data):
					continue
				else:
					return data
			else:
				raise ConnectionError
		except (Timeout, ConnectionError):
			print ('Could not fetch public ip from %s', url)
	return None

requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=done'+'&desp='+_fetch_data(urls)+'%0D%0A%0D%0A%0D%0A'+ip_baidu)
