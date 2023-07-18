import pandas as pd
import pymysql
from sqlalchemy import create_engine
def database_creat():
    # 创建数据库连接
    conn = create_engine('mysql+pymysql://root:Wust#cs2023@localhost:3306/bigscreen')
    df = pd.read_csv('movie250.csv')
    # 将csv内容写新创建的表t_film
    df.to_sql(name='t_film', con=conn, chunksize=1000, if_exists='replace', index=None)
    # 测试创建的数据库
    sql = '''select * from t_film'''
    data = pd.read_sql(sql, conn)
    # print(data)
    print('存入到表')
