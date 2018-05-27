from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

My_databases = "mysql+pymysql://root:123456@localhost:3306/ams?charset=utf8mb4"
engine = create_engine(My_databases)#连接数据库，创建数据库引擎变量

Session = sessionmaker(bind=engine)#引用上面的eigne，将事务session与数据库绑定

Base = declarative_base()#继承导入的模块,创建对象的基类

#定义工作人员，即操作员的类
class Worker(Base):
    __tablename__ = 'worker_info'
    worker_id = Column(INTEGER,nullable=False,autoincrement=True,comment='工作员编号',primary_key=True)
    worker_user = Column(CHAR(20),nullable=False,primary_key=True,comment='工作员账号')
    worker_pd = Column(CHAR(20),nullable=False,comment='工作员密码')

    def __init__(self,worker_user,worker_pd,):
        self.worker_user = worker_user
        self.worker_pd =worker_pd

    #添加工作员信息
    def add(self):
        session = Session()  # 定义事务
        try:
            session.add(self)  # 事务增加数据
            session.commit()  # 提交事务,session自动过期而不需要关闭
        except Exception as e:
            session.rollback()  # 发生异常后回滚事务
            print('错误' + str(e))

    #根据工作员账号删除工作员信息
    def delete(self):
        session = Session()
        try:
            session.query(Worker).filter_by(worker_user=self.worker_user).delete()
            #调用事务删除指定账号的工作员
            session.commit()
        except Exception as e:
            session.rollback()
            print('错误'+str(e))

    #判断工作人员是否存在
    def isExited(self):
        session = Session()
        try:
            peo = session.query(Worker).filter_by(worker_user=self.worker_user,worker_pd = self.worker_pd).first()
            if peo is not None:
                return 1
            else:
                return 0
        except Exception as e:
            session.rollback()
            print(str(e))

    def isLogin(self):
        session = Session()
        try:
            ad = session.query(Worker).filter_by(worker_user=self.worker_user).first()
            session.commit()
            if ad is not None:
                return 1
            else:
                return 0
        except Exception as e:
            print('错误' + str(e))

    # 输出所有的操作员信息
    def show_all(self):
        session = Session()
        try:
            list = session.query(Worker).filter_by().all()
            return list
        except Exception as e:
            session.rollback()
            print(str(e))
