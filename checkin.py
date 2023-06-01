import requests
import time

url = 'https://glados.rocks/api/user/checkin'
data = {'token': 'glados.network'}
headers = {
'authorization': '22411569344488265160294967890822-1080-1920',
'Content-type': 'application/json;charset=utf-8',
'accept': 'application/json, text/plain, */*',
'cookie': 'koa:sess=eyJ1c2VySWQiOjI1MDk2MywiX2V4cGlyZSI6MTcwODM5NjUyMjc4MiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=2FUH_9BtRbEmy_PGSbt1QyPFCjE; _ga=GA1.2.422419851.1682476472; _gid=GA1.2.2008597826.1685604062; _gat_gtag_UA_104464600_2=1; _ga_CZFVKMNT9J=GS1.1.1685604060.6.1.1685604065.0.0.0',
'origin': 'https://glados.rocks'
}

response = requests.post(url, json=data, headers=headers)

# 获取当前时间
current_time = int(time.time())
# 转换为localtime
localtime = time.localtime(current_time)
# 利用strftime()函数重新格式化时间
dt = time.strftime('%Y:%m:%d %H:%M:%S', localtime)
print(dt) # 返回当前时间：2021:09:09 19:17:29

print(response.json())

####
