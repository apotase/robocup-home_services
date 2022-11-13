**功能**：
使用百度在线语音识别 api ，识别语言为英语（若要修改中文则将 speech_recognition_api.py 的 DEV_PID = 1737 修改为1537）

使用前需要下载 SpeechRecognition 库：    
    pip install SpeechRecognition

**调试示例**:
先运行：
    roslaunch robocup_speech_recognition speech_recognition.launch
后在终端中输入：
    rosservice call /robo_speech_recognition True

**调用该服务后的返回值**：
1. state(bool)
2. errorcode(int64)
3. word(string), 代表识别出的字句
4. errormsg(string)

*Reminder*:
使用前最好先查找该pkg是否存在：

    rospack find robocup_speech_synthesis

如果出现：

    [rospack] Error: package 'robocup_speech_synthesis' not found

则到工作空间 source 一下 setup.bash：

    cd robocup-home_services
    source devel/setup.bash

另外，调试过程中容易遇到和路径有关的错误，请留意。