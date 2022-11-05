from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'mysql+pymysql://root:zxcv1234@localhost:3306/data'
# data is schema name!
engine = create_engine(database_url, echo=True, )
# connect database
# echo 引數為 True 時，會顯示每條執行的 SQL 語句，生產環境下可關閉。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
# Later we will inherit from this class to create each of the database models or classes (the ORM models):
