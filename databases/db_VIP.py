from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

My_databases = "mysql+pymysql://root:123456@localhost:3306/ams?charset=utf8mb4"
engine = create_engine(My_databases)#连接数据库，创建数据库引擎变量

Session = sessionmaker(bind=engine)#引用上面的eigne，将事务session与数据库绑定

Base = declarative_base()#继承导入的模块,创建对象的基类

#定义普通客户信息的类
class VIP(Base):
    __tablename__ = 'VIP_info'
    VIP_id = Column(INTEGER,nullable=False,autoincrement=True,primary_key=True,comment='VIP用户编号')
    VIP_name = Column(VARCHAR(20),nullable=False,comment='VIP用户姓名')
    VIP_id_num = Column(VARCHAR(20),nullable=False,primary_key=True,comment='VIP用户身份证号')

    def __init__(self,VIP_name,VIP_id_num):
        self.VIP_name = VIP_name
        self.VIP_id_num = VIP_id_num

    #添加用户信息，即用户注册
    def add(self):
        session = Session()  # 定义事务
        try:
            session.add(self)#事务增加数据
            session.commit()#提交事务,session自动过期而不需要关闭
        except Exception as e:
            session.rollback()#发生异常后回滚事务
            print('错误'+str(e))

    #根据用户姓名和身份证号删除用户信息
    def delete(self):
        session = Session()
        try:
            session.query(VIP).filter_by(VIP_name=self.P_name,VIP_id_num=self.P_id_num).delete()
            # 调用事务删除指定身份证号和姓名的用户信息
            session.commit()
        except Exception as e:
            session.rollback()
            print('错误' + str(e))

    #根据身份证号码和姓名判断用户是否存在,返回BOOL类型的值
    def isexited(self):
        session = Session()
        try:
            peo = session.query(VIP).filter_by(P_name=self.P_name, P_id_num=self.P_id_num).first()
            if peo is not None:
                return 1
            else:
                return 0
        except Exception as e:
            session.rollback()
            print(str(e))


