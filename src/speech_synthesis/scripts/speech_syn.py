#! /usr/bin/python3
# -*- coding:UTF-8 -*-

NAME = 'seu_speech_synthesiss'

# import the AddTwoInts service
from seu_speech_synthesis.srv import *
import rospy 
import time
import sys
import pyttsx3




def speech_to_text(data):
    speech=pyttsx3.init()
    voices=speech.getProperty('voices')
    speech.setProperty('voice',voices[11].id)
    speech.setProperty('rate',150)
    speech.say(data)
    speech.runAndWait()
    

def seu_speech_synthesis_main(req):
    print("i get a command  %s" % (req.word))
    time.sleep(1)
    speech_to_text(req.word)
    state=1
    errorcode=0
    errormsg='success'
    return speech_synthesisResponse(state,errorcode,errormsg)
def seu_speech_synthesis_srv():
    rospy.init_node(NAME)
    s = rospy.Service('/my_speech_synthesis', speech_synthesis, seu_speech_synthesis_main)
    print ("Ready to synthesize speech")
    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    seu_speech_synthesis_srv()
