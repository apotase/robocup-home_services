**功能**：
<br>
实现人脸识别（离线），将识别出的人脸放存在人脸库中（该功能只支持识别一张图中的面积最大的人脸

**调试示例**:
<br>
先运行：

    roslaunch robocup_face_detection face_detection.launch

后在终端中输入：

    rosservice call /robo_face_detection '[Name]'

其中， [Name] 是识别出的人的名字

**调用该服务后的返回值**：
1. state(bool)
2. errorcode(int64)
3. name(string), 代表识别出的人脸
4. errormsg(string)

*Reminder*:
1. ACCESS——TOKEN需要每30日更新一次。最近更新于2022.11.12
2. 使用前最好先查找该pkg是否存在：

    rospack find robocup_face_detection

如果出现：

    [rospack] Error: package 'robocup_face_detection' not found

则到工作空间 source 一下 setup.bash：

    cd robocup-home_services
    source devel/setup.bash

另外，调试过程中容易遇到和路径有关的错误，请留意。