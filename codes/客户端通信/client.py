import socket
import os
import winsound

os.chdir(r'E:\fire_detecton1.0\fire_detection\qbw_work\client_demo')
c = socket.socket()
host = '127.0.0.1'
port = 9090
try:
    while True:
        try:
            c.connect((host, port))  # 链接服务器的ip + 端口
            while True:
                data = c.recv(1024)
                print("server:"+'%s'% data.decode('utf-8'))
                if data == b'fire_alarm':
                    duration = 3000
                    freq = 440
                    winsound.Beep(freq, duration)
                msg = input(">>:").strip()  # 获得要向服务端发送的信息，字符串格式
                if len(msg) == 0:
                    continue
                if msg == 'break':
                    break
                c.send(msg.encode('utf-8'))
                if msg=='get fire picture please':
                    data1=c.recv(1024)
                    print('server:'+'%s'% data1.decode('utf-8'))
                    if len(str(data1, 'utf-8').split('|')) == 2:  # 如果返回的字符串长度为2，说明针对的任务2，从服务端传回一张图片
                        filename, filesize = str(data1, 'utf8').split('|')  # 获得指定图像的名称，图像大小

                        filesize = int(filesize)  # 图像大小转换成整形

                        with open('./'+filename+'.jpg', 'ab') as f:  # 以二进制格式打开一个文件用于追加。如果该文件不存在，创建新文件进行写入。
                            has_receive = 0  # 统计接收到的字节数
                            while has_receive != filesize:
                                data2 = c.recv(1024)  # 一次从服务端接收1024字节的数据
                                f.write(data2)  # 写入
                                has_receive += len(data2)  # 更新接收到的字节数


            c.close()
        except ConnectionError:
            pass
except OSError:
    print('您选择使用break退出连接，希望我们的服务能让您满意！')
