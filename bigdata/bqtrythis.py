import pymysql
from pprint import pprint
import bigquery
# client = bigquery.get_client(json_key_file='Bigquery.json', readonly=False)



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

# pprint(rows)


with conn:
    acur = conn.cursor()
    asql = "select * from Album"

    acur.execute(asql)
    arows = acur.fetchall()

dic = {}
adic = {}
slist = []
alist = []

# if not client.check_table(DATABASE, TABLE):
#     print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

#     client.create_table(DATABASE, TABLE, [
#             {'name': 'song_no', 'type': 'integer', 'description': 'song id'},
#             {'name': 'title', 'type': 'string', 'description': 'song title'},
#             {'name': 'genre', 'type': 'string', 'description': 'genre'},
#             {'name': 'album', 'type': 'record', 'description': 'album info',
#             'fields': [ {'name': 'album_id', 'type': 'string'},
#                         {'name': 'album_title', 'type': 'string'},
#                         {'name': 'album_genre', 'type': 'string'},
#                         {'name': 'rating', 'type': 'integer'},
#                         {'name': 'releasedt', 'type': 'string'}]
#             },
#         ])


for i in arows:
    adic[i[0]] = {'album_id': i[0], 'album_title': i[1], 'album_genre': i[2], 'rating': i[3] , 'releasedt': i[4]}
    alist.append(adic)
# pprint(alist)

for r in rows:
    dic[r[0]] = {'song_no': r[0], 'title': r[1], 'genre': r[2], 'album': r[3]}
    # if r[3] == adic['album_id']:
    #     r[3] = adic
    slist.append(dic)
# pprint(slist)


for _id, _info in dic.items():
    for key, val in arows.items():
        if _info['album'] == key:
            
        


# try:
#     pushResult = client.push_rows(DATABASE, TABLE, slist, insert_id_key='songno')
#     # client._raise_executing_exception_if_error(pushResult)
#     # client._raise_insert_exception_if_error(client.job)
# except Exception as err:
#     print(pushResult, err)

# print("Pushed Result is", pushResult)