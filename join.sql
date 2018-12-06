insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by id;

insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;
 
insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;
 
 select * from Enroll;

select s.*, p.name as 'prof.name'
	from Subject s inner join Prof p on s.prof = p.id;
    
    
select subject, count(*)
  from Enroll group by subject;
  

select * from Enroll;
select * from Subject;

#과목별 학생수
select e.subject, max(s.name) as 'subject name', count(*) as '학생수'
  from Enroll e inner join Subject s on e.subject = s.id  group by e.subject;
##역사 과목의 학생 목록
select s.name, s.birth
  from Enroll e inner join Student s on e.student = s.id
                inner join Subject sbj on e.subject = sbj.id
 where sbj.name = '분자생물학';
#특정과목(국어)과목을 듣는 서울 거주 학생 목록 (과목명, 학번, 학생명)
select sbj.name, s.id, s.name
  from Enroll e inner join Student s on e.student = s.id
                inner join Subject sbj on e.subject = sbj.id
 where sbj.name = '분자생물학' and s.addr = '서울';
 
select s.addr, count(*)
   from Enroll e inner join Student s on e.student = s.id
				inner join Subject sbj on e.subject = sbj.id
where sbj.name = '분자생물학' group by s.addr;
