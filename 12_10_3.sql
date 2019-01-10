#ClubMember 테이블 생성
CREATE TABLE `dooodb`.`ClubMember` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `club` VARCHAR(31) NOT NULL,
  `student` INT NULL,
  `level` TINYINT(0) NULL DEFAULT 0 ,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


START TRANSACTION;
#ClubMember에 클럽이름, 클럽장 입력하기
insert into ClubMember(club) select name from Club order by id;
insert into ClubMember(student) select leader from Club order by id;
update ClubMember set level = 2 where id between 1 and 3;
select * from ClubMember;

#ClubMember에 클럽간부 입력하기 
insert into ClubMember(student, club)
select id, (select id from Club order by rand() limit 1) from Student order by id limit 10
on duplicate key update student = student;
update ClubMember set level = 1 where id > 3; 
select * from ClubMember;

#ClubMember에 클럽회원 입력하기 
insert into ClubMember(student, club)
select id, (select id from Club order by rand() limit 1) from Student order by id limit 40
on duplicate key update student = student;
update ClubMember set level = 0 where id > 21; 
select * from ClubMember;

# Club 테이블에서 leader 삭제
ALTER TABLE `dooodb`.`Club` 
DROP FOREIGN KEY `Club_ibfk_1`;
ALTER TABLE `dooodb`.`Club` 
DROP INDEX `fk_leader_student`;

Alter table Club drop leader;
select * from Club;

#ClubMember 테이블에 FK 추가
#Update ClubMember set club = 1 where id = 1;
#Update ClubMember set club = 2 where id = 2;
#Update ClubMember set club = 4 where id = 3;

ALTER TABLE `dooodb`.`ClubMember` 
CHANGE COLUMN `club` `club` SMALLINT UNSIGNED NULL DEFAULT NULL ,
CHANGE COLUMN `student` `student` INT(11) UNSIGNED NULL DEFAULT NULL ;

ALTER TABLE ClubMember ADD Constraint FOREIGN KEY (student) REFERENCES Student(id);
ALTER TABLE ClubMember ADD Constraint FOREIGN KEY (club) REFERENCES Club(id);

select * from ClubMember;

COMMIT;


select * from Dept;


