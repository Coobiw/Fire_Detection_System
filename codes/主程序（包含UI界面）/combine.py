import cv2
from predict import  YOLO_test_new
from resnet50 import resnet50
class combine_test():
    def __init__(self):
        super(combine_test, self).__init__()
        #基本信息
        self.faceCascade = cv2.CascadeClassifier("cascade.xml")
        self.faceCascade.load('cascade_huomiao.xml')


    def opencv_testing(self, frame):
        self.result = []
        img = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rect = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=3,
            minSize=(3, 3),
            flags=cv2.IMREAD_GRAYSCALE
        )

        for (x, y, w, h) in rect:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.result.append([(x, y), (x + w, y + h),'fire'])
        '''
        if len(rect) != 0 :
            (x, y, w, h) = rect[0]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.result.append([(x, y), (x + w, y + h), 'fire'])
        '''
        return self.result

    def combine(self,model,image,threshold=0.6):
        result_opencv = self.opencv_testing(image)

        result_yolo = YOLO_test_new(model,image)

        result = []
        if len(result_yolo)!=0:
            for ((xmin2, ymin2), (xmax2, ymax2), type2, prob) in result_yolo:
                if prob>threshold:
                    result.append([(xmin2, ymin2), (xmax2, ymax2), type2, prob])
                else:
                    for ((xmin1, ymin1), (xmax1, ymax1), type1) in result_opencv:
                        # 计算交并比
                        s1 = (xmax1 - xmin1) * (ymax1 - ymin1)  # opencv框的面积
                        s2 = (xmax2 - xmin2) * (ymax2 - ymin2)  # yolo框的面积
                        # 计算相交矩形
                        xmin = max(xmin1, xmin2)
                        ymin = max(ymin1, ymin2)
                        xmax = min(xmax1, xmax2)
                        ymax = min(ymax1, ymax2)

                        w = max(0, xmax - xmin)
                        h = max(0, ymax - ymin)
                        area = w * h  # C∩G的面积

                        prob += (area / (s1 + s2 - area))#*0.5 #*0.05
                    if prob > threshold:
                        result.append([(xmin2, ymin2), (xmax2, ymax2), type2, prob])
        else:
            for result_index,result_unit in enumerate(result_opencv):
                result_opencv[result_index].append(1.1)
            result = result_opencv


        for left_up, right_bottom, cls, prob in result:
            color = [128, 0, 0]
            cv2.rectangle(image, left_up, right_bottom, color, 2)
            label = 'fire' + str(round(prob, 2))
            text_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
            p1 = (left_up[0], left_up[1] - text_size[1])
            cv2.rectangle(image, (p1[0] - 2 // 2, p1[1] - 2 - baseline), (p1[0] + text_size[0], p1[1] + text_size[1]),
                          color, -1)
            cv2.putText(image, label, (p1[0], p1[1] + baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, 8)

        return result



if __name__ == '__main__':
    img = cv2.imread(r'E:\fire_detecton1.0\fire_detection\none_fire_5.jpg',1)
    model = resnet50()
    result = combine_test().combine(model,img)
    for each in result:
        print(each)
        cv2.rectangle(img,each[0],each[1],(0,0,255),2)
    cv2.imshow('1',img)
    cv2.waitKey(0)
















