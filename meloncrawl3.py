conn = pymysql.connect(
    host='localhost',
    user='dooo',
    password='dooo!',
    port=3306,
    db='dooodb',
    charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, tel, email, birth, addr) values(%s,%s,%s,%s,%s)"
    cur.executemany(sql, data)
    print("AffecedRowCount is", cur.rowcount)
    conn.commit()