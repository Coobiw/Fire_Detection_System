############导入相关的py文件和库##############
import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import combine
import resnet50
model=resnet50.resnet50()
print('load model...')
model.load_state_dict(torch.load('yolo_fire50.pth'))
model.eval()
root_path=r'D:\qbw2\machine_learning\fire_detection\qbw_work\YOLO_NN\a-yolov1-mine_CPU'
imgnames = os.listdir(root_path+r'\data\JPEGImages')
labelnames = os.listdir(root_path+r'\labels')
size=448
threshold_list=[0.55,0.6,0.65,0.7]
warm_coor=[0.,0.,0.,0.]
warm_lou=[0.,0.,0.,0.]
warm_xu=[0.,0.,0.,0.]
warm_num=0
epoch_counter=0
for i,threshold in enumerate(threshold_list):
    for index,image_name in enumerate(imgnames):
        if 'warm' not in image_name:
            continue
        if epoch_counter==0:
            warm_num+=1
        image=cv2.imread(root_path+r'\data\JPEGImages'+'\\'+image_name)
        # print(root_path+r'\data\JPEGImages'+'\\'+image_name)
        # print(image)
        comtest=combine.combine_test()
        result = comtest.combine(model,image,threshold=threshold)
        # result[0,1,2,3,....]=[(x1, y1), (x2, y2), 'fire', prob]
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
        if len(result)==0:
            warm_lou[i]=warm_lou[i]+1.
        else:
            if len(result)>1:
                warm_xu[i]=warm_xu[i]+float(len(result))-1.
            for result_unit in result:
                xp1,yp1 = result_unit[0]
                xp2,yp2 = result_unit[1]
                cxp=int((xp1+xp2)/2)
                cyp=int((yp1+yp2)/2)
                if((cx-cxp)**2+(cy-cyp)**2<=9000):
                    warm_coor[i]=warm_coor[i]+1
    epoch_counter+=1
    warm_xu[i]=warm_xu[i]/warm_num
    warm_lou[i]=warm_lou[i]/warm_num
    warm_coor[i]=warm_coor[i]/warm_num




threshold_label=['0.55','0.6','0.65','0.7']
x=list(range(len(threshold_label)))
total_width,n=0.9,3
width = total_width/n
plt.bar(x, warm_coor, width=width, label='coor_acc',tick_label = threshold_label,fc = 'pink')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, warm_xu, width=width, label='xujing_rate',fc = 'purple')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, warm_lou, width=width, label='loujing_rate',fc = 'green')
for x,a1,a2,a3 in zip(x,warm_coor,warm_xu,warm_lou): # 在柱状图上显示具体数值
    plt.text(x-0.6,a1, '%.3f' % float(a1*100.), ha='center', va= 'bottom',fontsize=8)
    plt.text(x-0.3,a2, '%.3f' % float(a2*100.),ha='center', va= 'bottom',fontsize=8)
    plt.text(x , a3, '%.3f' % float(a3*100.), ha='center', va='bottom', fontsize=8)

plt.legend()
plt.title(r'combine_threshold_adjust', fontsize=20)
plt.savefig(r'D:\qbw2\machine_learning\fire_detection\new-combine_threshold_adjust_new(non).jpg')
plt.show()
