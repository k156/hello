select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id;
 
select en.*, sub.id as 'sub_id', sub.name as 'sub_name', sub.prof from Enroll en full outer join Subject sub on en.subject = sub.id;

 
select id, name from Student order by rand() limit 100;
 
select * from Student;
select * from Subject;
select * from Enroll;

select name, count(*) from Student group by name having count(*) > 1;

select s.name, e.* from Student s left outer join Enroll e on s.id = e.student;





select count(*) from Student;
select name, birth from Student order by birth asc limit 10;
select * from Student where name like '김%' limit 10;
select * from Student where addr = '서울' and birth like'199%' and '2%';


select Subject.*, Prof.name from Subject inner join Prof on Subject.prof = Prof.id;

select s.id, (select id from Subject order by rand() limit 1) from Student s, Subject sbj;

select id, (select id from Subject order by rand() limit 1) sid from Student order by id;


select subject, count(*) from Subject group by subject;
select subject, student from Enroll group by subject, student having count(*) >1;


select * from Enroll;
