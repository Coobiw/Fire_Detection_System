############导入相关的py文件和库##############
import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import predict
import os
import resnet50
import opencv_test as cv_test
root_path=r'D:\qbw2\machine_learning\fire_detection\qbw_work\YOLO_NN\a-yolov1-mine_CPU'
model=resnet50.resnet50()
print('load model...')
model.load_state_dict(torch.load('yolo_fire50.pth'))
model.eval()
imgnames = os.listdir(root_path+r'\data\JPEGImages')
size=448

cold_lou=0.
cold_xu=0.
cold_num=0
cold_lou1=0.
cold_xu1=0.

non_lou=0.
non_xu=0.
non_num=0
non_lou1=0.
non_xu1=0.

warm_lou=0.
warm_xu=0.
warm_num=0
warm_lou1=0.
warm_xu1=0.
for index,image_name in enumerate(imgnames):
    image=cv2.imread(root_path+r'\data\JPEGImages'+'\\'+image_name)
    # print(root_path+r'\data\JPEGImages'+'\\'+image_name)
    # print(image)
    result_yolo = predict.YOLO_test(model,image)
    cvtest = cv_test.opencv_test()
    result_opencv = cvtest.testing(image)
    # result_yolo[0,1,2,3,....]=[(x1, y1), (x2, y2), 'fire', prob]
    # result_opencv[0,1,2,3,....]=[(x, y), (x + w, y + h), 'fire']
    if 'cold' in image_name:
        cold_num+=1

    elif 'non' in image_name:
        non_num+=1

    else:
        warm_num+=1
    if len(result_yolo)!=0:
        if len(result_yolo)>1:
            if 'cold' in image_name:
                cold_xu += len(result_yolo)-1

            elif 'non' in image_name:
                non_xu += len(result_yolo)-1

            else:
                warm_xu+=len(result_yolo)-1
    else:
        if 'cold' in image_name:
            cold_lou += 1

        elif 'non' in image_name:
            non_lou+= 1

        else:
            warm_lou += 1
    if len(result_opencv)!=0:
        if len(result_opencv)>1:
            if 'cold' in image_name:
                cold_xu1 += len(result_yolo)-1

            elif 'non' in image_name:
                non_xu1 += len(result_yolo)-1

            else:
                warm_xu1+=len(result_yolo)-1
    else:
        if 'cold' in image_name:
            cold_lou1 += 1

        elif 'non' in image_name:
            non_lou1 += 1

        else:
            warm_lou1 += 1
xu_yolo =[float(cold_xu/cold_num),float(non_xu/non_num),float(warm_xu/warm_num)]
xu_opencv =[float(cold_xu1/cold_num),float(non_xu1/non_num),float(warm_xu1/warm_num)]
lou_yolo=[float(cold_lou/cold_num),float(non_lou/non_num),float(warm_lou/warm_num)]
lou_opencv=[float(cold_lou1/cold_num),float(non_lou1/non_num),float(warm_lou1/warm_num)]
img_label=['cold_fire','non_fire','warm_fire']
x=list(range(len(img_label)))

total_width,n=1.0,4
width = total_width/n
plt.bar(x, xu_yolo, width=width, label='xujing of yolo',tick_label = img_label,fc = 'pink')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, xu_opencv, width=width, label='xujing of opencv',fc = 'red')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, lou_yolo, width=width, label='loujing of yolo',tick_label = img_label,fc = 'green')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, lou_opencv, width=width, label='loujing of opencv',fc = 'blue')
for x,a1,a2,a3,a4 in zip(x,xu_yolo,xu_opencv,lou_yolo,lou_opencv): # 在柱状图上显示具体数值
    plt.text(x-0.75,a1, '%.3f' % float(a1*100.), ha='center', va= 'bottom',fontsize=8)
    plt.text(x-0.5,a2, '%.3f' % float(a2*100.),ha='center', va= 'bottom',fontsize=8)
    plt.text(x - 0.25, a3, '%.3f' % float(a3 * 100.), ha='center', va='bottom', fontsize=8)
    plt.text(x , a4, '%.3f' % float(a4 * 100.), ha='center', va='bottom', fontsize=8)

plt.legend()
plt.title(r'the rate of false report of two methods in testing set', fontsize=10)
plt.savefig(r'D:\qbw2\machine_learning\fire_detection\false_report_analysis0.5.jpg')
plt.show()