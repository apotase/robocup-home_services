**功能**：
实现语音合成

**调试示例**:
先运行：

    roslaunch robocup_speech_synthesis speech_synthesis.launch

后在终端中输入：

    rosservice call /robo_speech_synthesis '[Sentence]'

其中，[Sentence]为期望语音合成的语句。

**调用该服务后的返回值**：
1. state(bool)
2. errorcode(int64)
3. errormsg(string)

*Reminder*:
使用前最好先查找该pkg是否存在：

    rospack find robocup_speech_synthesis

如果出现：

    [rospack] Error: package 'robocup_speech_synthesis' not found

则到工作空间 source 一下 setup.bash：

    cd robocup-home_services
    source devel/setup.bash
    
另外，调试过程中容易遇到和路径有关的错误，请留意。