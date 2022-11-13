
# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5WGkSEuy4U6h8E67LDv81b0z&client_secret=nGPGsCepoiW67PReGt6ZSUMQAlG65sC1'
response = requests.get(host)
if response:
    print('hhhhhhhhhhhhh',response.json())
# 2022.11.7 access-token:
# 24.ab1ebcd67df27f169b568e6b17abac53.2592000.1670423879.282335-28299517