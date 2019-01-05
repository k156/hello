import mysqldata2 as mu


oraconn = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dooodb')


with oraconn :
   cursor_j = oraconn.cursor()

   oracle_j = ''' select JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY from JOBS '''

   cursor.execute(oracle_j)

   rows_j = cursor.fetchall()

for row_j in rows_j:
   print(row_j)


with myconn :
   cur_j = myconn.cursor()
   cur_j.execute("drop table if exists Jobs")

   sql_j = ''' create table Jobs (
                   id varchar(10) not null primary key default '',
                   job_title varchar(35) not null default '',
                   min_salary int default 0,
                   max_salary int default 0
               )
         '''

   cur.execute(sql_j)

   sql_insert_j = "insert into Jobs(id, JOB_TITLE, MIN_SALARY, MAX_SALARY) values(%s, %s, %s, %s)"
   cur.executemany(sql_insert_j, rows_j)

   print( "affectedrowcount for Jobs", cur.rowcount)