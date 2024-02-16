import pymysql

conn = pymysql.connect(host = '13.124.144.111', user = 'usrid', password = 'usrpassword', db = 'cafemenu', charset = 'utf8')

cur = conn.cursor()

def make_newmenu(name, price):
    sql = "INSERT INTO menu (menuname, price) VALUE ('%s','%s');"%(name, price)
    cur.execute(sql)
    conn.commit()
    print("%s - %s원이 추가되었습니다."%(name, price))  

def delete_menu(name, id):
    sql = "DELETE FROM menu WHERE id = '%s';" %(id)
    cur.execute(sql)
    conn.commit()
    print("%s가 삭제되었습니다."%(name))

def update_menu(id, name, price):
    sql = "UPDATE menu SET menuname = '%s', price = '%s' WHERE Id = '%s'"%(name, price, id)
    cur.execute(sql)
    conn.commit()
    print("%s - %s원으로 수정되었습니다."%(name, price))

def list_menu():
  sql = "SELECT * FROM menu" 
  cur.execute(sql)
  b = list()
  for row in cur:
    a=list()
    a.append(row[0])
    a.append(row[1])
    a.append(row[2])
    b.append(a)
  return b
