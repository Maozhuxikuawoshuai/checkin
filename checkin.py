import requests
import time

url = 'https://glados.rocks/api/user/checkin'
data = {'token': 'glados.network'}
headers = {
'authorization': '65514417340718653465740470278038-1080-1920',
'Content-type': 'application/json;charset=utf-8',
'accept': 'application/json, text/plain, */*',
'cookie': '_ga=GA1.2.708365971.1675044132; _gid=GA1.2.1268817973.1675044132; koa:sess=eyJ1c2VySWQiOjI2NzQ1OCwiX2V4cGlyZSI6MTcwMDk2NjMyNjM3NiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=GOjBA2u8irXWxHqfAr1iHdbZ5hE; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc',
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
