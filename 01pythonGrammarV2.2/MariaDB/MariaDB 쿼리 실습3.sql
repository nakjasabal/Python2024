#select절의 *은 와일드카드로 모든 컬럼을 지정한다.
SELECT * FROM board;
#where절에는 인출을 위한 조건을 추가할 수 있다.
SELECT * FROM board WHERE num>=3;
#필요한 컬럼만 인출할때는 이와같이 컬럼명을 직접 기술한다.
SELECT num, title, id FROM board;
#title 컬럼에 입력된 내용으로 조건 추가 
SELECT * FROM board WHERE title='제목1';
#제목이 정확히 일치하지 않으므로 인출안됨 
SELECT * FROM board WHERE title='제목';
#정확히 일치하지 않는 키워드를 사용할때는 like를 써야한다.
SELECT * FROM board WHERE title LIKE '%목2%';


INSERT INTO board (title, content, id) VALUES 
	('오늘은 4월27일', '오늘은 토요일', 'bupyoung');
SELECT * FROM board ;

#레코드 수정하기 
/*
형식] update 테이블명 set 수정할내용 where 조건 
*/
UPDATE board SET 
	title='제목수정Test', content='내용수정Test', visitcount=999
WHERE num=3;

#레코드 삭제하기 
DELETE FROM board WHERE num=1; #1번 게시물 삭제 





