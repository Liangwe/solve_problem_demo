import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8')
cursor = conn.cursor()
try:
    # 开始建库
    cursor.execute("create database test character set utf8;")
except pymysql.err.ProgrammingError:
    print("数据库已存在")
# 使用库
cursor.execute("use test;")
# 建表
try:
    cursor.execute("create table coupon(id int primary key auto_increment,val varchar(255))")
    print("完成表的创建")
except pymysql.err.InternalError:
    print("表已存在")

insert_sql = "insert into coupon(val) values (%s)"

with open("../0001_生成优惠券/Coupon.txt", 'r', encoding='utf-8') as f:
    fp = f.readlines()
error = []
print("开始插入数据")
for i in fp:
    try:
        if i.replace('\n','') != '':
            cursor.execute(insert_sql,i.replace('\n',''))
            conn.commit()
        else:
            pass
    except Exception as e:
        conn.rollback()
        print(e)
        error.append(i)
print(error)

conn.close()