import mig_util as mu

oraconn = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dooodb')
table = 'JOBS'
cols = "JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY"
rand_row_count = 0


with oraconn:
	ora_cnt = mu.get_count(oraconn, table)

	cur = oraconn.cursor()
	sql = "SELECT * FROM (SELECT " + cols + " FROM " + table + " ORDER BY DBMS_RANDOM.RANDOM) WHERE rownum <= 10"
	cur.execute(sql)
	ora_list = cur.fetchall()
	rand_row_count = cur.rowcount
	



with myconn :

    my_cnt = mu.get_count(myconn , "Jobs")

    print("이관된 oracle 레코드수", ora_cnt, ", 이관된 mysql 레코드 수 =", my_cnt)
    if ora_cnt != my_cnt:
        print("레코드 수가 일치하지 않습니다! oracle=", ora_cnt, ", mysql =", my_cnt)
        exit()

    else:
        print("레코드 수가 일치합니다.")
        cur = myconn.cursor()

        sql = '''select id, job_title, min_salary, max_salary
                   from Jobs
                  where id = %s
                    and job_title = %s
                    and min_salary = ifnull(%s, 0)
                    and max_salary = ifnull(%s, 0)
                  '''
        cur.executemany(sql, ora_list)
        curcnt = cur.rowcount
	
	
        if rand_row_count == curcnt:
            print("데이터 샘플이 일치합니다", "샘플 레코드 개수는", rand_row_count)

        else:
            print("실패. oracle에서 읽힌 레코드와 mysql에서 읽힌 레코드의 개수는 각각 다음과 같습니다",
                  rand_row_count, curcnt)
