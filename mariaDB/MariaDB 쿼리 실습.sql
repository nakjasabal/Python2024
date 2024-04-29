# DB와 사용자계정 생성>> mysql DB에서 root로 로그인한 후 실행
CREATE DATABASE sample_db;
CREATE USER 'sample_user'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'localhost';
FLUSH PRIVILEGES;


#앞에서 생성한 계정으로 로그인 후 실행

/*
블럭단위 주석 
*/
# 라인단위주석

/*
HeidiSQL(하이디SQL)에서 쿼리를 실행하는 방법
1.F9 : 현재 문서의 쿼리 전체를 실행한다. 
2.Ctrl+F9 : 블럭으로 지정한 쿼리만 실행한다. 
	만약 쿼리의 절반정도만 선택하면 에러가 발생한다. 
3.Ctrl+Shift+F9 : 현재 쿼리를 실행한다. 
	단, 마지막에 기술한 세미콜론 안으로 커서를 옮긴후 실행해야
	한다. 
*/

/*
테이블 생성하기 : 엑셀에서 워크시트와 같은 개념으로 데이터를
	저장하는 공간이다. create명령으로 생성하고 형식은 다음과같다.
	형식] create table 테이블명 (
				컬럼명 자료형 제약조건1 제약조건2
			);
	제약조건설명
		PRIMARY KEY : 기본키라고도 하는데, 해당 키로 지정되면
			중복되지 않는 값이 입력되어야 한다. 사람으로 따지면
			주민번호와 같은 역할을 한다. 
		AUTO_INCREMENT : 자동증가컬럼으로 지정하겠다는 의미로 
			1씩 증가하는 순차적인 정수값이 자동으로 입력된다. 
		UNSIGNED : 정수형을 사용할 경우 음수는 사용하지 않고
			양수의 범위만 사용한다. 이 경우 양의 범위가 2배 늘어난다.
		NOT NULL : 빈값을 허용하지 않겠다는 제약조건으로 반드시
			입력되야하는 항목에 지정한다. 
*/
/*****
데이터 타입(자료형)의 종류
1.숫자형
******/
CREATE TABLE tb_int ( 
	idx INT PRIMARY KEY AUTO_INCREMENT, 	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT ,
	fnum1 FLOAT(10,5) NOT NULL,
	fnum2 DOUBLE(20,10) 
);

# 테이블의 구조를 확인한다. 
DESC tb_int;

/*
데이터입력하기
형식1]  insert into 테이블명 (컬럼명) values (값);
	컬럼의 갯수와 값의 갯수는 반드시 일치해야한다. 
*/
INSERT INTO tb_int (num1,num2,num3,num4,fnum1,fnum2)
VALUES (123, 12345, 1234567, 1234567890, 
		12345.12345, 1234567890.1234567890);
		
/*
형식2] insert into 테이블명 values (값);
	이 경우에는 생성된 테이블의 모든 컬럼을 대상으로 한다. 
	컬럼이 7개라면 값도 반드시 7개 전체를 기술해야한다. 
*/
INSERT INTO tb_int 
VALUES (2, 123, 12345, 1234567, 1234567890, 
		12345.12345, 1234567890.1234567890);
/*
현재 tb_int테이블은 idx컬럼이 primary key(기본키)로 지정되어있다. 
따라서 해당 컬럼에 중복된 값이 들어가면 에러가 발생된다. 
auto_increment (자동증가) 컬럼으로 지정되어 있으므로 형식1과 같이
insert를 실행하면 자동으로 증가되어 중복되지 않는 정수값이 자동으로
입력된다. 
*/

/********
2.날짜형
*********/
CREATE TABLE tb_date (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	date1 DATE NOT NULL,
	date2 DATETIME DEFAULT CURRENT_TIMESTAMP
);
/*
DEFAULT : 해당 컬럼에 값이 입력되지 않는 경우 디폴트로 입력할 값을
	지정할때 사용하는 제약조건
CURRENT_TIMESTAMP : 날짜형식으로 지정된 컬럼에 현재시각을 입력할때
	사용하는 키워드. 초 단위까지의 시간이 입력된다. 
NOW() : insert 쿼리문에서 날짜타입의 컬럼에 현재날짜를 입력할 때 
	사용하는 함수 
*/
DESC tb_date;

INSERT INTO tb_date (DATE1, DATE2) VALUES ('2023-02-25', NOW());
INSERT INTO tb_date (DATE1) VALUES ('2023-02-27');

/*
레코드 조회하기 
형식]
	select *(혹은 컬럼명) from 테이블명 ;
*/
SELECT * FROM tb_date;
SELECT DATE2 FROM tb_date;




/**********
3. 문자형
**********/
CREATE TABLE tb_string (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 TEXT 
);
DESC tb_string;

INSERT INTO tb_string (str1, str2) VALUES 
	('난 짧은글3', '난 엄청 긴글3');

/*
레코드 조회시 조건 추가하기 
형식] select * from 테이블명 where 컬럼1=값 and(혹은 or) 컬럼2=값;
	and는 2개의 컬럼이 동시에 일치해야 하고, 
	or는 2개 중 하나만 일치하면 레코드를 인출한다. 
*/
SELECT * FROM tb_string;	
SELECT * FROM tb_string WHERE idx=2;	
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글2';	
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글3';	
SELECT * FROM tb_string WHERE idx=2 OR str1='난 짧은글3';	


/*
레코드 검색시 문자열이 포함된 것을 인출하고 싶다면 like절을 사용한다.
형식
	where 컬럼명 like '%검색어%' ;
		%는 모든 문자열을 대체하는 와일드 카드로
		'%난 짧은%' => 해당 문자열로 시작, 포함, 종료되는 레코드 
		'난 짧은%' => 시작되는 문자열
		'%난 짧은' => 종료되는 문자열
*/
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은%';	
SELECT * FROM tb_string WHERE str1 LIKE '난 짧은%';	
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은';	


/**********
4. 특수형
**********/
CREATE TABLE tb_spec (
	idx INT AUTO_INCREMENT, 
	
	spec1 ENUM('M','W','T'),
	spec2 SET('A','B','C','D'),
	
	PRIMARY KEY (idx)
);
DESC tb_spec;

#레코드 입력하기 
INSERT INTO tb_spec (spec1, spec2) VALUES ('W', 'A,B,C');#정상입력
#아래 2개의 쿼리문은 지정되지 않은 값이 입력되어 에러가 발생한다.
INSERT INTO tb_spec (spec1, spec2) VALUES ('X', 'A,B,C');#spec1에러
INSERT INTO tb_spec (spec1, spec2) VALUES ('M', 'X,B,C');#spec2에러
/* spec1컬럼은 not null 로 지정되지 않았으므로 null값을 허용하는 
컬럼이다. 따라서 값을 입력하지 않아도 된다. 
null이란 아무것도 입력되지 않았음을 표현하는 문장이다. */
INSERT INTO tb_spec (spec2) VALUES ('B,C,D');
SELECT * FROM tb_spec;

/******
Python 실습을 위한 테이블 생성
*******/
#테이블 삭제하기. 이때 저장된 모든 레코드도 삭제된다. 
DROP TABLE board;

#테이블 생성하기.
/*
컬럼의 순서대로 일련번호, 제목, 내용, 작성자아이디, 작성일, 
	조회수를 의미한다. 
	일련번호는 중복되지 않는 정수값 입력을 위해 기본키 와 자동증가
	컬럼으로 지정되었다. 
*/ 
CREATE TABLE board (
	num INT NOT NULL AUTO_INCREMENT,   
	title VARCHAR(200) NOT NULL,
	content TEXT NOT NULL,
	id VARCHAR(20) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP,
		visitcount MEDIUMINT ,
	PRIMARY KEY (num)
);
# 더미데이터(테스트 데이터) 입력하기
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목1', '내용1입니다.', 'tjoeun', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목2', '내용2입니다.', 'tjoeun', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목3', '내용3입니다.', 'tjoeun', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목4', '내용4입니다.', 'tjoeun', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목5', '내용5입니다.', 'tjoeun', NOW(), 0);
#데이터 확인하기
SELECT * FROM board;

#정렬하기
/*
	desc : 내림차순 정렬
	asc : 오름차순 정렬(default이므로 생략할 수 있다)
*/
SELECT * FROM board ORDER BY num DESC;
SELECT * FROM board ORDER BY num ASC; #오름차순
SELECT * FROM board ORDER BY num; #위와 결과가 동일하다. 

#수정하기
/*
update문 형식]
	update 테이블명 set 컬럼1=값1, 컬럼2=값2 where 컬럼=값
	-2개 이상의 컬럼을 수정하는 경우 위와같이 콤마로 구분한다. 
	-where절의 조건은 select와 동일하게 사용할 수 있다. 

시나리오1]일련번호가 2번인 레코드의 작성자 아이디를 korea로 
	수정하시오.
*/
UPDATE board SET id='korea' WHERE num=2;
SELECT * FROM board;

/*
시나리오2] 일련번호가 3이상인 레코드의 제목을 '제목3이상' 으로 
	수정하시오. 
*/
# 문제의 조건에 일치하는 레코드 확인하기
SELECT * FROM board WHERE num>=3;
# 해당 조건으로 업데이트(수정) 하기
UPDATE board SET title='제목3이상' WHERE num>=3;
# 제대로 적용되었는지 확인 
SELECT * FROM board;

/*
시나리오3] 일련번호 5번 게시물의 조회수를 1 증가시키시오.
	(컬럼의 형식이 숫자인 경우에는 이와같이 사칙연산이 가능하다)
*/
# 조회수를 무조건 1로 업데이트 한다. 
UPDATE board SET visitcount=1 WHERE num=5;
# 기존의 조회수에 1을 더해서 입력하므로 지속적으로 증가한다. 
UPDATE board SET visitcount=visitcount+1 WHERE num=5;
SELECT * FROM board;

#삭제하기 
/*
delete문 형식]
	delete from 테이블명 where 컬럼=값;
	(삭제할때는 컬럼명을 별도로 명시할 필요가 없으므로 생략한다.)
	
시나리오4] 일련번호 3번 게시물을 삭제하시오.
*/
DELETE FROM board WHERE num=3;
SELECT * FROM board;






