# Use Baidu api to identify face charecteristics
# encoding:utf-8
import requests
import base64
from robocup_get_face.srv import *
import json
import rospy

USR_NAME = 'aokaihua'
face_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_detection/src/detection.jpg'

def img_encoding(img_path):
    '''
    图像编码
    '''
    with open(img_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
    return base64_data
'''
人脸检测与属性分析
'''

def get_face_main(req, img_path = face_path, access_token='24.ab1ebcd67df27f169b568e6b17abac53.2592000.1670423879.282335-28299517'):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=" + access_token
    body = '"{\"image\": \"' + bytes.decode(img_encoding(img_path)) + '\",\"image_type\": \"BASE64\",\"max_face_num\" : 2, \"face_field\":\"gender,faceshape,age,glassses,mask\"}"'
    body = body.strip('"')
    body = bytes(body, 'utf-8')
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=body, headers=headers)
    if response:
        print ('RESULT:',response.json()['result']['face_list'][0])
        face_attribute = json.dumps(response.json()['result']['face_list'][0])
        state=1
        errorcode=0
        errormsg='success'
    else:
        face_attribute = 'None'
        state=0
        errorcode=1
        errormsg='cannot get face attributes'
    return get_faceResponse(face_attribute,state,errorcode,errormsg)

def get_face_srv():
    rospy.init_node('face_detection_server')
    s = rospy.Service('robo_get_face', get_face, get_face_main)
    print("Ready to get face attributes.")
    rospy.spin()

if __name__ == '__main__':
    get_face_srv()