create table Classroom(
	id number,
	room_num number
    );
    
create table Prof (
	id number(5) not null primary key,
	name varchar2(31) not null,
	likecnt number(5) default 0 not null
    );
    
create table Subject (
    id number not null primary key,
    name varchar2(31) not null,
    prof number(5),
    classroom number(5),
	constraint fk_prof foreign key (prof)
  	  references Prof(id),
      constraint fk_classroom foreign key (classroom) references Classroom(id)
      );
      
      

select * from countries;
select * from departments;
select * from employees;
select * from jobs;

select employee_id, count(*) from employees group by deprartment_id;
select department_id, avg(salary) from employees group by department_id;
select job_id, avg(salary) from employees group by job_id;

select employee_id from employees where  from employees e;


select e.last_name, e.salary from employees e inner join jobs j on e.job_id = j.job_id where j.job_title = Sales Representative and e.salary between 9000 and 10000;