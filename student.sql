create table Test(
	id tinyint unsigned not null auto_increment,
  name char(5) not null,
  primary key(id)
  );
  
desc Test;

show create table Test;

insert into Student (name, addr, birth) values ('김하나', '서울시 언주로 303', '1991-05-03');

update Student set name = '김둘리' where id = 4;

INSERT INTO Student(Name, addr, birth, tel, email)
			VALUES('이순신', '서울시 강남구 개포로', '19950216', '01031010024', 'apple@naver.com');

INSERT INTO Student(Name, addr, birth, tel, email)
			VALUES('차은우','서울시 송파구 올림픽로', '19910701', '01050274421', 'facegenius@outlook.com');

INSERT INTO Student(Name, addr, birth, tel, email)
			VALUES('홍길동','서울시 안암동', '19930124', '01022402341', 'abuzi@google.com');

select * from Student;
select * from Test;

update Student set gender = (case when tel like '010-1%' or tel like '010-2%' or tel like '010-3%' 
                             or tel like '010-4%' or tel like '010-5%' then 0 else 1 end)
                             where id > 0;



Student

insert into Test(name) select name from Student where id < 5;

select * from Student where name like '%정_';
select * from Student where id in (10, 20, 30);
select * from Student where id = 10 or id = 20 or id = 30;
select * from Student where id between 10 and 30;
select * from Student where id in (select id from Test where id between 5 and 30);

select * from Student where email like 'a%' and tel like '____9%';
select * from Student where addr = '강원' order by birth desc limit 10,5;

ALTER DATABASE dooodb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;




CREATE TABLE `Test3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ttt` varchar(45) DEFAULT NULL,
PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET=utf8;
