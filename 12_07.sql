#Grade 테이블 생성
create table Grade(
	id int unsigned not null auto_increment primary key,
    midterm smallint unsigned not null default 0,
    finalterm smallint unsigned not null default 0,
    enroll smallint unsigned not null
);


insert into Grade(enroll) (select id from Enroll order by id);
 
update Grade set midterm = (floor(rand() * 101));
update Grade set finalterm = (floor(rand() * 101));


select * from Grade;

-- 여기에서 학점이 안되요~!!

#insert into Grade g (select sub.name as '과목', stu.name as '학생명', g.midterm as '중간고사', g.finalterm as '기말고사', 
#		g.midterm + g.finalterm as '총점',  round((g.midterm + g.finalterm) / 2 , 1) as '평균');
#         case '평균' when '평균' like'9%' then 'A' 
#				     when '평균' like'8%' then 'B'
#                     when '평균' like'7%' then 'C'
#                     when '평균' like'6%' then 'D'
#                             else 'F' end as '학점'
#)
#from Grade g inner join (Enroll e inner join Student stu on e.student = stu.id
#						          inner join Subject sub on e.subject = sub.id) on g.enroll = e.id;


select sub.name as '과목', stu.name as '학생명', g.midterm as '중간고사', g.finalterm as '기말고사',
         midterm + g.finalterm as '총점',  round((g.midterm + g.finalterm) / 2 , 1) as '평균',
     case when round((g.midterm + g.finalterm) / 2 , 1) >= 90 then 'A'
              when round((g.midterm + g.finalterm) / 2 , 1) >= 80 then 'B'
              when round((g.midterm + g.finalterm) / 2 , 1) >= 70 then 'C'
              when round((g.midterm + g.finalterm) / 2 , 1) >= 60 then 'D'
              when round((g.midterm + g.finalterm) / 2 , 1) >= 50 then 'E'
                else 'F' end as '학점'
from Grade g inner join (Enroll e inner join Student stu on e.student = stu.id
                        inner join Subject sub on e.subject = sub.id) on g.enroll = e.id
order by 1, 6 desc;


select sub.name as '과목', round(avg(g.midterm+g.finalterm), 1) as '평균'
from Grade g inner join (Enroll e inner join Student stu on e.student = stu.id
                        inner join Subject sub on e.subject = sub.id) on g.enroll = e.id
group by sub.id ;


select * from Enroll order by subject, student;
select * from Student;

-- 과목별 학생수
select subject, count(*) from Enroll group by subject;

-- 동일과목(한과목)에 중복 학생 존재 여부 체크
select subject, student, count(*) from Enroll group by subject, student having count(*) > 1;



update Enroll set student where ;


START TRANSACTION;

create view Trial1 AS
select e.subject as 'subject', stu.name as 'student', g.midterm as 'midterm', g.finalterm as 'final',
midterm + g.finalterm as 'total',  round((g.midterm + g.finalterm) / 2 , 1) as 'average'
from Grade g inner join Enroll e on e.id = g.enroll
			 inner join Student stu on e.student = stu.id
			 inner join Subject sub on e.subject = sub.id;



select * from Trial1;