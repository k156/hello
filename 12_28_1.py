import mig_util as mu

connection = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dooodb')

with connection:
    cursor = connection.cursor()

    sql = '''select job_id, job_title, min_salary, max_salary from Jobs'''
    cursor.execute(sql)
    rows = cursor.fetchall()

for row in rows:
    print(row)

with myconn:
    cur = myconn.cursor()
    cur.execute("drop table if exists Jobs")
	#프로시저 만들 수 있으면 만들기.

    sql_create = '''
        create table Jobs(
            id varchar(10) not null primary key,
            job_title varchar(35),
			min_salary int(11),
			max_salary int(11)
        )
    '''
    cur.execute(sql_create)

    sql_insert = "insert into Regions(id, job_title, min_salary, max_salary) values(%s, %s, %s, %s)"
    cur.executemany(sql_insert, rows)
    print("AffectedRowCount is", cur.rowcount)
