from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

My_databases = "mysql+pymysql://root:123456@localhost:3306/ams?charset=utf8mb4"
engine = create_engine(My_databases)#连接数据库，创建数据库引擎变量

Session = sessionmaker(bind=engine)#引用上面的eigne，将事务session与数据库绑定

Base = declarative_base()#继承导入的模块,创建对象的基类

class Booked(Base):
    #定义已经订票的信息表
    __tablename__='alresdy_booked'
    Flight_num = Column(CHAR(30),nullable=False,primary_key=True,comment='航班号')
    Seat_num = Column(BigInteger,nullable=False,comment='座位号',primary_key=True)
    Aircraft_num = Column(CHAR(30),nullable=False,comment='飞机号')
    id_num = Column(CHAR(20),nullable=True,comment='已订票用户身份证号')
    name = Column(CHAR(20),nullable=True,comment='已订票用户姓名')

    def __init__(self,Flight_num,Seat_num,Aircraft_num,id_num,name):
        self.Flight_num = Flight_num
        self.Aircraft_num =Aircraft_num
        self.Seat_num = Seat_num
        self.id_num = id_num
        self.name = name

    #添加订票信息
    def add(self):
        session = Session()  # 定义事务
        try:
            session.add(self)  # 事务增加数据
            session.commit()  # 提交事务,session自动过期而不需要关闭
        except Exception as e:
            session.rollback()  # 发生异常后回滚事务
            print('错误' + str(e))

    #根据航班号和身份证号删除订票信息
    def delete(self):
        session = Session()
        try:
            session.query(Booked).filter_by(Flight_num=self.Flight_num,id_num=self.id_num).delete()
            # 调用事务删除指定航班号和身份证号的订票信息
            session.commit()
        except Exception as e:
            session.rollback()
            print('错误' + str(e))


    #根据用户姓名和身份证号查询指定用户的订票信息
    def show_peo(self):
        session = Session()
        try:
            list = session.query(Booked).filter_by(id_num=self.id_num,name=self.name).all()
            return list
        except Exception as e:
            session.rollback()
            print('错误'+str(e))
    #根据用户提供的航班号和座位号来查询是否有座位，返回BOOL值
    def isexited_seat(self):
        session = Session()
        seat = session.query(Booked).filter_by(Flight_num=self.Flight_num,Seat_num = self.Seat_num).first()
        if seat is None:
            return 1
        else:
            return 0

    #显示所有订票信息
    def show_all(self):
        session = Session()
        try:
            list =session.query(Booked).filter().all()
            return list
        except Exception as e:
            session.rollback()
            print(str(e))

    #根据用户姓名和身份证号查询是否有过订票记录
    def isexited(self):
        session  = Session()
        try:
            list = session.query(Booked).filter_by(id_num = self.id_num,name=self.name).first()
            if list is not None:
                return 1
            else:
                return 0
        except Exception as e:
            session.rollback()
            print(str(e))

