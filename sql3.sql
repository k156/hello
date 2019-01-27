drop procedure if exists sp_stem_leaf;
delimiter $$
create procedure sp_stem_leaf(_sbj_name varchar(31))
begin


Declare avr_cur CURSOR FOR
	select avr from Grade;

declare is_done = False;

Declare Continue Handler
	For Not Found SET is_done = True;
OPEN avr_cur;

drop table if exists v_stem_leaf;


<cursor-loop-var>: LOOP
	Fetch avr_cur into <var-name>, ...;

	IF is_done THEN
		LEAVE <cursor-loop-var>;
	END IF;
END LOOP <cursor-loop-var>;
CLOSE <cursor-name>;

end $$
delimiter ;