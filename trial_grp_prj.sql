drop procedure if exists sp_top3_name_grade;
delimiter $$
create procedure sp_top3_name_grade()
begin
	declare v_isdone boolean default False;
    declare v_sbj_name varchar;
    declare v_name varchar;
    declare v_score smallint(5) unsigned;
    
	declare top_3 CURSOR FOR
		select subject_name, student_name, max(avr)
		from v_grade_enroll 
		group by subject_name, student_name 
		order by 1, 3 desc;
    
    declare continue handler
        for not found set _isdone = True;
	
    drop table if exists top3;
	create temporary table top3 (
    subjects varchar(31) primary key,
	`1stname` varchar(32),
    `1stscore` smallint(5) unsigned,
    `2ndname` varchar(32),
    `2ndscore` smallint(5) unsigned,
	`3rdname` varchar(32),
    `3rdscore` smallint(5) unsigned
    );
    
    
    open cur_top3;
    

    loop1: LOOP
        Fetch top_3  into v_sbj_name,  v_name , v_score  ;
        
        IF EXISTS(_subjects) THEN
            update top3 set (2stname = v_name,
                               cnt = cnt + 1
             
        ELSE
            insert into top3 value(v_sbj_name, v_name, v_score);
            
        END IF;
        
        IF _isdone THEN
            LEAVE loop1;
        END IF;
    
    END LOOP loop1;
    
    close cur_avrs;
    
    select * from t_grade;
    
end $$
delimiter ;

call sp_grade_stem_leaf('국어');

select * from Subject;

/*
select * from v_grade_enroll;
select floor(avr / 10), group_concat(mod(avr, 10))
  from v_grade_enroll
  where subject = 1
  group by floor(avr / 10)
  ;
*/
-- call sp_cnt('select * from Subject');


-- select * from Club;
-- select * from ClubMember;

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `dooo`@`172.17.0.1` 
    SQL SECURITY DEFINER
VIEW `v_grade_enroll` AS
    SELECT 
        `g`.`id` AS `id`,
        `g`.`midterm` AS `midterm`,
        `g`.`finalterm` AS `finalterm`,
        (`g`.`midterm` + `g`.`finalterm`) AS `total`,
        FLOOR(((`g`.`midterm` + `g`.`finalterm`) / 2)) AS `avr`,
        `g`.`enroll` AS `enroll`,
        `e`.`subject` AS `subject`,
        `e`.`student` AS `student`
    FROM
        (`Grade` `g`
        JOIN `Enroll` `e` ON ((`g`.`enroll` = `e`.`id`)))
