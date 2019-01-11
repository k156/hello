DELIMITER //
Create Trigger auto_assign_leader
 AFTER INSERT on Club FOR EACH ROW
BEGIN
    insert into ClubMember (club, student, level) value (
    NEW.id,
    (select s.id from Student s inner join ClubMember c on s.id = c.student  
								where c.level = 0 order by rand() limit 1), 2 
                                );

END //
DELIMITER ;



insert into Club set name = '불교부';
