import pyodbc
import os

class database():
    def __init__(self):
        super(database, self).__init__()
        #基本信息
        #self.conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=DESKTOP-3J3JQ49;DATABASE=fire_detect_record;UID=sa;PWD=7758521')
        self.conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=.\sqlexpress;DATABASE=fire_detect_record;UID=sa;PWD=729608')
        #self.conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=127.0.0.2,6565;DATABASE=fire_detect_record;UID=zy;PWD=az20000808')
        self.table_retime_record = 'dbo.[retime record]'
        self.table_retime_detial = 'dbo.[retime detial]'
        self.table_offline_original_record = 'dbo.[offline original record]'
        self.table_offline_tested_record = 'dbo.[offline tested record]'
        self.table_offline_tested_detial = 'dbo.[offline tested detial]'
        #实时检测参数
        self.oder_num = 0
        self.retime_begin_frame = 0
        self.retime_max_store =3
        #离线检测参数
        self.offline_label = ''
        self.offline_begin_frame =0

    def insert_retime_record(self, id, name,addr):
        cur = self.conn.cursor()
        cur.execute("exec dbo.[insert_retime_record]  " + str(id) + ", '" + name + "','" + addr +"'")
        cur.commit()
        cur.close()

    def insert_retime_detial(self, name,type,begin_frame):
        cur = self.conn.cursor()
        cur.execute(
            "select id from dbo.[retime record] where name = '" + name + "'")
        id = cur.fetchone()


        id = id[0]

        cur.execute("exec dbo.[insert_retime_detial]  " + str(id) + ", '" + name + "','" + type +"'," +str(begin_frame))
        cur.commit()
        cur.close()

    def insert_retime_detial_end(self, name, type,begin_frame,end_frame):
        cur = self.conn.cursor()
        cur.execute(
            "select id from dbo.[retime record] where name = '" + name + "'")
        id = cur.fetchone()[0]
        print(id)
        cur.execute("exec dbo.[insert_retime_detial_end]  " + str(id) + ",'" + type + "', " + str(begin_frame) + ", " + str(
            end_frame))
        cur.commit()
        cur.close()

    def insert_retime_result_sum(self, id, result):
        cur = self.conn.cursor()
        cur.execute("exec dbo.[insert_retime_result_sum]  " + str(id) + ", '" + result + "'")
        cur.commit()
        cur.close()

    def retime_delete(self, id):
        cur = self.conn.cursor()
        cur.execute("exec dbo.[retime_delete]  "+ str(id))
        cur.commit()
        cur.close()


    def insert_offline_record(self, name_original, addr_original,name_tested, addr_tested):
        cur = self.conn.cursor()
        self.offline_file_delete(name_original)
        cur.execute("exec dbo.[insert_offline_record]  '" + name_original + "', '" + addr_original + "','" + name_tested +"','" +addr_tested+ "'")
        self.offline_label = name_original
        cur.commit()
        cur.close()

    def insert_offline_detial(self, label,name,type,begin_frame):
        cur = self.conn.cursor()
        cur.execute("exec dbo.[insert_offline_detial]  '" + label + "', '" + name + "','" + type +"'," + str(begin_frame))
        cur.commit()
        cur.close()

    def insert_offline_detial_end(self, label,type,begin_frame,end_frame):
        cur =self.conn.cursor()
        cur.execute(
            "exec dbo.[insert_offline_detial_end]  " + label + ",'" + type + "', " + str(begin_frame) + ", " + str(
                end_frame))
        cur.commit()
        cur.close()

    def insert_offline_result_sum(self, label, result):
        cur = self.conn.cursor()
        cur.execute(
            "exec dbo.[insert_offline_result_sum]  '" + label + "' , '" + result + "'")
        cur.commit()
        cur.close()

    def offline_delete(self, label):
        cur = self.conn.cursor()
        cur.execute("select name from dbo.[offline original record] where dbo.[offline original record].name = '" + label +"'")
        list = cur.fetchone()
        print(list)
        if list:
            cur.execute("exec dbo.[offline_delete] '" + label +"'")
        else:
            cur.execute(
                "select label from dbo.[offline tested record] where dbo.[offline tested record].name = '" + label + "'")
            list = cur.fetchone()
            if list:
                cur.execute("exec dbo.[offline_delete] '" + list[0] +"'")
        cur.commit()
        cur.close()

    ####自动给实时检测加序号######
    def retime_insert_auto(self, name ,addr):
        cur = self.conn.cursor()
        cur.execute("select id from dbo.[retime record] ")
        list = cur.fetchall()
        print(list)
        if len(list) == 0 :
            self.insert_retime_record(1, name, addr)
            self.oder_num = 1
        else:
            self.oder_num = int(max(list)[0])+1
            self.insert_retime_record(self.oder_num, name, addr)
        while len(list)>self.retime_max_store:
            self.retime_file_delete(min(list)[0])
            cur.execute("select id from dbo.[retime record] ")
            list = cur.fetchall()
        cur.commit()
        cur.close()

    #######删除数据时同时删除文件##########
    def retime_file_delete(self, id):
        cur = self.conn.cursor()
        cur.execute("select addr from dbo.[retime record] where dbo.[retime record].id = " + str(id))
        list = cur.fetchone()
        if list:
            if os.path.exists(list[0]):
                os.remove(list[0])
            else:
                pass
        else:
            pass
        self.retime_delete(id)
        cur.commit()
        cur.close()

    def offline_file_delete(self, label):
        cur = self.conn.cursor()
        cur.execute("select name,addr from dbo.[offline original record] where dbo.[offline original record].name = '" + label + "'")
        list = cur.fetchone()
        if list:
            self.offline_label = label
            '''
            if os.path.exists(list[1]):
                os.remove(list[1])
            else:
                pass
            '''
            cur.execute(
                "select name,addr from dbo.[offline tested record] where dbo.[offline tested record].label = '" + label + "'")
            list = cur.fetchone()
            if list:
                if os.path.exists(list[1]):
                    os.remove(list[1])
                else:
                    pass
            cur.execute("exec dbo.[offline_delete] '" + self.offline_label + "'")
        else:
            cur.execute(
                "select label,addr from dbo.[offline tested record] where dbo.[offline tested record].name = '" + label + "'")
            list = cur.fetchone()
            if list:
                self.offline_label = list[0]
                '''
                if os.path.exists(list[1]):
                    os.remove(list[1])
                else:
                    pass
                '''
            cur.execute(
                "select addr from dbo.[offline original record] where dbo.[offline original record].name = '" + self.offline_label + "'")
            list = cur.fetchone()
            if list:
                if os.path.exists(list[0]):
                    os.remove(list[0])
                else:
                    pass
            cur.execute("exec dbo.[offline_delete] '" + self.offline_label + "'")

        cur.commit()
        cur.close()
    ########统计结果#################
    def retime_counting(self,id):
        cur = self.conn.cursor()
        cur.execute("select tested_type from dbo.[retime detial] where dbo.[retime detial].id = " +str(id))
        list = cur.fetchall()
        if len(list) == 0:
            self.insert_retime_result_sum(id,'fire:0;spark:0')
        else:
            fire = 0
            spark = 0
            for i in list:
                if i[0] == 'fire' or i[0] == 'forestfire' or i[0] == 'spark':
                    fire +=1
                elif i[0] == 'spark':
                    spark +=1
            self.insert_retime_result_sum(id, 'fire:'+str(fire)+';spark:'+str(spark))
        cur.commit()
        cur.close()

    def offline_counting(self,label):
        cur = self.conn.cursor()
        cur.execute("select tested_type from dbo.[offline tested detial] where dbo.[offline tested detial].label = '" + label+ "'")
        list = cur.fetchall()
        if len(list) == 0:
            self.insert_offline_result_sum(label,'fire:0;spark:0')
        else:
            fire = 0
            spark = 0
            for i in list:
                if i[0] == 'fire':
                    fire +=1
                elif i[0] == 'spark':
                    spark +=1
                else:
                    pass
            self.insert_offline_result_sum(label, 'fire:'+str(fire)+';spark:'+str(spark))
        cur.commit()
        cur.close()

##########查询数据库单张表内所有信息
    def inquiry(self,table):
        cur = self.conn.cursor()
        cur.execute("select * from " +table)
        list = cur.fetchall()
        for i in list:
            if str(i[0]).isnumeric():
                if int(i[0]) == 0:
                    pass
                else:
                    self.retime_counting(i[0])
            else:
                self.offline_counting(i[0])
        cur.execute("select * from " + table)
        list = cur.fetchall()
        cur.commit()
        cur.close()
        return list

    def inquiry_detial(self,id,name):
        if id.isnumeric():
            if int(id) == 0:
                cur = self.conn.cursor()
                cur.execute("select * from " + self.table_offline_tested_detial + " where label = '" + name + "'")
                list = cur.fetchall()
            else:
                cur = self.conn.cursor()
                cur.execute("select * from " + self.table_retime_detial + " where id = " + id )
                list = cur.fetchall()
        else:
            cur = self.conn.cursor()
            cur.execute("select * from " + self.table_offline_tested_detial + " where label = '" + id + "'")
            list = cur.fetchall()
        cur.commit()
        cur.close()
        for i in range (len(list)):
            if list[i][4]:
                pass
            else:
                list[i][4] ='end'
        if list:
            print(list)
            return list
        else:
            return


if __name__ == '__main__':
    database = database()
    #database.insert_retime_record(0, 'nnsl','E:/ruanjiankeshe')
    #database.insert_retime_detial( 'nnsl', 'fire',  12)
    #database.insert_retime_detial_end('nnsl','fire', 12, 21)
    #database.insert_retime_result_sum(0,'fire:5;spark:3') #y
    #database.retime_delete(10) #y
    database.insert_offline_record('testing1', 'E:/ruanjiankeshe/offline_tested.avi', 'testing1_tested', 'E:/ruanjiankeshe/offline_tested.avi')
    database.insert_offline_detial('testing1','testing_tested', 'spark', 9) #y
    database.insert_offline_detial_end('testing1' ,'spark', 9 , 20) #cnmbuxing
    database.insert_offline_result_sum('testing1', 'fire:5;spark:0') #y
    #database.offline_delete('testing1')
    #database.retime_insert_auto('tesing3','e:/database/realtime.mp4')
    #database.offline_file_delete('testing1')
    #database.retime_counting(0)
    #database.offline_counting('testing1')
    database.offline_counting('testing1')
    #database.retime_file_delete(21)
    #database.inquiry(database.table_offline_original_record)
    #database.inquiry_detial('testing2', 'testing1_tested')
    database.conn.close()














