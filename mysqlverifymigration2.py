import pymysql

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')


conn_dooodb = get_conn('dooodb')
conn_dadb = get_conn('dadb')

with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select count(*) from Subject"

    cur.execute(sql)
    cnt_dooo = cur.fetchone()[0]

with conn_dadb:
    cur =  conn_dadb.cursor()
    sql = "select count(*) from Subject"

    cur.execute(sql)
    cnt_dadb = cur.fetchone()[0]






with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject order by rand() limit 5"

    cur.execute(sql)
    dooo_id = cur.fetchall()[0]
    verify_dooo = cur.fetchall()

with conn_dadb:
    cur =  conn_dadb.cursor()
    sql = "select id, name, prof, classroom from Subject where id < 5"

    cur.execute(sql)
    verify_dadb = cur.fetchall()


verify_dooo[1], verify_dooo[2], verify_dooo[3], verify_dooo[4], verify_dooo[5]


if cnt_dooo == cnt_dadb:
    print("데이터의 개수가 일치합니다.")
    
    if verify_dooo == verify_dadb:
        print("샘플 데이터가 일치합니다.")
    else:
        print("샘플 데이터가 일치하지 않습니다.")

else:
    print("데이터의 개수가 일치하지 않습니다.")