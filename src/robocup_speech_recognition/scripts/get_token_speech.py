
# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=raihP9ndDevXRYGbt8pC2Cyl&client_secret=W04MGCUUdrKnb0ytz3j7YR74SNiBuGhn'
response = requests.get(host)
if response:
    print('hhhhhhhhhhhhh',response.json())
# 2022.11.12 access-token:
# '24.b8501ac94448ae2a6375ce57ca3fbf35.2592000.1670843838.282335-28387529'