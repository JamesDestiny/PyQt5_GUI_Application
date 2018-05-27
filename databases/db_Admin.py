import sqlalchemy#导入数据库处理ORM映射函数类
from sqlalchemy import *#导入生成引擎的类来连接数据库
from sqlalchemy.orm import sessionmaker#导入生成事务的类，通过传输代替数据库的引擎
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

from sqlalchemy.orm import mapper#导入映射方法，可以将已经存在的表映射到类中

My_databases = "mysql+pymysql://root:123456@localhost:3306/ams?charset=utf8mb4"
engine = create_engine(My_databases)#连接数据库，创建数据库引擎变量

Session = sessionmaker(bind=engine)#引用上面的eigne，将事务session与数据库绑定

Base = declarative_base()#继承导入的模块,创建对象的基类

#建立管理员类
class admin(Base):
    #定义类,定义表
    __tablename__ ='admin_info'
    admin_id = Column(INTEGER,primary_key=True,autoincrement=True,nullable=False,comment='管理员编号',unique=True)
    admin_user = Column(CHAR(20),primary_key=True,nullable=False,comment='管理员账号',unique=True)
    admin_pd = Column(CHAR(20),nullable=False,comment='管理员密码')
    def __init__(self,admin_user,admin_pd):
        self.admin_user = admin_user#定义管理员用户名
        self.admin_pd = admin_pd#定义管理员密码


    #添加管理员,插入到数据库中
    def add(self):
        session = Session()  # 定义事务
        try:
            session.add(self)#事务增加数据
            session.commit()#提交事务,session自动过期而不需要关闭
        except Exception as e:
            session.rollback()#发生异常后回滚事务
            print('错误'+str(e))


    #根据管理员用户名删除管理员，从数据库中删除
    def delete(self):
        session = Session()
        try:
            session.query(admin).filter_by(admin_user=self.admin_user).delete()
            #调用事务删除指定管理员用户名的数据库数据
            session.commit()
        except Exception as e:
            session.rollback()
            print('错误'+str(e))

    #根据管理员用户名和密码判断是否成功登录
    def isExited(self):
        session =Session()
        try:
            ad=session.query(admin).filter_by(admin_user=self.admin_user,admin_pd=self.admin_pd).first()
            session.commit()
            if ad is not None:
                return 1
            else:
                return 0
        except Exception as e:
            print('错误' + str(e))

    def isLogin(self):
        session = Session()
        try:
            ad = session.query(admin).filter_by(admin_user=self.admin_user).first()
            session.commit()
            if ad is not None:
                return 1
            else:
                return 0
        except Exception as e:
            print('错误' + str(e))

    # 输出所有的管理员信息
    def show_all(self):
        session = Session()
        try:
            list = session.query(admin).filter_by().all()
            return list
        except Exception as e:
            session.rollback()
            print(str(e))

'''
pad = admin('','')
list = pad.show_all()
for i in list:
    print(i.admin_user)
'''
