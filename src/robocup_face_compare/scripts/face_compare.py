#!/usr/bin/env python3
from __future__ import print_function
from robocup_face_compare.srv import *
import rospy
from tkinter.ttk import Widget
from PIL import Image
import face_recognition
import cv2
import shutil,os
import numpy as np
import json
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import base64
import requests
import time

# 需要修改本机用户名
USR_NAME = 'aokaihua'

compare_image_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_compare/src/compare.jpg'
face_store_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_detection/src/face_store/'
compare_store_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_compare/src/compare_store/'
cut_store_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_compare/src/cut_store/'
ACCESS_TOKEN = '24.ab1ebcd67df27f169b568e6b17abac53.2592000.1670423879.282335-28299517'

def img_encoding(img_path):
    '''
    图像编码
    '''
    with open(img_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
    return base64_data

# def rename():
#     for compare_face in os.listdir(compare_store_path):
#         position = compare_face[:3]
#         for cut_face in os.listdir(cut_store_path):
#             if cut_face[:3] != position:
#                 shutil.copy(cut_store_path+cut_face, compare_store_path+cut_face[:3]+'Host.jpg')

def callback(msg):
    rate = rospy.Rate(2)
    bridge = CvBridge()
    cvimg = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
    cv2.imwrite(compare_image_path,cvimg)
    rate.sleep()

def face_detect(access_token = ACCESS_TOKEN):
    # first, detect human face
    imageBGR = cv2.imread(compare_image_path)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=" + access_token
    body = {'image':bytes.decode(img_encoding(compare_image_path)),'image_type':"BASE64", 'max_face_num': 2}
    headers = {'content-type': 'application/json'}
    response = (requests.post(request_url, data=body, headers=headers)).json()
    face_list = response['result']['face_list']
    for index, face in enumerate(face_list):
        location = face['location']
        # dont tend to write an error handler now
        x = int(location['left'])
        y = int(location['top'])
        w = int(location['width'])
        h = int(location['height'])
        # add x position in the pic name
        cv2.imwrite(cut_store_path+str(x)+'_'+str(index)+'.jpg', imageBGR[y:y+h, x:x+w])   

def face_comparison(access_token = ACCESS_TOKEN):
    for face_store in os.listdir(face_store_path):
        for cut_face in os.listdir(cut_store_path):
            image = cv2.imread(cut_store_path+cut_face)
            request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="+ access_token
            body = []
            body.append({'image':bytes.decode(img_encoding(cut_store_path+cut_face)), 'image_type':'BASE64'})
            body.append({'image':bytes.decode(img_encoding(face_store_path+face_store)), 'image_type':'BASE64'})
            headers = {'content-type': 'application/json'}
            response = (requests.post(request_url, json=body, headers=headers)).json()
            print('1',response)
            score = response['result']['score']
            time.sleep(0.5)
            if score > 70:
                cv2.imwrite(compare_store_path+cut_face[:3]+face_store, image)
                break


def nameNposition():
    face_detect()
    face_comparison()
    name_position = {}
    for compare_face in os.listdir(compare_store_path):
        name_position.update({compare_face[3:-4]: compare_face[:3]})
    return name_position

    # 需要考虑到识别不出人脸的情况，所以要加异常处理，比如如果出错则重新调用客户端

def face_compare_main(req):
    name_position = nameNposition()
    result = json.dumps(name_position)
    if len(name_position) == 0:
        state=0
        errorcode=1
        errormsg='there is no people'
        name_position = 'NUll'
    else:
        state=1
        errorcode=0
        errormsg='success'
        name_position = result
    return face_compareResponse(state,errorcode,errormsg,name_position)

def face_compare_srv():
    rospy.init_node('face_compare_server')
    # sub = rospy.Subscriber('/kinect2_down/hd/image_color',Image,callback)
    s = rospy.Service('robo_face_compare', face_compare, face_compare_main)
    print("Ready to compare faces.")
    rospy.spin()
 

if __name__ == '__main__':
    face_compare_srv()
