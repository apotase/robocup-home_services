#! /usr/bin/python3

NAME = 'seu_wakeup_snowboy'

from robocup_wakeup_robot.srv import *
import rospy 
import time
import snowboydecoder
import sys
import signal
from std_srvs.srv import SetBool
global interrupted
interrupted = False

USR_NAME = 'aokaihua'
MODEl = '/home/'+USR_NAME+'/receptionist/src/seu_wakeup/scripts/resources/models/snowboy.umdl'

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
    detector = snowboydecoder.HotwordDetector(MODEl, sensitivity=0.8)
    time.sleep(1)
    interrupted = False
    # capture SIGINT signal, e.g., Ctrl+C
    print('Listening... Press Ctrl+C to exit')
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
def wakeuop_srv():
    rospy.init_node(NAME)
    s = rospy.Service('robo_sownboy_wakeup', sownboy_wakeup, wakeup_main)
    print("Ready to be waken up.")
    rospy.spin()

    

if __name__ == "__main__":
    wakeuop_srv()




