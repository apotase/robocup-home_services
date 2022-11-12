#!/usr/bin/env python

NAME = 'seu_wakeup_snowboy'

# import the AddTwoInts service
from seu_wakeup.srv import *
import rospy 
import time
import sys
# print(sys.path)
# sys.path.append('/home/aokaihua/catkin_ws/src/snowboy/examples/Python3')
import snowboydecoder
import sys
import signal
from std_srvs.srv import SetBool
global interrupted
interrupted = False


def CloseInfo():
    rospy.loginfo('WakeUp node is closed')


def Close():
    rospy.on_shutdown(CloseInfo)


#def signal_handler(signal, frame):
    #global interrupted
    #interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def detected():
    global interrupted
    print("detected is true")
    interrupted = True

def re_detected():
    global interrupted
    interrupted = False
    
def wakeup_main(req):
    print("i get a command  %d" % (req.enable))
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.8)
    time.sleep(1)
    interrupted = False
    # capture SIGINT signal, e.g., Ctrl+C
    print('Listening... Press Ctrl+C to exit')
    # main loop
    #detector = snowboydecoder.HotwordDetector(model, sensitivity=0.8)
    #print(interrupted)
    detector.start(detected_callback=detected,
		re_detected_callback=re_detected,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)
    # print(interrupted)
    detector.terminate()
    print ('wakeup_snowboy_srv finish')
    state=1
    errorcode=0
    errormsg='success'
    return sownboy_wakeupResponse(state,errorcode,errormsg)

print(1)
model = '/home/aokaihua/receptionist/src/seu_wakeup/scripts/resources/models/snowboy.umdl'
print(2)
rospy.init_node(NAME)
print(3)
#signal.signal(signal.SIGINT, signal_handler)
s = rospy.Service('my_sownboy_wakeup', sownboy_wakeup, wakeup_main)
print(4)

# spin() keeps Python from exiting until node is shutdown
rospy.spin()

    






