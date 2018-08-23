'''
conn = pymysql.connect(host='127.0.0.1',port=3306,user = 'root',passwd = 'lxs19951017',db = 'lxs')
# curssor = conn.cursor()   #定义游标，默认元组形式
curssor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #设为字典形式
curssor.execute(sql)  执行语句
fetchone() 取一条数据
fetchmany() 取多条数据 ,参数为条数
fetchall()  取全部

scroll  光标移动
scroll(+-1,mode = 'relative)  1为向下移动一位，-1为向上移动一位
scroll(1,mode = 'absolute) 将光标固定到1

cursor.lastrowid  得到上一条插入数据的自增id

事务：
    start transaction   开启事务
    Rollback  撤销
    Commit   提交，增加删除修改操作必须

    savepoint 保留点

SQL注入：
        xxx' or 1=1 --
        select * from test where id='%s' and name='%s'
        select * from test where id='xxx' or 1=1 -- and name=%s
        --为sql的注释，即前边1=1位真，后边需要密码被注释，可任意登录

'''
#
# import pymysql
#
#
# conn = pymysql.connect(host='127.0.0.1',port=3306,user = 'root',passwd = 'lxs19951017',db = 'lxs')
#
# # curssor = conn.cursor()   #定义游标，默认元组形式
# curssor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #设为字典形式
#
#
# # sql = 'create table test(id int ,name varchar(20))'
# # curssor.execute(sql)         #调用
#
# #sql = 'INSERT INTO test VALUES (2,"e"),(3,"v"),(4,"n")'
#
# sql = 'select * from test'
# RET = curssor.execute(sql)
# print(RET)   #结果为行数
#
# # print(curssor.fetchone())
# # print(curssor.fetchmany(3))
# print(curssor.fetchall())
#
#
# conn.commit()   #提交
# curssor.close()
# conn.close()



#
# import pymysql
#
#
# conn = pymysql.connect(host='127.0.0.1',port=3306,user = 'root',passwd = 'lxs19951017',db = 'lxs')
#
#
# curssor = conn.cursor()
#
# user = input('username:')
# pwd = input('password:')
#
#
# # sql = "select * from test where id=%s and name=%s "
# # args = [user,pwd]
# # curssor.execute(sql,args)   #execute会自动进行拼接
# # curssor.execute(sql,[user,pwd])   #execute会自动进行拼接
#
#
# sql = "select * from test where id=%(u)s and name=%(p)s "
# curssor.execute(sql,{'u':user,'p':pwd})   #execute会自动进行拼接
#
#
#
# RET = curssor.fetchone()
# curssor.close()
# conn.close()
#
# if RET:
#     print('登陆成功！')
# else:
#     print('失败！！！')


import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user = 'root',passwd = 'lxs19951017',db = 'lxs')

curssor = conn.cursor()

sql = "insert into test values (%s,%s)"
curssor.executemany(sql,[('5','dsf'),('6','pcew')])  #插入多条

conn.commit()   #增删改操作必须
curssor.close()
conn.close()

