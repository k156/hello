create view v_grade_enroll AS
select g.*, e.subject, e.student 
  from Grade g inner join Enroll e on g.enroll = e.id;
  

select * from Grade;


select subject, count(*);


create view v_student_grade as
select stu.id, stu.name, g.id '과목id' , sbj.name '과목이름' , g.midterm, g.finalterm, 
       (midterm+finalterm), round((midterm+finalterm)/2) 'avr', 
	      (case when round((midterm+finalterm)/2) >= 90 then 'A'
          when round((midterm+finalterm)/2)>= 80  then 'B'
          when round((midterm+finalterm)/2) >= 70 then 'C'
          else 'F' end) '평점'
        from Enroll e inner join Student stu on stu.id = e.student
                 inner join Subject sbj on e.subject = sbj.id
				 inner join Grade g on g.enroll = e.id;


alter table Subject add column students smallint default 0 not null;

update Subject s
   set students = (select count(*) from Enroll where subject = s.id group by subject);



delimiter //
create trigger tr_enroll_subject_students
 after insert on Enroll For Each Row
 BEGIN

 END
 //
 delimiter 