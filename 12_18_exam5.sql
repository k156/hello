select e.last_name, e.salary, d.department_name
  from Employees e inner join Departments d on e.department_id = d.department_id
 where d.department_name = 'Marketing'
   and e.salary < (select avg(salary) from Employees where department_id = 80);
   
