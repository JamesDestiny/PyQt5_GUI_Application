from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

My_databases = "mysql+pymysql://root:123456@localhost:3306/ams?charset=utf8mb4"
engine = create_engine(My_databases)#连接数据库，创建数据库引擎变量

Session = sessionmaker(bind=engine)#引用上面的eigne，将事务session与数据库绑定

Base = declarative_base()#继承导入的模块,创建对象的基类

#定义航班信息类
class flight(Base):
    __tablename__ ='flight_info'#定义表名
    Flight_num = Column(VARCHAR(30),nullable=False,primary_key=True,comment='航班号',unique=True)
    Aircraft_num = Column(VARCHAR(30),nullable=False,comment='飞机号')
    Destination = Column(VARCHAR(30),nullable=False,comment='目的地')
    Start = Column(VARCHAR(30),nullable=False,comment='出发地')
    Num_bookings = Column(INTEGER,nullable=False,comment='订票数')
    Num_rm_tickets = Column(INTEGER,nullable=False,comment='余票数')

    def __init__(self,Flight_num,Aircraft_num,Start,Destination,Num_bookings,Num_rm_tickets):
        self.Flight_num = Flight_num#定义航班号
        self.Aircraft_num = Aircraft_num#定义飞机号
        self.Destination = Destination#定义目的地
        self.Num_bookings = Num_bookings#定义订票数
        self.Num_rm_tickets = Num_rm_tickets#定义余票数
        self.Start = Start#定义出发地

    #添加航班信息函数
    def add(self):
        session = Session()  # 定义事务
        try:
            session.add(self)#事务增加数据
            session.commit()#提交事务,session自动过期而不需要关闭
        except Exception as e:
            session.rollback()#发生异常后回滚事务
            print('错误'+str(e))

    #根据航班号删除航班信息
    def delete(self):
        session = Session()
        try:
            session.query(flight).filter_by(Flight_num=self.Flight_num).delete()
            #调用事务删除指定管理员用户名的数据库数据
            session.commit()
        except Exception as e:
            session.rollback()
            print('错误'+str(e))

    #输出所有的航班信息
    def show_all(self):
        session =Session()
        try:
            list = session.query(flight).filter_by().all()
            return list
        except Exception as e:
            session.rollback()
            print(str(e))
    #根据用户输入的航班号来输出除该航班号的其它所有航班信息
    def show_except(self):
        session = Session()
        try:
            list = session.query(flight).filter_by(Flight_num=self.Flight_num).all()
            return list
        except Exception as e:
            session.rollback()
            print(str(e))

    #根据航班号判断是否有余票，返回BOOL值类型
    def ishave_tickets(self):
        session =Session()
        try:
            ticket = session.query(flight).filter_by(Flight_num=self.Flight_num,Num_rm_tickets =0).first()
            if ticket is None:
                return 1
            else:
                return 0
        except Exception as e:
            session.rollback()
            print(str(e))

    #客户订票成功后，根据航班号让该航班的订票数加一，余票数减一
    def okbook(self):
        session = Session()
        try:
            ok = session.query(flight).filter_by(Flight_num=self.Flight_num).first()
            ok.Num_bookings += 1
            ok.Num_rm_tickets -=1
            session.commit()
        except Exception as e:
            print(str(e))

    #客户退票成功后，根据航班号让该航班的订票数减一，余票数加一
    def cancelbook(self):
        session = Session()
        try:
            ok = session.query(flight).filter_by(Flight_num=self.Flight_num).first()
            ok.Num_bookings -= 1
            ok.Num_rm_tickets += 1
            session.commit()
        except Exception as e:
            print(str(e))

    #当用户输入航班号时，根据航班号判断该航班号是否存在
    def isexited(self):
        session = Session()
        try:
            Fl = session.query(flight).filter_by(Flight_num=self.Flight_num).first()
            if Fl is not None:
                return 1
            else:
                return 0

        except Exception as e:
            session.rollback()
            print(str(e))



#以下为测试模块
'''
try:
    pad = flight('','','','','','')
    list=pad.show_all()
    for i in list:
        print(i.Flight_num)
except Exception as e:
        print(str(e))
'''
