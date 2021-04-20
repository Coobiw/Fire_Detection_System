import pandas as pd
import numpy as np
import torch as t
import torch.nn.functional as F
from torch.utils.data import DataLoader
from PIL import Image
from dataset import CamvidDataset
from FCN import FCN
import cfg
import cv2
import matplotlib.pyplot as plt


device = t.device('cpu')#t.device('cuda') if t.cuda.is_available() else t.device('cpu')

Cam_test = CamvidDataset([cfg.TEST_ROOT, cfg.TEST_LABEL], cfg.crop_size)
test_data = DataLoader(Cam_test, batch_size=1, shuffle=True, num_workers=0)

net = t.load('./models_save/FCN_epoch50.pth').to(device)
# net.load_state_dict(t.load("xxx.pth"))
net.eval()

pd_label_color = pd.read_csv('./dataset/class_dict_demo.csv', sep=',')
name_value = pd_label_color['name'].values
num_class = len(name_value)
colormap = []
for i in range(num_class):
	tmp = pd_label_color.iloc[i]
	color = [tmp['r'], tmp['g'], tmp['b']]
	colormap.append(color)

cm = np.array(colormap).astype('uint8')

dir = "./result_pics/"

for i, sample in enumerate(test_data):
	valImg = sample['img'].to(device)
	valLabel = sample['label'].long().to(device)
	out = net(valImg)
	out = F.log_softmax(out, dim=1)
	pre_label = out.max(1)[1].squeeze().cpu().data.numpy()
	pre = cm[pre_label]
	print(pre.shape) #pillow是（W，H） opencv是（H，W）
	# print(type(pre))
	# print(pre.shape)
	pre1 = Image.fromarray(pre)
	pre1.save(dir + str(i) + '.png')
	# cv2.imwrite(dir+str(i)+'.png',pre)
	# cv2.imshow('prediction',cv2.cvtColor(pre, cv2.COLOR_RGB2BGR))# opencv 使用BGR
	# cv2.waitKey(0)
	import os
	os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

	plt.figure("prediction")
	plt.imshow(pre)
	plt.show()
	print('Done')