print("Te'st 汪俊 \u4e2d\u6587");
val1=["A","无"]
print(val1.pop())
val2 = ("edd","eeee")
print(val2)

import mysql.connector

conn = mysql.connector.connect(user='root', password='111qqq!!!',
                              host='106.12.24.68',
                              database='wangjun')
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into t1 (V1) values (%s)', ['Michael'])
cursor.rowcount
conn.commit()
cursor.execute('select * from t1' )
val3 = cursor.fetchall()
print(val3)
conn.close()