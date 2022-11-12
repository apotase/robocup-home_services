#! /usr/bin/python3
from tkinter import W
import speech_recognition as sr
# from speechbrain.pretrained import EncoderDecoderASR
from seu_speech_recognition.srv import *
import rospy 
from playsound import playsound
import speech_split as split
import speech_recognition.scripts.speech_recognition_api as api
#从系统麦克风拾取音频数据，采样率为 16000
def recognition(req):
    rate=16000
    r = sr.Recognizer()
    print("i get a command  %d" % (req.enable))
    
    with sr.Microphone(sample_rate=rate) as source:
        print('正在获取声音中...')
        r.adjust_for_ambient_noise(source)
        playsound('wav/dong.wav')
        audio = r.listen(source)


    with open("wav/recording.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print('声音获取完成.')
        try:
            word= split.extract_info()
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


def voice_into_word(audio):
    print('start recognition...')
    model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-transformerlm-librispeech",
                                           savedir="pretrained_models/asr-transformer-transformerlm-librispeech",
                                           run_opts={"device":"cuda"})
    word = model.transcribe_file(audio)
    print(word)
    return word

def main():
    rospy.init_node('seu_speech_recognition')
    s = rospy.Service('my_speech_recognition', speech_recognition, recognition)
    print ("Ready to recognize speech")
    rospy.spin()

if __name__ == '__main__':
    main()
