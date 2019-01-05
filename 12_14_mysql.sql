
select * from Subject;
select * from Prof;

DELIMITER //
Create Trigger tr_auto_assign_prof
BEFORE INSERT on Subject FOR EACH ROW
BEGIN
	IF NEW.prof is null then
    set New.prof = (select id from Prof 
    order by rand() limit 1);
    
END IF; 

END//
DELIMITER ;


select * from Subject;
insert into Subject(name, prof, students) values ('열역학', null, 0);

#과목명을 주면, 해당 과목의 수강 학생수를 반환하는 함수를 만드시오

DELIMITER $$
CREATE Function stu_cnt3(_name varchar(31)) 
RETURNS smallint(6)
BEGIN
RETURN (select count(*) from Enroll where subject = (select id from Subject where name = _name));
END $$
DELIMITER ;







DELIMITER $$
CREATE Function dt(_ts timestamp) RETURNS varchar(31)
BEGIN
	RETURN date_format(_ts, '%m/%d %H:%i');
END $$
DELIMITER ;


select dt(current_timestamp);
select regdt, dt(regdt) from Student;

select stu_cnt3('세포생물학');