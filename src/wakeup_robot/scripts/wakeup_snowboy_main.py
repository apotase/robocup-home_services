#! /usr/bin/python3
import snowboydecoder
import sys
import signal
import rospy
from std_srvs.srv import SetBool

interrupted = False


def CloseInfo():
    rospy.loginfo('WakeUp node is closed')


def Close():
    rospy.on_shutdown(CloseInfo)


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def detected():
    global interrupted
    interrupted = True


def snowboyMain():
    global interrupted
    model = 'resources/models/seurat.pmdl'

    # capture SIGINT signal, e.g., Ctrl+C
    #signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=detected,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

def wakeup_snowboy_srv(req):
    global interrupted
    tts_data = str(req.data)
    print ('wakeup_snowboy_srv gets ' + tts_data)
    interrupted = False
    snowboyMain()
    interrupted = False
    print ('wakeup_snowboy_srv finish')
    return True

def main():
    rospy.init_node('wakeup_snowboy')
    rospy.Service('wakeup_snowboy_srv', SetBool, wakeup_snowboy_srv)
    rospy.spin()


if __name__ == '__main__':
    main()
