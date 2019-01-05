import mig_util as mu


oraconn = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dooodb')


with oraconn :
   cursor_e = oraconn.cursor()

   oracle_e = ''' select EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, NVL(SALARY,0), round(COMMISSION_PCT *100), NVL(MANAGER_ID, 0), NVL(DEPARTMENT_ID,0) from EMPLOYEES'''

   cursor_e.execute(oracle_e)

   rows_e = cursor_e.fetchall()

for row_e in rows_e:
   print(row_e)


with myconn :
   cur_e = myconn.cursor()
   cur_e.execute("drop table if exists Employees")

   sql_e = ''' create table Employees (
	   				id int unsigned not null primary key default '0', 
					first_name varchar(20),
					last_name varchar(25) not null,
					email varchar(25) not null unique, 
					phone_number varchar(20),
					hire_date date not null, 
					job_id varchar(10) not null,
					salary int(10) unsigned not null default '0', 
					commission_pct int(10) unsigned not null default '0', 
					manager_id varchar(10) not null, 
					department_id int(10) unsigned not null default '0'
               )
         '''

   cur_e.execute(sql_e)

   sql_insert_e = "insert into Employees(id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) values(%s, %s, %s, %s, %s, %s, %s, %s, ifnull(%s, 0), %s, %s)"
   cur_e.executemany(sql_insert_e, rows_e)

   print( "affectedrowcount for Employees", cur_e.rowcount)