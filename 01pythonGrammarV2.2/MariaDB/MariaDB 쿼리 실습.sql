# tb_int 테이블 생성 
/*
PRIMARY KEY : 기본키라고 한다. 테이블에서 중복되지 않는
	식별자가 입력되는 컬럼에 지정한다. 사람으로 치면
	주민등록번호와 같은 역할을 한다. 
AUTO_INCREMENT : 기본키로 지정된 컬럼에 순차적인 
	일련번호를 부여해준다. 보통 자동증가컬럼이라고 표현
	하는데, 입력할때마다 1씩 증가된 숫자가 자동으로 
	부여된다. 
UNSIGNED : 자료형이 숫자형인 경우 양수로만 입력할수 
	있게 해준다. 이렇게 지정하면 표현범위가 2배로
	늘어난다. 
NOT NULL : null 즉 빈값을 허용하지 않는 제약조건으로
	필수입력사항인 경우에 지정한다. 
DEFAULT : 입력값이 없을때 기본값을 지정한다. 
*/

/*
1.숫자형 컬럼 : 정수, 실수와 같은 숫자를 입력할때 사용한다. 
	정수는 크기에 따라 tiny, samll과 같이 구분한다. 
	실수는 정밀도에 따라 구분한다. 
	FLOAT(10,5) : 전체 10자리, 소수점은 5자리까지 표현할수있다.
*/
CREATE TABLE tb_int(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT,
	
	fnum1 FLOAT(10,5) NOT NULL,
	fnum2 DOUBLE(20,10) 
);
DESC tb_int;

INSERT INTO tb_int (num1, num2, num3, num4, fnum1, fnum2)
VALUES (123, 12345, 1234567, 1234567890,
			12345.12345, 1234567890.1234567891);
SELECT * FROM tb_int;			

/*
2.날짜형 컬럼 : 날짜와 시간을 입력한다. 

CURRENT_TIMESTAMP : 날짜 입력값이 없는 경우 현재시각을 
	자동으로 입력해준다. 
*/
CREATE TABLE tb_date (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	date1 DATE NOT NULL,
	date2 DATETIME DEFAULT CURRENT_TIMESTAMP
);
DESC tb_date;

INSERT INTO tb_date (DATE1, DATE2) VALUES ('2024-04-19', NOW());
INSERT INTO tb_date (DATE1) VALUES ('2024-04-18');

SELECT * FROM tb_date;


/*
3.문자형 컬럼 
	char : 고정된 식별자로 사용하는 컬럼
	varchar : 게시판의 제목과 같이 길이를 정확히 결정할 수 
		없는 데이터 입력
	text : 내용과 같이 매우 긴 글을 작성할때 사용 
*/
CREATE TABLE tb_string (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 TEXT 
);
DESC tb_string;

INSERT INTO tb_string (str1, str2) VALUES
	('나는 짧은글', '나는 엄청 긴글');
SELECT * FROM tb_string;	


/*
4.특수형 컬럼 : 정해진 항목중 하나만 선택하거나, 2개이상을
	선택해서 입력할때 사용. 정해진 항목이 아닌 경우 입력시
	에러가 발생된다. 
*/
CREATE TABLE tb_spec (
	idx INT AUTO_INCREMENT, 
	
	spec1 ENUM('M','W','T'),
	spec2 SET('A','B','C','D'),
	
	PRIMARY KEY (idx)
);
DESC tb_spec;

INSERT INTO tb_spec (spec1, spec2) VALUES ('W', 'A,B,C');
INSERT INTO tb_spec (spec2) VALUES ('C,D');
INSERT INTO tb_spec (spec1, spec2) VALUES ('X', 'E');

SELECT * FROM tb_spec;



#파이썬 연동을 위한 게시판 테이블 생성 
/*
컬럼 : 일련번호, 제목, 내용, 작성자, 작성일, 조회수 
*/
CREATE TABLE board
(
	num INT NOT NULL AUTO_INCREMENT,            
	title VARCHAR(100) NOT NULL,   
	content TEXT NOT NULL, 
	id VARCHAR(30) NOT NULL,   
	postdate DATETIME DEFAULT current_timestamp, 
	visitcount MEDIUMINT NOT NULL DEFAULT 0,
	PRIMARY KEY (num)
);

#테스트용 더미데이터 입력 
INSERT INTO board (title, content, id)
	VALUES ('제목1', '내용입니다1', 'korea');
INSERT INTO board (title, content, id)
	VALUES ('제목2', '내용입니다2', 'korea');
INSERT INTO board (title, content, id)
	VALUES ('제목3', '내용입니다3', 'korea');
INSERT INTO board (title, content, id)
	VALUES ('제목4', '내용입니다4', 'korea');
INSERT INTO board (title, content, id)
	VALUES ('제목5', '내용입니다5', 'korea');

#전체레코드 조회	
SELECT * FROM board;
#레코드 조회시 정렬
SELECT * FROM board ORDER BY num DESC ; #내림차순
SELECT * FROM board ORDER BY num ASC ; #오름차순 
SELECT * FROM board ORDER BY num; #오름차순이 디폴트값 

/*
시나리오]일련번호가 2인 레코드의 작성자 아이디를 Hong으로 수정하시오.
*/
UPDATE board SET id='Hong' WHERE num=2;

/*
시나리오] 3번 게시물의 조회수를 1 증가시키시오. 
*/
UPDATE board SET visitcount=visitcount+1 WHERE num=3;

/*
시나리오] 4번 게시물을 삭제하시오. 
*/
DELETE FROM board WHERE num=4;


