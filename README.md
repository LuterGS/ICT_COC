# ICT_COC
서울시와 함께하는 인공지능(AI) 공모전(공공서비스 문제해결) 3회 출전팀 - 세줄요약장인


### article
------
**필요 라이브러리**
* beautifulsoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

`class Article` : 게시글 하나를 표현하는 클래스
`get_gwanak(article_count)` : article_count 만큼의 최신 게시글을 Article 객체로 리스트 반환

```python
from gwanak import get_gwanak
gwanak_articles = get_gwanak(5) # Article 객체가 5개 담긴 리스트
for gwanak_article in gwanak_articles:
    gwanak_article.print_article()  
```
