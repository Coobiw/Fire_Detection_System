# Fire_Detection_System
It is a system used to detect the fire object based on cascade-classifier,Yolov1 Network Architecture and their combination.By the way,In order to improve the accuracy,we also use FCN Network.Actually,it is better for you to use Yolov3,v4,v5 to solve this problem.We just want to introduce an idea to enhance the accurary on small object,such as detecting on the segmentation results.


## codes大体介绍
此模块将完成对各模块代码的整体性介绍。

### 主程序
主程序内的main程序即为整个火焰检测系统，具体包括了GUI、使用opencv里的cascade classfier、使用YOLOv1神经网络（包括其backbone，以及进行预测的程序）、二者的combine算法，同时，还有火焰识别系统的作为服务器的socket通信代码。

### FCN代码
里面包含了超参数配置程序、建立dataset程序、FCN网络结构定义、FCN的训练、通过confusion matrix计算各种语义分割指标、以及利用FCN进行预测的程序

其中FCN数据集见压缩文件

### 可视化
里面包含了对opencv、Yolo以及combine算法相关指标的可视化，同时还包含了不同threshold的combine算法的指标测算，从而根据此得到combine算法的较好的阈值，选择的数据集见压缩文件

### 客户端通信
内含客户机的socket通信代码。

## 压缩文件说明
压缩文件为训练FCN所用dataset，内含data与其对应的label（ground truth），label均使用labelme软件手动标注。

