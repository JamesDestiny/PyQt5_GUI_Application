import sys
import time  # 增加延时，使启动界面时间足够
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.Admin import *
from UI.OrP import *
from UI.OrP_zc import *
from UI.Worker import *
from test_plus import *
from UI.VIP import *
from UI.VIP_zc import *
from databases.db_Flight import *
from databases.db_Admin import *
from databases.db_Booked import *
from databases.db_OrdinaryP import *
from databases.db_VIP import *
from databases.db_Worker import *



#定义跳出超级管理员登录页面的类
class Window_Sadmin(QDialog,Ui_Admin):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)
    #定义获取输入框管理员账号的函数
    def get_zhanghao(self):
        return self.lineEdit.text()#返回第一个单行文本框的输入内容

    #定义获取输入框管理员密码的函数
    def get_mima(self):
        return self.lineEdit_2.text()#返回第二个单行文本框的输入内容

    #定义登录界面中确认pushButton的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.get_zhanghao() == 'James' and self.get_mima() == '123456':  # 当账号密码匹配成功时，代表登录成功
            QMessageBox.information(self, '成功', '登录成功！')
            self.close()
            return 1
        else:
            QMessageBox.information(self, 'error', '账号或者密码错误！请重新输入')
            self.lineEdit.setText('')  # 将第一个单行文本框清空
            self.lineEdit_2.setText('')  # 将第二个单行文本框清空
            return 0

    @pyqtSlot()
    #定义登录界面中取消pushButton2的触发器函数
    def on_pushButton_2_clicked(self):
        self.close()

    # 定义跳出普通管理员登录页面的类
class Window_Padmin(QDialog, Ui_Admin):
        def __init__(self):
            QDialog.__init__(self, parent=None)
            self.setupUi(self)

        # 定义获取输入框管理员账号的函数
        def get_zhanghao(self):
            return self.lineEdit.text()  # 返回第一个单行文本框的输入内容

        # 定义获取输入框管理员密码的函数
        def get_mima(self):
            return self.lineEdit_2.text()  # 返回第二个单行文本框的输入内容

        # 定义登录界面中确认pushButton的触发器函数
        @pyqtSlot()
        def on_pushButton_clicked(self):
            pad = admin(self.get_zhanghao(),self.get_mima())#建立一个管理员数据库类的对象变量
            if pad.isExited():  # 当账号密码匹配成功时，代表登录成功,导入了管理员数据库类中的判断账号密码是否存在的函数isExited（）
                QMessageBox.information(self, '成功', '登录成功！')
                self.close()
                return 1
            else:
                QMessageBox.information(self, 'error', '账号或者密码错误！请重新输入')
                self.lineEdit.setText('')  # 将第一个单行文本框清空
                self.lineEdit_2.setText('')  # 将第二个单行文本框清空
                return 0


        @pyqtSlot()
        # 定义登录界面中取消pushButton2的触发器函数
        def on_pushButton_2_clicked(self):
            self.close()

#定义跳出操作员登录页面的类
class Window_worker(QDialog,Ui_Worker):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)

    def get_zhanghao(self):
        return self.lineEdit.text()#获得操作员账号，返回第一个单行文本框的内容

    def get_mima(self):
        return self.lineEdit_2.text()#获得操作员密码，返回第二个单行文本框的内容

    #定义操作员登录界面的确认按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        pad = Worker(self.get_zhanghao(),self.get_mima())#导入操作员数据库，定义操作员类的对象变量
        if pad.isExited():#当账号密码在数据库中有备份时，才可以接下来的操作
            QMessageBox.information(self,'成功','登录成功！')
            self.close()#登录成功后关闭对话框
            return 1
        else:#数据库中没有该用户
            QMessageBox.information(self,'error','账号或密码错误')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            return 0
    #定义界面取消按钮的触发器函数

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.close()#关闭登录窗口


#定义跳出普通用户登录页面的类
class Window_OrP(QDialog,Ui_OrP):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)
    #定义从单行文本框获取用户姓名的函数
    def getname(self):
        return self.lineEdit.text()
    #定义从单行文本框获取的用户的身份证号的函数
    def getid(self):
        return self.lineEdit_2.text()
    #定义普通用户登录栏中确认按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        pad = OrdinaryP(self.getname(),self.getid())#将从文本框中获取到的内容放入普通用户数据库所定义的类中
        if pad.isexited():#导入普通用户数据库类中的根据姓名和身份证号码判断用户是否存在的函数
            QMessageBox.information(self,'成功','登录成功！')
            self.close()
            return 1
        else:#如果用户不存在的话，或者是身份证和姓名不匹配的话，报错，并且提示用户若未注册，请先注册
            QMessageBox.information(self,'error','姓名或者身份证号出现错误，若未注册还请先注册')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')#将输入文本框全部置空
            return 0

    #定义普通用户登录栏中取消按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.close()#关闭窗口

    #定义普通用户栏中注册按钮的触发器函数
    @pyqtSlot()#防止界面需要两次点击进行关闭
    def on_pushButton_2_clicked(self):
        #按下注册之后，需要跳出注册界面，并且先关闭当前登录界面，(同时注册成功后跳出登录界面，关闭注册界面)括号内在注册界面类中实现
        self.close()
        Ord = Window_OrP_zc()#定义注册页面的类的变量
        Ord.exec_()#使注册页面显示出来


#定义普通用户注册页面的类
class Window_OrP_zc(QDialog,Ui_OrP_zc):
    def __init__(self):
        QDialog.__init__(self,parent=None)
        self.setupUi(self)

    # 定义普通用户登录栏中确认按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        pad = OrdinaryP(self.getname(), self.getid())  # 将从文本框中获取到的内容放入普通用户数据库所定义的类中
        win = Window_OrP()#定义一个普通用户登录的界面的类变量，为了在注册成功之后跳出该登录界面
        if pad.isexited():  # 导入普通用户数据库类中的根据姓名和身份证号码判断用户是否存在的函数
            QMessageBox.information(self, 'error', '该普通用户已经存在！')#如果存在，则报错，注册不成功
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')  # 将输入文本框全部置空
        else:  # 如果用户不存在的话，则代表这是一个新的注册用户
            try:
                #设置用户输入的姓名和身份证号都不能为空
                if self.getname()=='' or self.getid()=='':
                    QMessageBox.information(self, 'error', '请输入有效的姓名信息和身份证号信息')
                else:
                    pad.add()  # 导入普通用户数据库中的导入用户数据函数
                    QMessageBox.information(self, '成功', '注册成功')
                    # 注册成功之后先关闭注册界面
                    self.close()
                    time.sleep(0.4)
                    win.exec_()


            except Exception as e:
                QMessageBox.information(self,'error',str(e))#若执行不成功则提出警告，并输出错误信息
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')  # 将输入文本框全部置空

    def out(self):
        pad = OrdinaryP(self.getname(),self.getid())  # 导入操作员数据库，定义操作员类的对象变量
        if pad.isExited():  # 当账号密码在数据库中有备份时，才可以接下来的操作
            return 1
        else:  # 数据库中没有该用户
            return 0

    # 定义普通用户注册栏中取消按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        win = Window_OrP()  # 定义一个普通用户登录的界面的类变量，为了在注册取消之后跳出该登录界面
        self.close()  # 关闭窗口
        time.sleep(0.4)
        win.exec_()#跳出登录界面

    #返回第一个文本框代表的用户姓名
    def getname(self):
        return self.lineEdit.text()
    #返回第二个文本框代表的用户身份证号
    def getid(self):
        return self.lineEdit_2.text()




# 定义跳出VIP用户登录页面的类
class Window_VIP(QDialog, Ui_VIP):
    def __init__(self):
        QDialog.__init__(self, parent=None)
        self.setupUi(self)

    # 定义从单行文本框获取用户姓名的函数
    def getname(self):
        return self.lineEdit.text()

    # 定义从单行文本框获取的用户的身份证号的函数
    def getid(self):
        return self.lineEdit_2.text()

    # 定义VIP用户登录栏中确认按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        pad = OrdinaryP(self.getname(), self.getid())  # 将从文本框中获取到的内容放入VIP用户数据库所定义的类中
        if pad.isexited():  # 导入VIP用户数据库类中的根据姓名和身份证号码判断用户是否存在的函数
            QMessageBox.information(self, '成功', '登录成功！')
            self.close()
            return 1
        else:  # 如果用户不存在的话，或者是身份证和姓名不匹配的话，报错，并且提示用户若未注册，请先注册
            QMessageBox.information(self, 'error', '姓名或者身份证号出现错误，若未注册还请先注册')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')  # 将输入文本框全部置空
            return 0

    # 定义VIP用户登录栏中取消按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.close()  # 关闭窗口

    # 定义VIP用户栏中注册按钮的触发器函数
    @pyqtSlot()  # 防止界面需要两次点击进行关闭
    def on_pushButton_2_clicked(self):
        # 按下注册之后，需要跳出注册界面，并且先关闭当前登录界面，(同时注册成功后跳出登录界面，关闭注册界面)括号内在注册界面类中实现
        self.close()
        Ord = Window_VIPzc()  # 定义注册页面的类的变量
        Ord.exec_()  # 使注册页面显示出来

# 定义跳出VIP用户注册页面的类
class Window_VIPzc(QDialog, Ui_VIP_zc):
    def __init__(self):
        QDialog.__init__(self, parent=None)
        self.setupUi(self)
    # 定义VIP用户注册栏中确认按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_clicked(self):
        pad = VIP(self.getname(), self.getid())  # 将从文本框中获取到的内容放入VIP用户数据库所定义的类中
        win = Window_VIP()  # 定义一个VIP用户登录的界面的类变量，为了在注册成功之后跳出该登录界面
        if pad.isexited():  # 导入VIP用户数据库类中的根据姓名和身份证号码判断用户是否存在的函数
            QMessageBox.information(self, 'error', '该VIP用户已经存在！')  # 如果存在，则报错，注册不成功
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')  # 将输入文本框全部置空
        else:  # 如果用户不存在的话，则代表这是一个新的注册用户
            try:
                # 设置用户输入的姓名和身份证号都不能为空，且输入正确邀请码为1314520。
                if self.getname() == '' or self.getid() == '' :
                    QMessageBox.information(self, 'error', '请输入有效的姓名信息和身份证号信息')
                elif self.getname()!=''and self.getid()!='' and self.getyaoqingma()!='1314520':
                    QMessageBox.information(self,'error','邀请码错误！请查看帮助')
                else:
                    pad.add()  # 导入VIP用户数据库中的导入用户数据函数
                    QMessageBox.information(self, '成功', '注册成功')
                    # 注册成功之后先关闭注册界面
                    self.close()
                    time.sleep(0.2)
                    win.exec_()

            except Exception as e:
                QMessageBox.information(self, 'error', str(e))  # 若执行不成功则提出警告，并输出错误信息
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')  # 将输入文本框全部置空

    # 定义VIP用户注册栏中取消按钮的触发器函数
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        win = Window_VIP()  # 定义一个VIP用户登录的界面的类变量，为了在注册取消之后跳出该登录界面
        self.close()  # 关闭窗口
        time.sleep(0.4)
        win.exec_()  # 跳出登录界面

    # 返回第一个文本框代表的用户姓名
    def getname(self):
        return self.lineEdit.text()

    # 返回第二个文本框代表的用户身份证号
    def getid(self):
        return self.lineEdit_2.text()

    #返回第三个文本框代表的邀请码
    def getyaoqingma(self):
        return self.lineEdit_3.text()

#定义主界面的类
class Window_one(QMainWindow,Ui_Window):
    def __init__(self):
        QMainWindow.__init__(self,parent=None)
        self.setupUi(self)
        time.sleep(1)#使启动界面可以多显示2秒
        self.frame.close()
    #定义槽函数
    @pyqtSlot()
    #定义菜单栏上退出action被点击时触发的函数,用on_triggered表示
    def on_actiontuichu_triggered(self):
        sys.exit()

    @pyqtSlot()
    #定义登录栏上退出action（actionquit）被点击时触发的函数
    def on_actionquit_triggered(self):
        sys.exit()

    @pyqtSlot()
    #定义登录栏超级管理员登录
    def on_actionchaoji_triggered(self):
        try:
            admin = Window_Sadmin()#定义对话框变量
            admin.exec_()#使对话框变量显示出来
            #接下来从输入框输入内容判断并且识别该超级管理员是否存在，由于是个人操作，超级管理员只有一个
            if admin.on_pushButton_clicked():
                self.menubar.setEnabled(False)
                self.frame.show()
                self.label.setEnabled(True)
                self.label.setText('欢迎！超级管理员 {}'.format(str(admin.get_zhanghao())))
                self.tab.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.tab_2.setEnabled(False)
                self.tab_3.setEnabled(False)
                self.tab_4.setEnabled(False)
        except Exception as  e:
            QMessageBox.information(admin,'错误',str(e))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            pad = admin(self.lineEdit.text(),self.lineEdit_2.text())
            if self.lineEdit.text()!=''and self.lineEdit_2.text()!='' and self.lineEdit_3.text()!='':
                if self.lineEdit_2.text()==self.lineEdit_3.text():
                    if pad.isLogin():
                        QMessageBox.information(self, 'error', '该管理员账号已经存在！请重新输入')
                        self.lineEdit.setText('')
                        self.lineEdit_2.setText('')
                        self.lineEdit_3.setText('')
                    else:
                        pad.add()
                        QMessageBox.information(self,'成功','添加管理员账号成功！')
                        self.lineEdit.setText('')
                        self.lineEdit_2.setText('')
                        self.lineEdit_3.setText('')
                else:
                    QMessageBox.information(self, 'error', '两次密码输入不一致！请重新输入')
                    self.lineEdit_2.setText('')
                    self.lineEdit_3.setText('')
            else:
                QMessageBox.information(self,'error','请输入有效的账号密码')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            pad = admin(self.lineEdit_4.text(),'')
            if self.lineEdit_4.text()=='':
                QMessageBox.information(self,'error','请输入有效的账号！')
            else:
                if pad.isLogin():
                    pad.delete()
                    QMessageBox.information(self,'成功','删除管理员成功！')
                    self.lineEdit_4.setText('')
                else:
                    QMessageBox.information(self,'error','该管理员用户不存在！请重新输入')
                    self.lineEdit_4.setText('')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))


    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        try:
            pad = admin('','')
            list = pad.show_all()
            for i in list:
                self.textBrowser.append("用户名："+i.admin_user+"       "+"密码："+i.admin_pd+"  ;")
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        self.textBrowser.setText('')

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.frame.close()
        self.menubar.setEnabled(True)

    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        try:
            pad = Worker(self.lineEdit_5.text(), self.lineEdit_7.text())
            if self.lineEdit_5.text() != '' and self.lineEdit_7.text() != '' and self.lineEdit_6.text() != '':
                if self.lineEdit_7.text() == self.lineEdit_6.text():
                    if pad.isLogin():
                        QMessageBox.information(self, 'error', '该操作员账号已经存在！请重新输入')
                        self.lineEdit_5.setText('')
                        self.lineEdit_7.setText('')
                        self.lineEdit_6.setText('')
                    else:
                        pad.add()
                        QMessageBox.information(self, '成功', '添加操作员账号成功！')
                        self.lineEdit_5.setText('')
                        self.lineEdit_7.setText('')
                        self.lineEdit_6.setText('')
                else:
                    QMessageBox.information(self, 'error', '两次密码输入不一致！请重新输入')
                    self.lineEdit_7.setText('')
                    self.lineEdit_6.setText('')
            else:
                QMessageBox.information(self, 'error', '请输入有效的账号密码')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        self.lineEdit_5.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_6.setText('')

    @pyqtSlot()
    def on_pushButton_21_clicked(self):
        try:
            pad = Worker(self.lineEdit_18.text(), '')
            if self.lineEdit_18.text() == '':
                QMessageBox.information(self, 'error', '请输入有效的账号！')
            else:
                if pad.isLogin():
                    pad.delete()
                    QMessageBox.information(self, '成功', '删除操作员成功！')
                    self.lineEdit_18.setText('')
                else:
                    QMessageBox.information(self, 'error', '该操作员用户不存在！请重新输入')
                    self.lineEdit_18.setText('')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        self.lineEdit_18.setText('')

    @pyqtSlot()
    def on_pushButton_22_clicked(self):
        try:
            pad = Worker('', '')
            list = pad.show_all()
            for i in list:
                self.textBrowser_3.append("用户名：" + i.worker_user + "       " + "密码：" + i.worker_pd + "  ;")
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_23_clicked(self):
        self.textBrowser_3.setText('')

    @pyqtSlot()
    #定义登录栏普通管理员登录
    def on_actionputong_triggered(self):
        try:
            admin = Window_Padmin()  # 定义对话框变量
            admin.exec_()  # 使对话框变量显示出来
            if admin.on_pushButton_clicked():
                self.menubar.setEnabled(False)
                self.frame.show()
                self.label.setEnabled(True)
                self.label.setText('欢迎！管理员 {}'.format(str(admin.get_zhanghao())))
                self.tab_2.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.tab.setEnabled(False)
                self.tab_3.setEnabled(False)
                self.tab_4.setEnabled(False)
        except Exception as  e:
            QMessageBox.information(self, '错误', str(e))

    @pyqtSlot()
    def on_pushButton_24_clicked(self):
        try:
            pad = Worker(self.lineEdit_19.text(), self.lineEdit_21.text())
            if self.lineEdit_19.text() != '' and self.lineEdit_21.text() != '' and self.lineEdit_20.text() != '':
                if self.lineEdit_21.text() == self.lineEdit_20.text():
                    if pad.isLogin():
                        QMessageBox.information(self, 'error', '该操作员账号已经存在！请重新输入')
                        self.lineEdit_19.setText('')
                        self.lineEdit_20.setText('')
                        self.lineEdit_21.setText('')
                    else:
                        pad.add()
                        QMessageBox.information(self, '成功', '添加操作员账号成功！')
                        self.lineEdit_19.setText('')
                        self.lineEdit_20.setText('')
                        self.lineEdit_21.setText('')
                else:
                    QMessageBox.information(self, 'error', '两次密码输入不一致！请重新输入')
                    self.lineEdit_20.setText('')
                    self.lineEdit_21.setText('')
            else:
                QMessageBox.information(self, 'error', '请输入有效的账号密码')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_25_clicked(self):
        self.lineEdit_19.setText('')
        self.lineEdit_20.setText('')
        self.lineEdit_21.setText('')

    @pyqtSlot()
    def on_pushButton_32_clicked(self):
        try:
            pad = Worker(self.lineEdit_26.text(), '')
            if self.lineEdit_26.text() == '':
                QMessageBox.information(self, 'error', '请输入有效的账号！')
            else:
                if pad.isLogin():
                    pad.delete()
                    QMessageBox.information(self, '成功', '删除操作员成功！')
                    self.lineEdit_26.setText('')
                else:
                    QMessageBox.information(self, 'error', '该操作员用户不存在！请重新输入')
                    self.lineEdit_26.setText('')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_33_clicked(self):
        self.lineEdit_26.setText('')

    @pyqtSlot()
    def on_pushButton_35_clicked(self):
        try:
            pad = Worker('', '')
            list = pad.show_all()
            for i in list:
                self.textBrowser_5.append("用户名：" + i.worker_user + "       " + "密码：" + i.worker_pd + "  ;")
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_34_clicked(self):
        self.textBrowser_5.setText('')

    @pyqtSlot()
    def on_pushButton_38_clicked(self):
        try:
            pad = flight(self.lineEdit_27.text(),self.lineEdit_28.text(),self.lineEdit_29.text(),self.lineEdit_30.text(),int(self.lineEdit_31.text()),int(self.lineEdit_32.text()))
            if self.lineEdit_27.text()=='' or self.lineEdit_28.text()=='' or self.lineEdit_29.text()=='' or self.lineEdit_30.text()=='' or self.lineEdit_31.text()=='' or self.lineEdit_32.text()=='':
                    QMessageBox.information(self,'error','请输入有效的航班信息！')
                    self.lineEdit_27.setText('')
                    self.lineEdit_28.setText('')
                    self.lineEdit_29.setText('')
                    self.lineEdit_30.setText('')
                    self.lineEdit_31.setText('')
                    self.lineEdit_32.setText('')
            else:
                if pad.isexited():
                    QMessageBox.information(self, 'error', '该航班号已经存在！请重新输入')
                    self.lineEdit_27.setText('')
                    self.lineEdit_28.setText('')
                    self.lineEdit_29.setText('')
                    self.lineEdit_30.setText('')
                    self.lineEdit_31.setText('')
                    self.lineEdit_32.setText('')
                else:
                    if (self.lineEdit_31.text()).isdigit() and (self.lineEdit_32.text()).isdigit():
                        pad.add()
                        QMessageBox.information(self, '成功', '导入航班信息成功！')
                        self.lineEdit_27.setText('')
                        self.lineEdit_28.setText('')
                        self.lineEdit_29.setText('')
                        self.lineEdit_30.setText('')
                        self.lineEdit_31.setText('')
                        self.lineEdit_32.setText('')
                    else:
                        QMessageBox.information(self,'error','请输入整数形式的余票数和订票数！请重新输入！')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_39_clicked(self):
        self.lineEdit_27.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
        self.lineEdit_32.setText('')

    @pyqtSlot()
    def on_pushButton_40_clicked(self):
        QMessageBox.information(self,'提示','该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_41_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_42_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_43_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_44_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_45_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_46_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_47_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_48_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_49_clicked(self):
        QMessageBox.information(self, '提示', '该功能正在完善！敬请期待！')

    @pyqtSlot()
    def on_pushButton_36_clicked(self):
        try:
            pad = flight('','','','',0,0)
            list = pad.show_all()
            for i in list:
                self.textBrowser_6.append('航班号：'+i.Flight_num+'     '+'飞机号: '+i.Aircraft_num+'    '+'出发地: '+i.Start+'     '+'目的地：'+i.Destination+'      '+'订票数：'+str(i.Num_bookings)+'      '+'余票数: '+str(i.Num_rm_tickets))
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_37_clicked(self):
        self.textBrowser_6.setText('')

    @pyqtSlot()
    def on_pushButton_52_clicked(self):
        return 1

    @pyqtSlot()
    def on_pushButton_52_clicked(self):
        try:
            pad = flight(self.lineEdit_33.text(),'','','',0,0)
            if self.lineEdit_33.text()=='':
                QMessageBox.information(self,'error','请输入有效的航班号！')
            else:
                if pad.isexited():
                    pad_2 = flight(self.lineEdit_33.text(),self.lineEdit_35.text(),self.lineEdit_36.text(),self.lineEdit_34.text(),int(self.lineEdit_37.text()),int(self.lineEdit_38.text()))
                    pad.delete()
                    pad_2.add()
                    QMessageBox.information(self,'成功','修改航班信息成功！')
                    self.lineEdit_33.setText('')
                    self.lineEdit_35.setText('')
                    self.lineEdit_34.setText('')
                    self.lineEdit_36.setText('')
                    self.lineEdit_37.setText('')
                    self.lineEdit_38.setText('')
                else:
                    QMessageBox.information(self,'error','该航班号不存在！请重新输入！')
                    self.lineEdit_33.setText('')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))


    @pyqtSlot()
    def on_pushButton_53_clciked(self):
        self.lineEdit_33.setText('')
        self.lineEdit_35.setText('')
        self.lineEdit_34.setText('')
        self.lineEdit_36.setText('')
        self.lineEdit_37.setText('')
        self.lineEdit_38.setText('')

    @pyqtSlot()
    #定义登录栏操作员登录
    def on_actionc_triggered(self):
        try:
            worker = Window_worker()  # 定义对话框变量
            worker.exec_()  # 使对话框变量显示出来
            if worker.on_pushButton_clicked():
                self.menubar.setEnabled(False)
                self.frame.show()
                self.label.setEnabled(True)
                self.label.setText('欢迎！操作员 {}'.format(str(worker.get_zhanghao())))
                self.pushButton_2.setEnabled(True)
                self.tab_3.setEnabled(True)
                self.tab.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_4.setEnabled(False)
        except Exception as  e:
            QMessageBox.information(self, '错误', str(e))

    @pyqtSlot()
    def on_pushButton_54_clicked(self):
        try:
            pad = Booked(str(self.lineEdit_41.text()),int(self.lineEdit_63.text()),str(self.lineEdit_42.text()),str(self.lineEdit_40.text()),str(self.lineEdit_39.text()))
            if self.lineEdit_39.text()=='' or self.lineEdit_40=='' or self.lineEdit_41.text()=='' or self.lineEdit_42.text()=='' or self.lineEdit_63.text()=='':
                QMessageBox.information(self,'error','请输入正确的订票信息！')
                self.lineEdit_39.setText('')
                self.lineEdit_40.setText('')
                self.lineEdit_41.setText('')
                self.lineEdit_42.setText('')
                self.lineEdit_63.setText('')
            else:
                if pad.isexited_seat():
                    pad3 = flight(self.lineEdit_41.text(),'','','',0,0)
                    if pad3.isexited():
                        if pad3.ishave_tickets():
                            pad.add()
                            QMessageBox.information(self,'成功','订票成功！')
                            pad2 = flight(self.lineEdit_41.text(), '', '', '',0, 0)
                            pad2.okbook()
                            self.lineEdit_39.setText('')
                            self.lineEdit_40.setText('')
                            self.lineEdit_41.setText('')
                            self.lineEdit_42.setText('')
                            self.lineEdit_63.setText('')
                        else:
                            QMessageBox.information(self,'error','该航班号余票数为0！请重新订票！')
                            self.lineEdit_39.setText('')
                            self.lineEdit_40.setText('')
                            self.lineEdit_41.setText('')
                            self.lineEdit_42.setText('')
                            self.lineEdit_63.setText('')
                    else:
                        QMessageBox.information(self,'error','该航线不存在，请重新输入！')
                        self.lineEdit_39.setText('')
                        self.lineEdit_40.setText('')
                        self.lineEdit_41.setText('')
                        self.lineEdit_42.setText('')
                        self.lineEdit_63.setText('')
                else:
                    QMessageBox.information(self,'error','该航班的座位已被订走！请重新输入订票信息')
                    self.lineEdit_39.setText('')
                    self.lineEdit_40.setText('')
                    self.lineEdit_41.setText('')
                    self.lineEdit_42.setText('')
                    self.lineEdit_63.setText('')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_55_clicked(self):
        self.lineEdit_39.setText('')
        self.lineEdit_40.setText('')
        self.lineEdit_41.setText('')
        self.lineEdit_42.setText('')
        self.lineEdit_63.setText('')


    @pyqtSlot()
    def on_pushButton_55_clicked(self):
        self.lineEdit_43.setText('')
        self.lineEdit_46.setText('')
        self.lineEdit_45.setText('')
        self.lineEdit_44.setText('')
        self.lineEdit_47.setText('')

    @pyqtSlot()
    def on_pushButton_58_clicked(self):
        try:
            pad = Booked(str(self.lineEdit_49.text()),0,'',str(self.lineEdit_48.text()),str(self.lineEdit_50.text()))
            if self.lineEdit_49.text()!='' and self.lineEdit_48.text()!='' and self.lineEdit_50.text()!='':
                if pad.isexited_seat():
                    pad3 = flight(self.lineEdit_49.text(),'','','',0,0)
                    if pad3.isexited():
                        pad.delete()
                        QMessageBox.information(self, '成功', '退票成功！')
                        pad2 = flight(self.lineEdit_49, '', '', '', 0, 0)
                        pad2.cancelbook()
                        self.lineEdit_49.setText('')
                        self.lineEdit_48.setText('')
                        self.lineEdit_50.setText('')
                    else:
                        QMessageBox.information(self,'error','该航线不存在！请重新输入！')
                else:
                    QMessageBox.information(self, 'error', '该订票记录不存在，请重新输入！')
                    self.lineEdit_49.setText('')
                    self.lineEdit_48.setText('')
                    self.lineEdit_50.setText('')
            else:
                QMessageBox.information(self,'error','请输入有效的退票信息！')
                self.lineEdit_49.setText('')
                self.lineEdit_48.setText('')
                self.lineEdit_50.setText('')

        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_59_clicked(self):
        self.lineEdit_49.setText('')
        self.lineEdit_48.setText('')
        self.lineEdit_50.setText('')

    @pyqtSlot()
    def on_pushButton_60_clicked(self):
        try:
            pad = Booked(self.lineEdit_52.text(), 0, '', self.lineEdit_51.text(), self.lineEdit_53.text())
            if self.lineEdit_52.text() != '' and self.lineEdit_51.text() != '' and self.lineEdit_53.text() != '':
                if pad.isexited_seat():
                    pad3 = flight(self.lineEdit_52.text(), '', '', '', 0, 0)
                    if pad3.isexited():
                        pad.delete()
                        QMessageBox.information(self, '成功', '退票成功！')
                        pad2 = flight(self.lineEdit_52.text(), '', '', '', 0, 0)
                        pad2.cancelbook()
                        self.lineEdit_52.setText('')
                        self.lineEdit_51.setText('')
                        self.lineEdit_53.setText('')
                    else:
                        QMessageBox.information(self, 'error', '该航班信息不存在！请重新输入！')
                        self.lineEdit_52.setText('')
                        self.lineEdit_51.setText('')
                        self.lineEdit_53.setText('')
                else:
                    QMessageBox.information(self, 'error', '该订票记录不存在，请重新输入！')
                    self.lineEdit_52.setText('')
                    self.lineEdit_51.setText('')
                    self.lineEdit_53.setText('')

            else:
                QMessageBox.information(self, 'error', '请输入有效的退票信息！')
                self.lineEdit_52.setText('')
                self.lineEdit_51.setText('')
                self.lineEdit_53.setText('')

        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_61_clicked(self):
        self.lineEdit_52.setText('')
        self.lineEdit_51.setText('')
        self.lineEdit_53.setText('')

    @pyqtSlot()
    def on_pushButton_62_clicked(self):
        try:
            pad = Booked('',0,'',str(self.lineEdit_54.text()),str(self.lineEdit_56.text()))
            list = pad.show_peo()
            if self.lineEdit_54.text()!='' and self.lineEdit_56!='':
                if pad.isexited():
                    for i in list:
                        self.textBrowser_8.append('航班号： '+i.Flight_num+'    '+'座位号：'+str(i.Seat_num)+'   '+'飞机号：'+i.Aircraft_num+'   '+'姓名：'+i.name+'    '+'身份证号：'+i.id_num)
                        self.lineEdit_54.setText('')
                        self.lineEdit_56.setText('')
                else:
                    QMessageBox.information(self,'error','该用户无订票记录！请重新输入！')
                    self.lineEdit_54.setText('')
                    self.lineEdit_56.setText('')
            else:
                QMessageBox.information(self,'error','请输入有效的信息！')
                self.lineEdit_54.setText('')
                self.lineEdit_56.setText('')
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_63_clicked(self):
        self.lineEdit_54.setText('')
        self.lineEdit_56.setText('')

    @pyqtSlot()
    def on_pushButton_66_clicked(self):
        self.textBrowser_8.setText('')

    @pyqtSlot()
    def on_pushButton_64_clicked(self):
        try:
            pad = Booked('',0,'','','')
            list = pad.show_all()
            for i in list:
                self.textBrowser_7.append('航班号： '+i.Flight_num+'    '+'座位号：'+str(i.Seat_num)+'   '+'飞机号：'+i.Aircraft_num+'   '+'姓名：'+i.name+'    '+'身份证号：'+i.id_num)
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_65_clicked(self):
        self.textBrowser_7.setText('')

    @pyqtSlot()
    def on_pushButton_67_clicked(self):
        try:
            pad = flight(str(self.lineEdit_55.text()),'','','',0,0)
            if self.lineEdit_55.text()!='':
                if pad.isexited():
                    list = pad.show_except()
                    for i in list:
                        self.textBrowser_9.append('航班号：'+i.Flight_num+'     '+'飞机号: '+i.Aircraft_num+'    '+'出发地: '+i.Start+'     '+'目的地：'+i.Destination+'      '+'订票数：'+str(i.Num_bookings)+'      '+'余票数: '+str(i.Num_rm_tickets))
                else:
                    QMessageBox.information(self,'error','该航班不存在！请重新输入！')
                    self.lineEdit_55.setText('')
            else:
                QMessageBox.information(self,'error','请输入正确的航线信息！')
                self.lineEdit_55.setText('')
        except Exception as  e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_68_clicked(self):
        self.lineEdit_55.setText('')

    @pyqtSlot()
    def on_pushButton_69_clicked(self):
        self.textBrowser_9.setText('')

    @pyqtSlot()
    def on_pushButton_70_clicked(self):
        try:
            pad = flight('','','','',0,0)
            list = pad.show_all()
            for i in list:
                self.textBrowser_10.append('航班号：'+i.Flight_num+'     '+'飞机号: '+i.Aircraft_num+'    '+'出发地: '+i.Start+'     '+'目的地：'+i.Destination+'      '+'订票数：'+str(i.Num_bookings)+'      '+'余票数: '+str(i.Num_rm_tickets))
        except Exception as e:
            QMessageBox.information(self,'error',str(e))

    @pyqtSlot()
    def on_pushButton_71_clicked(self):
        self.textBrowser_10.setText('')

    @pyqtSlot()
    #定义登录栏普通用户登录
    def on_actiono_triggered(self):
        try:
            Orp = Window_OrP()  # 定义对话框变量
            Orp.exec_()  # 使对话框变量显示出来
            if Orp.on_pushButton_clicked():
                self.menubar.setEnabled(False)
                self.frame.show()
                self.label.setEnabled(True)
                self.label.setText('欢迎！普通用户 {}'.format(str(Orp.getname())))
                self.pushButton_2.setEnabled(True)
                self.tab_4.setEnabled(True)
                self.tab.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_3.setEnabled(False)
        except Exception as  e:
            QMessageBox.information(self, '错误', str(e))

    @pyqtSlot()
    def on_pushButton_72_clicked(self):
        try:
            pad = Booked(str(self.lineEdit_57.text()), int(self.lineEdit_59.text()), str(self.lineEdit_58.text()),
                         str(self.lineEdit_60.text()), str(self.lineEdit_8.text()))
            if self.lineEdit_57.text() == '' or self.lineEdit_59 == '' or self.lineEdit_58.text() == '' or self.lineEdit_60.text() == '' or self.lineEdit_8.text() == '':
                QMessageBox.information(self, 'error', '请输入正确的订票信息！')
                self.lineEdit_57.setText('')
                self.lineEdit_58.setText('')
                self.lineEdit_59.setText('')
                self.lineEdit_60.setText('')
                self.lineEdit_8.setText('')
            else:
                if pad.isexited_seat():
                    pad3 = flight(self.lineEdit_57.text(),'','','',0,0)
                    if pad3.isexited():
                        if pad3.ishave_tickets():
                            people = OrdinaryP(self.lineEdit_8.text(),self.lineEdit_60.text())
                            if people.isexited():
                                pad.add()
                                QMessageBox.information(self, '成功', '订票成功！')
                                pad2 = flight(self.lineEdit_57.text(), '', '', '', 0, 0)
                                pad2.okbook()
                                self.lineEdit_57.setText('')
                                self.lineEdit_58.setText('')
                                self.lineEdit_59.setText('')
                                self.lineEdit_60.setText('')
                                self.lineEdit_8.setText('')
                            else:
                                QMessageBox.information(self,'error','您的姓名与身份证号不匹配！请重新输入！')
                        else:
                            QMessageBox.information(self,'error','该航班无余票，请选择其它航班！')
                            self.lineEdit_57.setText('')
                            self.lineEdit_58.setText('')
                            self.lineEdit_59.setText('')
                            self.lineEdit_60.setText('')
                            self.lineEdit_8.setText('')
                    else:
                        QMessageBox.information(self,'error','该航线不存在！请重新输入！')
                        self.lineEdit_57.setText('')
                        self.lineEdit_58.setText('')
                        self.lineEdit_59.setText('')
                        self.lineEdit_60.setText('')
                        self.lineEdit_8.setText('')
                else:
                    QMessageBox.information(self, 'error', '该航班的座位已被订走！请重新输入订票信息')
                    self.lineEdit_57.setText('')
                    self.lineEdit_58.setText('')
                    self.lineEdit_59.setText('')
                    self.lineEdit_60.setText('')
                    self.lineEdit_8.setText('')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))
    @pyqtSlot()
    def on_pushButton_73_clicked(self):
        self.lineEdit_57.setText('')
        self.lineEdit_58.setText('')
        self.lineEdit_59.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_8.setText('')

    @pyqtSlot()
    def on_pushButton_75_clicked(self):
        try:
            pad = Booked(self.lineEdit_64.text(), 0, '', self.lineEdit_61.text(), '')
            if self.lineEdit_64.text() != '' and self.lineEdit_61.text() != '' :
                if pad.isexited_seat():
                    pad3 = flight(self.lineEdit_64.text(),'','','',0,0)
                    if pad3.isexited():
                        pad.delete()
                        QMessageBox.information(self, '成功', '退票成功！')
                        pad2 = flight(self.lineEdit_64.text(), '', '', '', '', '')
                        pad2.cancelbook()
                        self.lineEdit_61.setText('')
                        self.lineEdit_64.setText('')
                    else:
                        QMessageBox.information(self,'error','该航线不存在！请重新输入！')
                        self.lineEdit_61.setText('')
                        self.lineEdit_64.setText('')
                else:
                    QMessageBox.information(self, 'error', '该订票记录不存在，请重新输入！')
                    self.lineEdit_61.setText('')
                    self.lineEdit_64.setText('')
            else:
                QMessageBox.information(self, 'error', '请输入有效的退票信息！')
                self.lineEdit_61.setText('')
                self.lineEdit_64.setText('')

        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_74_clicked(self):
        self.lineEdit_61.setText('')
        self.lineEdit_64.setText('')

    @pyqtSlot()
    def on_pushButton_78_clicked(self):
        try:
            pad = flight(str(self.lineEdit_62.text()), '', '', '', 0, 0)
            if self.lineEdit_62.text() != '':
                if pad.isexited():
                    list = pad.show_except()
                    for i in list:
                        self.textBrowser_12.append(
                            '航班号：' + i.Flight_num + '     ' + '飞机号: ' + i.Aircraft_num + '    ' + '出发地: ' + i.Start + '     ' + '目的地：' + i.Destination + '      ' + '订票数：' + str(i.Num_bookings) + '      ' + '余票数: ' + str(i.Num_rm_tickets))
                else:
                    QMessageBox.information(self, 'error', '该航班不存在！请重新输入！')
                    self.lineEdit_62.setText('')
            else:
                QMessageBox.information(self, 'error', '请输入正确的航线信息！')
                self.lineEdit_62.setText('')
        except Exception as  e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_79_clicked(self):
        self.lineEdit_62.setText('')

    @pyqtSlot()
    def on_pushButton_80_clicked(self):
        self.textBrowser_12.setText('')

    @pyqtSlot()
    def on_pushButton_81_clicked(self):
        try:
            pad = flight('', '', '', '', 0, 0)
            list = pad.show_all()
            for i in list:
                self.textBrowser_13.append(
                    '航班号：' + i.Flight_num + '     ' + '飞机号: ' + i.Aircraft_num + '    ' + '出发地: ' + i.Start + '     ' + '目的地：' + i.Destination + '      ' + '订票数：' + str(i.Num_bookings) + '      ' + '余票数: ' + str(i.Num_rm_tickets))
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_82_clicked(self):
        self.textBrowser_13.setText('')

    @pyqtSlot()
    def on_pushButton_76_clicked(self):
        try:
            pad = Booked('', 0, '', str(self.lineEdit_10.text()), str(self.lineEdit_9.text()))
            list = pad.show_peo()
            if pad.isexited():
                for i in list:
                    self.textBrowser_11.append(
                        '航班号： ' + i.Flight_num + '    ' + '座位号：' + str(i.Seat_num) + '   ' + '飞机号：' + i.Aircraft_num + '   ' + '姓名：' + i.name + '    ' + '身份证号：' + i.id_num)
                    self.lineEdit_9.setText('')
                    self.lineEdit_10.setText('')
            else:
                QMessageBox.information(self,'error','该用户不存在订票记录')
                self.lineEdit_9.setText('')
                self.lineEdit_10.setText('')
        except Exception as e:
            QMessageBox.information(self, 'error', str(e))

    @pyqtSlot()
    def on_pushButton_77_clicked(self):
        self.textBrowser_11.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')

    @pyqtSlot()
    #定义登录栏VIP用户登录
    def on_actionvip_triggered(self):
        try:
            VIP = Window_VIP()  # 定义对话框变量
            VIP.exec_()  # 使对话框变量显示出来
            if VIP.on_pushButton_clicked():
                self.menubar.setEnabled(False)
                self.frame.show()
                self.label.setEnabled(True)
                self.label.setText('欢迎！VIP用户 {}'.format(str(VIP.getname())))
                self.pushButton_2.setEnabled(True)
                self.tab_4.setEnabled(True)
                self.tab.setEnabled(False)
                self.tab_2.setEnabled(False)
                self.tab_3.setEnabled(False)
        except Exception as  e:
            QMessageBox.information(self, '错误', str(e))

    @pyqtSlot()
    #定义帮助栏帮助被点击时触发的函数
    def on_actionbangzhu_triggered(self):
        QMessageBox.information(self,'帮助','使用航空订票系统前请先登录！\n有任何错误信息请联系邮箱:1294844426@qq.com\n注册使用的是中国公民身份证号')

    @pyqtSlot()
    #定义关于栏关于被点击时触发的函数
    def on_actionguanyu_triggered(self):
        QMessageBox.information(self,'关于','由James制作，联系邮箱:1294844426@qq.com,电子科技大学计科5班')

    @pyqtSlot()
    #定义建议栏建议被点击时触发的函数
    def on_actionjianyi_triggered(self):
        QMessageBox.information(self,'建议','VIP用户的测试邀请码为1314520')




if __name__=='__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap('.\img\spalsh.jpeg'))#设置启动界面，传进图片
    splash.show()#显示启动界面
    splash.showMessage('正在进入航空管理系统',Qt.AlignHCenter)#使文字显示在图片中央
    app.processEvents()
    ui = Window_one()
    ui.show()
    splash.close()#关闭启动界面
    sys.exit(app.exec_())#系统退出
