首先打开终端，将该项目clone到本地：

    git clone https://github.com/apotase/robocup-home_services.git

没出意外的话该项目会存放在主目录下。
接下来将该工作空间编译一遍:

    cd robocup-home_services
    catkin_make

编译成功后在该工作空间下接着source一下setup.bash:
    
    source devel/setup.bash

完成后即可开始调用该工作空间下的pkg

P.S.
1. 每个pkg有单独的 README.md 文档可供参考
2. 在使用相应的pkg时要注意.launch里对应执行的.py文件里的路径，需要将  /home/[名字]/...  里的  [名字]  修改为用户的名字（用  ~/... 替代 /home/[名字]/...  会出错）