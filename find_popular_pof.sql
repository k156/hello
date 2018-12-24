#likecnt, 수강생수, 수강생 평균점수로 인기있는 교수 찾기

DELIMITER $$
CREATE Function dt(_ts timestamp) RETURNS varchar(31)
BEGIN
	RETURN (select p.name from Prof p inner join Subject s on s.prof = p.id
									  inner join Enroll e on e.subject = s.id
									  inner join Grade g on g.enroll = e.id
			 order by s.students desc limit 1
END $$
DELIMITER ;

select * from v_grade_enroll;