

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
