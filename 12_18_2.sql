DELIMITER $$
CREATE Function f_student_avg(_id int) 
 RETURNS int
BEGIN
	RETURN (select avg(midterm + finalterm)/2 from Enroll e inner join Grade g on g.enroll = e.id
															inner join Student s on e.student = s.id
                                                            where s.id = _id);
END $$
DELIMITER ;

select f_student_avg(100);



                                    
