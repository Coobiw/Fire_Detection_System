import sys
import cv2
import qdarkstyle
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from all_update4 import Ui_MainWindow
#图像处理
from database import database
from opencv_test import opencv_test
from combine import combine_test
#神经网络
#from resnet10 import resnet10
from resnet50 import resnet50


#初始化窗口
class main_Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(main_Window, self).__init__(parent)
        # 初始化定时器
        self.timer_camera = QtCore.QTimer()  #实时检测
        self.timer_video = QtCore.QTimer()   #离线检测
        self.timer_record = QtCore.QTimer()  #检测记录
        self.timer_show = QtCore.QTimer()   # 算法展示
        self.timer_show_real = QtCore.QTimer()  # 算法展示实时检测
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.fps = 30
        self.counting = 0
        self.record_time = 10 #录制十秒
        self.max = 3 #最多录制三份
        self.total = self.record_time * self.fps #每份录制这么多帧
        self.shape = (448, 448)
        self.saving_addr = '录像'
        # 初始化文件写入 文件名 编码解码器 帧率 文件大小
        #self.VWirte = cv2.VideoWriter('./' + self.saving_addr + '/' +time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +'.avi',
        #                              cv2.VideoWriter_fourcc('I', '4', '2', '0'), self.fps, self.shape)
        self.CAM_NUM = 0
        self.mode = 'opencv'
        #初始化yolo
        self.net = resnet50()
        self.net.eval()

        #火焰统计
        self.type = ['fire','forestfire','smog','spark']
        self.flag = [0,0,0,0] #打火机火焰，森林火焰，烟雾，电火花
        self.begin_frame = [0,0,0,0]
        self.type_counting = [0,0,0,0]
        self.tolerance = 15 #火焰检测允许出现15帧中断即0.5秒
        # 火焰统计
        self.counting = 0
        #self.type = ''

        #离线检测补充
        self.addr = ''
        self.mode = ''

        #数据记录页面补充


        # 初始化数据库与信息
        self.database = database()

        # opencv检测初始化
        self.opencv_testing = opencv_test()

        # 联合检测初始化
        self.combine_testing = combine_test()

        self.setupUi(self)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = main_Window()
    myWin.show()
    sys.exit(app.exec_())