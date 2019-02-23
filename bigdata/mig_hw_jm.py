import pymysql

def get_conn_hw(db):
    return pymysql.connect(
        host='34.85.92.216',
        user='root',
        password='gusdnr75',
        port=3306,
        db=db,
        charset='utf8')

def get_conn_jm(db):
    return pymysql.connect(
        host='35.243.74.84',
        user='root',
        password='1234567',
        port=3306,
        db=db,
        charset='utf8')


hw = get_conn_hw('melondb')
jm = get_conn_jm('melondb')

with hw:
    cur = hw.cursor()
    # sql1 = "select album_id, album_title, album_genre, rating, releasedt from Album"
    sql2 = 'select song_no, title, genre, album_id from MS_Song'

    cur.execute(sql2)
    rows = cur.fetchall()

for row in rows:
    print(row)


with jm:
    cur = jm.cursor()

    # sql1 = '''insert into Album(album_id, album_title, album_genre, rating, releasedt)
    #                       values(%s, %s, %s, %s, %s)'''
    sql2 = '''insert into Song(song_no, title, genre, album_id)
                          values(%s, %s, %s, %s)'''
    cur.executemany(sql2, rows)
    print("AffecedRowCount is", cur.rowcount)
    jm.commit()
    print("Done")





