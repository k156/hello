import mig_util as mu

oraconn = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dooodb')
table = 'DEPARTMENTS'
cols = " DEPARTMENT_ID, DEPARTMENT_NAME, nvl(MANAGER_ID, 0)"
rand_row_count = 0

with oraconn :
	ora_cnt = mu.get_count(oraconn, table)

	cur = oraconn.cursor()
	sql = "SELECT * FROM (SELECT " + cols + " FROM " + table + " ORDER BY DBMS_RANDOM.RANDOM) WHERE rownum <= 10"
	cur.execute(sql)
	ora_list = cur.fetchall()
	rand_row_count = cur.rowcount
	



with myconn :

    my_cnt = mu.get_count(myconn , "Departments")

    print("이관된 oracle 레코드수", ora_cnt, ", 이관된 mysql 레코드 수 =", my_cnt)
    if ora_cnt != my_cnt:
        print("레코드 수가 일치하지 않습니다! oracle=", ora_cnt, ", mysql =", my_cnt)
        exit()

    else:
        print("레코드 수가 일치합니다.")
        cur = myconn.cursor()

        sql = '''select id, department_name, manager_id
                   from Departments
                  where id = %s
                    and department_name = %s
                    and manager_id = ifnull(%s, 0)
                  '''
        cur.executemany(sql, ora_list)
        curcnt = cur.rowcount
	
	
        if rand_row_count == curcnt:
            print("데이터 샘플이 일치합니다", "샘플 레코드 개수는", rand_row_count)

        else:
            print("실패. oracle에서 읽힌 레코드와 mysql에서 읽힌 레코드의 개수는 각각 다음과 같습니다",
                  rand_row_count, curcnt)