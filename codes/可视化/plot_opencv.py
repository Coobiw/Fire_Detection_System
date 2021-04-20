import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import opencv_test as cv_test
import os
root_path=r'D:\qbw2\machine_learning\fire_detection\qbw_work\YOLO_NN\a-yolov1-mine_CPU'
imgnames = os.listdir(root_path+r'\data\JPEGImages')
labelnames = os.listdir(root_path+r'\labels')
size=448
cold_ioU0=0.
cold_ioU1=0.
cold_ioU2=0.
cold_ioU3=0.
cold_coor=0.
cold_num=0

non_ioU0=0.
non_ioU1=0.
non_ioU2=0.
non_ioU3=0.
non_coor=0.
non_num=0

warm_ioU0=0.
warm_ioU1=0.
warm_ioU2=0.
warm_ioU3=0.
warm_coor=0.
warm_num=0
for index,image_name in enumerate(imgnames):
    image=cv2.imread(root_path+r'\data\JPEGImages'+'\\'+image_name)
    # print(root_path+r'\data\JPEGImages'+'\\'+image_name)
    # print(image)
    cvtest = cv_test.opencv_test()
    result = cvtest.testing(image)
    # result[0,1,2,3,....]=[(x, y), (x + w, y + h), 'fire']
    label_name=labelnames[index]
    label_result = np.genfromtxt(root_path+r'\labels'+'\\'+label_name,delimiter=' ',dtype='Float64').tolist()
    x1=((label_result[1]-(label_result[3]/2))*size)
    x2=((label_result[1]+(label_result[3]/2))*size)
    y1=((label_result[2]-(label_result[4]/2))*size)
    y2=((label_result[2]+(label_result[4]/2))*size)
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    cx = (label_result[1]*size)
    cy = (label_result[2]*size)
    cx=int(cx)
    cy=int(cy)
    if 'cold' in image_name:
        cold_num+=1

    elif 'non' in image_name:
        non_num+=1

    else:
        warm_num+=1
    if len(result)!=0:
        for result_unit in result:
            xp1,yp1 = result_unit[0]
            xp2,yp2 = result_unit[1]
            cxp=int((xp1+xp2)/2)
            cyp=int((yp1+yp2)/2)
            #print(xp1,xp2,yp1,yp2)
            #ioU计算
            s1 = (x2 - x1) * (y2 - y1)  # opencv框的面积
            s2 = (xp2 - xp1) * (yp2 - yp1)  # yolo框的面积
            # 计算相交矩形
            xmin = max(x1, xp1)
            ymin = max(y1, yp1)
            xmax = min(x2, xp2)
            ymax = min(y2, yp2)

            w = max(0, xmax - xmin)
            h = max(0, ymax - ymin)
            area = w * h  # C∩G的面积
            ioU = area / (s1 + s2 - area)
            # print(ioU)
            #print((cx-cxp)**2+(cy-cyp)**2)
            if 'cold' in image_name:
                if ioU > 0.08:
                    cold_ioU3 += 1.
                if ioU > 0.05:
                    cold_ioU2 += 1.
                if ioU > 0.02:
                    cold_ioU1 += 1.
                if ioU > 0.:
                    cold_ioU0 += 1.
                if ((cx - cxp) ** 2 + (cy - cyp) ** 2) <= 9000:
                    cold_coor += 1.

            elif 'non' in image_name:
                if ioU > 0.08:
                    non_ioU3 += 1.
                if ioU > 0.05:
                    non_ioU2 += 1.
                if ioU > 0.02:
                    non_ioU1 += 1.
                if ioU > 0.:
                    non_ioU0 += 1.
                if ((cx - cxp) ** 2 + (cy - cyp) ** 2) <= 9000:
                    non_coor += 1.

            else:

                if ioU > 0.08:
                    warm_ioU3 += 1.
                if ioU > 0.05:
                    warm_ioU2 += 1.
                if ioU > 0.02:
                    warm_ioU1 += 1.
                if ioU > 0.:
                    warm_ioU0 += 1.
                if ((cx-cxp)**2+(cy-cyp)**2)<=9000:
                    warm_coor+=1.

acc_ioU0=[float(cold_ioU0/cold_num),float(non_ioU0/non_num),float(warm_ioU0/warm_num)]
acc_ioU1=[float(cold_ioU1/cold_num),float(non_ioU1/non_num),float(warm_ioU1/warm_num)]
acc_ioU2=[float(cold_ioU2/cold_num),float(non_ioU2/non_num),float(warm_ioU2/warm_num)]
acc_ioU3=[float(cold_ioU3/cold_num),float(non_ioU3/non_num),float(warm_ioU3/warm_num)]
acc_coor=[float(cold_coor/cold_num),float(non_coor/non_num),float(warm_coor/warm_num)]
img_label=['cold_fire','non_fire','warm_fire']
x=list(range(len(img_label)))
print(acc_ioU0)
print(acc_ioU1)
print(acc_ioU2)
print(acc_ioU3)
print(acc_coor)
total_width,n=1.0,5
width = total_width/n
plt.bar(x, acc_coor, width=width, label='coor_acc',tick_label = img_label,fc = 'pink')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, acc_ioU0, width=width, label='ioU_acc(thelsold:0)',fc = 'red')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, acc_ioU1, width=width, label='ioU_acc(thelsold:0.02)',fc = 'green')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, acc_ioU2, width=width, label='ioU_acc(thelsold:0.05)',fc = 'blue')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, acc_ioU3, width=width, label='ioU_acc(thelsold:0.08)',fc = 'yellow')
for x,a1,a2,a3,a4,a5 in zip(x,acc_coor,acc_ioU0,acc_ioU1,acc_ioU2,acc_ioU3): # 在柱状图上显示具体数值
    plt.text(x-0.8,a1, '%.2f' % float(a1*100.), ha='center', va= 'bottom',fontsize=8)
    plt.text(x-0.6,a2, '%.3f' % float(a2*100.),ha='center', va= 'bottom',fontsize=8)
    plt.text(x -0.4, a3, '%.4f' % float(a3*100.), ha='center', va='bottom', fontsize=8)
    plt.text(x -0.2, a4, '%.4f' % float(a4*100.), ha='center', va='bottom', fontsize=8)
    plt.text(x , a5, '%.4f' % float(a5*100.), ha='center', va='bottom', fontsize=8)

plt.legend()
plt.title(r'accurate rate analysis of testing set', fontsize=20)
plt.savefig(r'D:\qbw2\machine_learning\fire_detection\acc_analysis_opencv.jpg')
plt.show()


