select s.name
     from Enroll e inner join Subject sbj on e.subject = sbj.id
				   inner join Student s on e.student = s.id
where sbj.name = '역사';



select min(sbj.name) subject_name, 
s.gender (case s.gender when 1 then '남' when 0 then '여' else end, 
count(*) as 'student cnt'
	   from Enroll e inner join Student s on e.student = s.id
					 inner join Subject sbj on e.subject = sbj.id
where s.addr = '서울' 
group by sbj.id, s.gender
order by subjec_name, s.gender desc;


START TRANSACTION;

update Test set name = '딸기맛' where id = 4;

select * from Test;

ROLLBACK;


select * from Subject;

select group_concat(name) as 'subject name' from Subject;

insert ignore into Test(id, name) values (2, 'aaa');

select * from Test;

select sbj.name , count(*) as '학생수'
	   from Enroll e inner join Student s on e.student = s.id
					 inner join Subject sbj on e.subject = sbj.id
where s.addr = '서울' group by sbj.name;



select * from Student;
