create table Club(
	id smallint unsigned not null auto_increment primary key,
  name varchar(31) not null,
  createdate timestamp not null default current_timestamp,
  leader int unsigned,
  constraint foreign key fk_leader_student (leader) references Student (id)
);

create table Prof(
	id smallint unsigned not null auto_increment primary key,
  name varchar(31),
likecnt int default 0
);

desc Student;


create table Subject(
    id smallint unsigned not null auto_increment primary key,
  name varchar(31),
  prof smallint unsigned,
constraint foreign key fk_prof_prof (prof) references Prof (id)
on delete set null
);

create table Enroll(
    id int unsigned not null auto_increment primary key,
	subject smallint unsigned,
	student int unsigned,
	constraint foreign key fk_subject_subject (subject) references Subject (id)	on delete cascade,
    constraint foreign key fk_student_student (student) references Student (id) on delete cascade
);


insert into Club (name, leader) values ('연극부', 832);

select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id; 

insert into Subject (name, prof)
select '분자생물학', id from Prof order by rand() limit 10;

update Subject set name = '진화생물학' where name = '분자생물학' and id != 10 limit 1;



#과목별 학생수
select subject, count(*) from Subject group by subject;
# 동일과목에 중복학생 존재 여부 체커
select subject, student from Enroll group by subject, student having count(*) >1;

select * from Subject;
select * from Student;
select * from Prof;
select * from Enroll;





insert into Prof (name, likecnt) select name, ceil(rand() * 100) from Student order by rand() limit 100;
