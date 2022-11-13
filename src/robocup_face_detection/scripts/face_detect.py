#!/usr/bin/env python3
from __future__ import print_function
import rospy
from tkinter.ttk import Widget
import face_recognition
import cv2
from robocup_face_detection.srv import *
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
# Load the jpg file into a numpy array
import base64
import requests
USR_NAME = 'aokaihua'

detection_image_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_detection/src/detection.jpg'
face_store_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_detection/src/face_store/'
ACCESS_TOKEN = '24.ab1ebcd67df27f169b568e6b17abac53.2592000.1670423879.282335-28299517'

def img_encoding(img_path):
    '''
    图像编码
    '''
    with open(img_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
    return base64_data

def callback(msg):
    rate = rospy.Rate(2)
    bridge = CvBridge()
    cvimg = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
    cv2.imwrite(detection_image_path,cvimg)
    rate.sleep()

def face_detect(PERSON_IMAGE, access_token = ACCESS_TOKEN):
    # first, detect human face
    imageBGR = cv2.imread(detection_image_path)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=" + access_token
    body = {'image':bytes.decode(img_encoding(detection_image_path)),'image_type':"BASE64", 'max_face_num': 2}
    headers = {'content-type': 'application/json'}
    response = (requests.post(request_url, data=body, headers=headers)).json()
    if response['error_code'] != 0:
        print(response)
        return 0
    else:
        face_list = response['result']['face_list']
        for face in face_list:
            location = face['location']
            # dont tend to write an error handler now
            x = int(location['left'])
            y = int(location['top'])
            w = int(location['width'])
            h = int(location['height'])
            # add x position in the pic name
            cv2.imwrite(face_store_path+PERSON_IMAGE, imageBGR[y:y+h, x:x+w])   
        return len(face_list)

def store_face(PERSON_IMAGE):
    image = face_recognition.load_image_file(detection_image_path)
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) == 0:
        return 0
    else:
        biggest_face = 3000 # remain to be confirmed
        for face_location in face_locations:
            # Pick the biggest human face and place it into face store
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            height = bottom - top
            width = right - left
            area = width * height
            if area > biggest_face: 
                biggest_face = area
                face_image = image[top:bottom, left:right]
        store_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_face_detection/src/face_store/' + PERSON_IMAGE
        print(store_path)
        cv2.imwrite(store_path, face_image)
        return 1

def face_detection_main(req):
    PERSON_IMAGE = req.name + '.jpg'
    face_num = store_face(PERSON_IMAGE)
    if face_num != 0:
        state=1
        errorcode=0
        errormsg='success'
    else:
        state=0
        errorcode=1
        errormsg='there is no people'
    return face_detectionResponse(state,errorcode,req.name,errormsg)

def face_detection_srv():
    rospy.init_node('face_detection_server')
    # sub = rospy.Subscriber('/kinect2_down/hd/image_color',Image,callback)
    s = rospy.Service('robo_face_detection', face_detection, face_detection_main)
    print("Ready to detect faces.")
    rospy.spin()
 

if __name__ == '__main__':
    face_detection_srv()
    # face_detect('Jack.jpg')