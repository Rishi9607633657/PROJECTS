import mysql.connector
con=mysql.connector.connect(host='localhost',
                        username='root',
                        password='rishi@123',
                        database='blogproject')

if con:
    print("connection established")
#CREATE CURSOR OBJECT  
c1=con.cursor()

def create_table():
    c1.execute("create table if not exists blogtable(title text,author text,article text ,post_date date,image blob) ")
    
def addpost(a,b,c,d,e):
    c1.execute("insert into blogtable(title,author,article,post_date,image) values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
    con.commit()
def view_records():
    c1.execute("select * from blogtable")
    data=c1.fetchall()
    return data
def get_title(x):
    c1.execute("select * from blogtable where title ='{}'".format(x))
    data=c1.fetchall()
    return data
def get_author(x):
    c1.execute("select * from blogtable where author = '{}'".format(x))
    data=c1.fetchall()
    return data
def delete_data(author):
    c1.execute("delete from blogtable where author='{}'".format(author))
    con.commit()