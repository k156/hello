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
select * from locations;
select * from departments;
select * from job_history;


select max(d.department_name), count(distinct e.employee_id) emp_cnt
  from Employees e inner join departments d on e.department_id = d.department_id
  group by e.department_id
  order by emp_cnt desc;

--select employee_id, count(*) from employees group by deprartment_id;

select department_id, round(avg(salary),-1) from employees group by department_id;
select job_id, avg(salary) from employees group by job_id;

--select employee_id from employees where  from employees e;


--select e.last_name, e.salary from employees e inner join jobs j on e.job_id = j.job_id where j.job_title = "Sales Representative" and e.salary between 9000 and 10000;


--각 직급별로 급여의 총합을 구하고자 한다. 급여 총합이 가장 높은 직급순으로 급여 총합을 출력하시오. (단, 급여총합이 30,000 이상인 직급만 출력할 것)

select * from (
                select min(j.job_title) job_tit, sum(e.salary) ssum
                  from employees e inner join jobs j on e.job_id = j.job_id
                 group by j.job_id)
 where ssum > 30000
 order by ssum desc;


--각 도시별 평균 연봉(급여)가 높은순으로 상위 3개 도시만 출력


select * from (select * from (
                select min(l.city) city, round(avg(e.salary),0) avg_salary 
                  from employees e inner join departments d on e.department_id = d.department_id
                                   inner join locations l on d.location_id = l.location_id
                                   group by d.location_id) 
order by avg_salary desc) where rownum <=3;




--8)직책(Job Title)이 Sales Manager인 사원들의 입사년도와 입사년도(hire_date)별 평균 급여를 출력하시오. 출력 시 년도를 기준으로 오름차순 정렬하시오.

select * from (
               (select to_char(hire_date, 'YY')) hire_year, avg(salary) avg_salary
                  from employees
group by hire_year 
order by hire_year;
                 
                 
select * from ((select to_char(hire_date, 'YY')) hire_year, avg(salary) avg_salary from employees) group by hire_year;
                
select to_char(hire_date, 'YY')) hire_year, avg(salary) avg_salary from employees group by hire_year;
                 
                 
--select * from(
--              select e.hire_date hire_date, avg(e.salary) avg_salary
--                from employees e inner join jobs j on j.job_id = e.job_id
--                                 inner join job_history h on h.job_id = j.job_id)
-- where j.job_title = "Sales Representative"
-- group by e.hire_date order by e.hire_date;

--select * from (
--               select hire_date hire_date, avg(salary) avg_salary
--                 from employees inner join jobs j on j.job_id = e.job_id
--                 group by hire_date order by hire_date)
--where j.job_title = "Sales Representative";
 
-- 9)	각 도시(city)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다. 평균급여가 가장 낮은 도시부터 도시명(city)과 평균연봉, 해당 도시의 직원수를 출력하시오. 
-- 단, 도시에 근무하는 직원이 10명 이상인 곳은 제외하고 조회하시오.

select e.employee_id, count(*)
  from (select l.city, group by d.department order by avg(e.salary)