# ICT_COC
서울시와 함께하는 인공지능(AI) 공모전(공공서비스 문제해결) 3회 출전팀 - 세줄요약장인


### article 
: 서울시공공데이터 OPEN API로부터 데이터를 받아오고 정리하는 패키지

**필요 라이브러리**
* beautifulsoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

**주요 클래스 및 함수**
* `class Article` : 게시글 하나를 표현하는 클래스

* `get_article(gu, article_count)` : article_count 만큼의 gu의 최신 게시글을 Article 객체로 리스트 반환하는 함수

```python
from article.get_articles import get_articles
gwanak_articles = get_articles("gwanak", 5) # Article 객체가 5개 담긴 리스트
for gwanak_article in gwanak_articles:
    gwanak_article.print_article()  
```
**중복 체크하는 부분은 일단 주석처리 해놨음**
