import torch
from torch.autograd import Variable
import torch.nn as nn
from resnet50 import resnet50
import torchvision.transforms as transforms
import cv2
import numpy as np
import fire_server

def decoder(pred):
	grid_num = 14
	boxes=[]
	probs = []
	cell_size = 1./grid_num
	pred = pred.data
	pred = pred.squeeze(0)
	contain1 = pred[:,:,4].unsqueeze(2)
	contain2 = pred[:,:,9].unsqueeze(2)
	contain = torch.cat((contain1,contain2),2)
	k,_ = contain.max(2)
	k = k.unsqueeze(2)
	mask = (contain == k)
	for i in range(grid_num):
		for j in range(grid_num):
			for b in range(2):
				if mask[i,j,b] == 1:
					box = pred[i,j,b*5:b*5+4]
					contain_prob = torch.FloatTensor([pred[i,j,b*5+4]])
					xy = torch.FloatTensor([j,i])*cell_size
					box[:2] = box[:2]*cell_size + xy
					box_xy = torch.FloatTensor(box.size())
					box_xy[:2] = box[:2] - 0.5*box[2:]
					box_xy[2:] = box[:2] + 0.5*box[2:]
					box_xy = torch.clamp(box_xy, 0, 1)
					max_prob = pred[i,j,10]
					if float((contain_prob*max_prob)) > 0.1:
						boxes.append(box_xy.view(1,4))
						probs.append(contain_prob*max_prob)
	if len(boxes) == 0:
		return
	else:
		boxes = torch.cat(boxes,0)
		probs = torch.cat(probs,0)
	keep = nms(boxes, probs)
	return boxes[keep],probs[keep]
   
def nms(boxes, scores, threshold=0.3):
	keep = []
	indexs = []
	scores = scores.numpy().tolist()
	for i in range(len(boxes)):
		if i in indexs:
			continue
		for j in range(len(boxes)):
			if i == j:
				if i == len(boxes) - 1:
					keep.append(i)
				continue
			if get_IOU(boxes[i], boxes[j]) > threshold:
				if scores[i] < scores[j]:
					break
				indexs.append(j)
			if j == len(boxes) - 1:
				keep.append(i)
	return torch.LongTensor(keep)
				
def get_IOU(box1, box2):
	w = min(box1[2], box2[2]) - max(box1[0], box2[0])
	h = min(box1[3], box2[3]) - max(box1[1], box2[1])
	intr = w * h
	intr = 0 if w < 0 or h < 0 else w * h
	union = (box1[2] - box1[0]) * (box1[3] - box1[1]) + \
				(box2[2] - box2[0]) * (box2[3] - box2[1]) - intr
	return (intr / union)
		
def predict_gpu(model,image_name,root_path=''):
	result = []
	image = cv2.imread(root_path+'\\'+image_name)
	h,w,_ = image.shape
	img = cv2.resize(image,(448,448))
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	mean = (123,117,104)
	img = img - np.array(mean,dtype=np.float32)

	transform = transforms.Compose([transforms.ToTensor(),])
	img = transform(img)
	with torch.no_grad():
		img = Variable(img[None,:,:,:])

	pred = model(img)
	boxes,probs = decoder(pred)

	for i,box in enumerate(boxes):
		x1 = int(box[0]*w)
		x2 = int(box[2]*w)
		y1 = int(box[1]*h)
		y2 = int(box[3]*h)
		prob = float(probs[i])
		result.append([(x1,y1),(x2,y2),'fire',prob])
	return result
	
def predict_camera(model, image):
	result = []
	h,w,_ = image.shape
	img = cv2.resize(image,(448,448))
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	mean = (123,117,104)
	img = img - np.array(mean,dtype=np.float32)

	transform = transforms.Compose([transforms.ToTensor(),])
	img = transform(img)
	with torch.no_grad():
		img = Variable(img[None,:,:,:])

	pred = model(img)
	re = decoder(pred)
	if re == None:
		return []
	boxes,probs = re

	for i,box in enumerate(boxes):
		if(probs[i])>0.5:
			x1 = int(box[0]*w)
			x2 = int(box[2]*w)
			y1 = int(box[1]*h)
			y2 = int(box[3]*h)
			prob = float(probs[i])
			result.append([(x1,y1),(x2,y2),'fire',prob])

	for left_up,right_bottom,cls,prob in result:
		color = [128, 0, 0]
		cv2.rectangle(image,left_up,right_bottom,color,2)
		label = 'fire'+str(round(prob,2))
		text_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
		p1 = (left_up[0], left_up[1]- text_size[1])
		cv2.rectangle(image, (p1[0] - 2//2, p1[1] - 2 - baseline), (p1[0] + text_size[0], p1[1] + text_size[1]), color, -1)
		cv2.putText(image, label, (p1[0], p1[1] + baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, 8)

	return result


def YOLO_test(model, image):
	result = []
	h, w, _ = image.shape
	img = cv2.resize(image, (448, 448))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	mean = (123, 117, 104)
	img = img - np.array(mean, dtype=np.float32)

	transform = transforms.Compose([transforms.ToTensor(), ])
	img = transform(img)
	with torch.no_grad():
		img = Variable(img[None, :, :, :])

	pred = model(img)
	re = decoder(pred)
	if re == None:
		return []
	boxes, probs = re

	for i, box in enumerate(boxes):
		if (probs[i]) > 0.5:
			x1 = int(box[0] * w)
			x2 = int(box[2] * w)
			y1 = int(box[1] * h)
			y2 = int(box[3] * h)
			prob = float(probs[i])
			result.append([(x1, y1), (x2, y2), 'fire', prob])

	return result
def YOLO_test_new(model, image):
	result = []
	h, w, _ = image.shape
	img = cv2.resize(image, (448, 448))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	mean = (123, 117, 104)
	img = img - np.array(mean, dtype=np.float32)

	transform = transforms.Compose([transforms.ToTensor(), ])
	img = transform(img)
	with torch.no_grad():
		img = Variable(img[None, :, :, :])

	pred = model(img)
	re = decoder(pred)
	if re == None:
		return []
	boxes, probs = re

	for i, box in enumerate(boxes):
		if (probs[i]) > 0.:
			x1 = int(box[0] * w)
			x2 = int(box[2] * w)
			y1 = int(box[1] * h)
			y2 = int(box[3] * h)
			prob = float(probs[i])
			result.append([(x1, y1), (x2, y2), 'fire', prob])

	return result
if __name__ == '__main__':
	model = resnet50()
	print('load model...')
	model.load_state_dict(torch.load('yolo_fire50.pth'))
	model.eval()
	image_name = 'none_fire_5.jpg'
	image = cv2.imread(r'E:\fire_detecton1.0\fire_detection'+'\\'+image_name)
	print('predicting...')
	result = predict_gpu(model,image_name,r'E:\fire_detecton1.0\fire_detection')
	if result:
		for left_up,right_bottom,cls,prob in result:
			if prob>=0.5:
				color = [128, 0, 0]
				cv2.rectangle(image,left_up,right_bottom,color,2)
				label = 'fire'+str(round(prob,2))
				text_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
				p1 = (left_up[0], left_up[1]- text_size[1])
				cv2.rectangle(image, (p1[0] - 2//2, p1[1] - 2 - baseline), (p1[0] + text_size[0], p1[1] + text_size[1]), color, -1)
				cv2.putText(image, label, (p1[0], p1[1] + baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, 8)
	# cv2.imwrite(r'E:\fire_detecton1.0\fire_detection\result_give_client.jpg',image)
	if len(result)!=0:
		# try:
		# 	fire_server.fire_server(flag=1,img_path=r'E:\fire_detecton1.0\fire_detection\result_give_client.jpg')
		# except ConnectionError:
			print('通信结束啦!')
			print('发送的结果图展示如下')
		# cv2.imwrite(r'D:\qbw2\machine_learning\fire_detection\result9_0.jpg',image)
			cv2.imshow('result',image)
			wait_key=cv2.waitKey(0)

