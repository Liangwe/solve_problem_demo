import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
try:
    cursor.execute("create table coupon(id int primary key ,val varchar(255))")
    print("完成表的创建")
except sqlite3.OperationalError:
    print("表已存在")

insert_sql = "insert into coupon(id,val) values(?,?)"
with open("../0001/Coupon.txt" , 'r',encoding='utf-8') as f:
    fp = f.readlines()
error = []
print("开始插入数据")
for i in range(len(fp)):
    try:
        if fp[i].replace('\n','') != '':
            cursor.execute(insert_sql,(i+1,fp[i].replace('\n','')))
            conn.commit()
        else:
            pass
    except Exception as e:
        conn.rollback()
        print(e)
        error.append(i)
print(error)

conn.close()