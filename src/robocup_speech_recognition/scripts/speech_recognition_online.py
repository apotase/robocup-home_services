#! /usr/bin/python3
from tkinter import W
import speech_recognition as sr
from robocup_speech_recognition.srv import *
import rospy 
from playsound import playsound
import speech_split as split
import speech_recognition_api as api
#从系统麦克风拾取音频数据，采样率为 16000

USR_NAME = 'aokaihua'

def recognition(req):
    rate=16000
    r = sr.Recognizer()
    print("i get a command  %d" % (req.enable))
    
    with sr.Microphone(sample_rate=rate) as source:
        print('正在获取声音中...')
        r.adjust_for_ambient_noise(source)
        playsound('/home/'+USR_NAME+'/robocup-home_services/src/robocup_speech_recognition/scripts/wav/dong.wav')
        audio = r.listen(source)

    recording_path = '/home/'+USR_NAME+'/robocup-home_services/src/robocup_speech_recognition/scripts/wav/recording.wav'
    with open(recording_path, "wb") as f:
        f.write(audio.get_wav_data())
        print('声音获取完成.')
        try:
            # word= split.extract_info(api.recognize_speech(recording_path)) #如果需要处理识别后的语句则调用speech_split
            word = api.recognize_speech(recording_path)
            state=1
            errorcode=0
            errormsg='success'
            print(word)
        except AttributeError:
            word=''
            state=0
            errorcode=1
            errormsg='Failure'
            print(word)
    return speech_recognitionResponse(state,errorcode,word,errormsg)


def main():
    rospy.init_node('seu_speech_recognition')
    s = rospy.Service('robo_speech_recognition', speech_recognition, recognition)
    print ("Ready to recognize speech")
    rospy.spin()

if __name__ == '__main__':
    main()
