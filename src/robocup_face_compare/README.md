**功能**：
<br>
实现人脸比对（百度api在线识别），将比对出的人脸放存在  compare store  中, 文件名为人脸的x坐标和人名

**调试示例**:
<br>
先运行：

    roslaunch robocup_face_compare face_compare.launch

后在终端中输入：

    rosservice call /robo_face_compare True


**调用该服务后的返回值**：
1. state(bool)
2. errorcode(int64)
3. errormsg(string)
4. name_position(string), 识别出的人脸名字及x坐标，获取后需要json.loads(response.name_position)来将string转换成json对象

*Reminder*:
1. ACCESS——TOKEN需要每30日更新一次。最近更新于2022.11.12
2. 使用前最好先查找该pkg是否存在：

    rospack find robocup_face_compare

如果出现：

    [rospack] Error: package 'robocup_face_compare' not found

则到工作空间 source 一下 setup.bash：

    cd robocup-home_services
    source devel/setup.bash

另外，调试过程中容易遇到和路径有关的错误，请留意。