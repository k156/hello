select v.subject, group_concat(stu.name)
  from Subject sbj inner join v_grade_enroll v on sbj.id = v.subject
				 inner join Student stu on stu.id = v.student
                        group by v.subject
                        ; 

select * from v_grade_enroll;
select * from Grade;

