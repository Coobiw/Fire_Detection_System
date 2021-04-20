import cv2

class opencv_test():
    def __init__(self):
        super(opencv_test, self).__init__()
        #基本信息
        self.faceCascade = cv2.CascadeClassifier("cascade.xml")
        self.faceCascade.load('cascade_huomiao.xml')


    def testing(self, frame):
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
        '''
        for (x, y, w, h) in rect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.result.append([(x, y), (x + w, y + h),'fire'])
        '''
        if len(rect) != 0 :
            (x, y, w, h) = rect[0]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.result.append([(x, y), (x + w, y + h), 'fire'])
        return self.result


if __name__ == '__main__':
    img = cv2.imread(r'E:\fire_detecton1.0\fire_detection\none_fire_5.jpg',1)
    result = opencv_test().testing(img)
    for each in result:
        print(each)
        cv2.rectangle(img,each[0],each[1],(0,255,0),2)
    cv2.imshow('1',img)
    cv2.waitKey(0)

