**功能**：
<br>
实现人脸属性的获取，包括性别、年龄、脸型、是否戴眼镜、是否戴口罩。（具体属性数量的增减可参考百度人脸识别api）

**调试示例**:
<br>
先运行：

    roslaunch robocup_get_face get_face.launch

后在终端中输入：

    rosservice call /robo_get_face '[Name]'

其中， [Name] 为期望识别的人的名字。

**调用该服务后的返回值**：
1. FaceAttribute(string), 接收后需要使用json.loads(response.FaceAttribute)将string转换成json对象
1. state(bool)
2. errorcode(int64)
3. errormsg(string)

*Reminder*:
1. ACCESS——TOKEN需要每30日更新一次。最近一次更新于2022.11.7

2. 使用前最好先查找该pkg是否存在：

    rospack find robocup_get_face

如果出现：

    [rospack] Error: package 'robocup_get_face' not found

则到工作空间 source 一下 setup.bash：

    cd robocup-home_services
    source devel/setup.bash
    
另外，调试过程中容易遇到和路径有关的错误，请留意。