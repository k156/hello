import pymysql

def get_conn(db):
    return pymysql.connect(
        host='35.243.74.84',
        user='root',
        password='1234567',
        port=3306,
        db=db,
        charset='utf8')

conn = get_conn('melondb')


with conn:
    cur = conn.cursor()
    sql = "select * from Song"

    cur.execute(sql)
    rows = cur.fetchall()

print(rows)