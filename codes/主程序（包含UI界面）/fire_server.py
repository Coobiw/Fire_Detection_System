import os
import socket
def fire_server(flag,img_path):
    s=socket.socket() # 1.声明协议类型，同时生成socket链接对象
    s.bind(('localhost',9090))# 绑定要监听端口=(服务器的ip地址+任意一个端口)
    s.listen(5)# 监听
    print('等待客户端连接......')
    counter=0
    while True:
        conn, addr = s.accept()  # 等电话打进来
        # conn就是客户端连过来而在服务器端为其生成的一个连接实例
        print("收到来自{}请求".format(addr))
        while True:
            if(flag==0):
                break
            if counter==0:
                conn.send(bytes('fire_alarm',encoding='utf-8'))
                counter+=1
            data = conn.recv(1024)
            print('client: %s' % data.decode('utf-8'))
            if data.decode('utf-8')=='get fire picture please':
                file_size = os.stat(img_path).st_size  # 获得图像文件的大小，字节单位
                file_info = 'fire_image|%s' % (file_size)
                conn.sendall(bytes(file_info, 'utf-8'))
                with  open(img_path, 'rb') as f: # 以二进制格式打开一个文件用于只读
                    has_sent = 0  # 记录下已经发送的字节数
                    while has_sent != file_size:  # 发送的字节数 不等于 图像的大小，则接着发送
                        file = f.read(1024)  # 一次读1024个字节
                        conn.sendall(file)  # 发送给客户端
                        has_sent += len(file)  # 更新已发送的字节数
                conn.send(bytes('successful send',encoding='utf-8'))
                print('上传成功')
            else:
                conn.send(bytes('you can input "get fire picture please" to get image or you can input "break" to quit',encoding='utf-8'))
            if data.decode('utf-8')=='break':
                break
        break
    s.close()

