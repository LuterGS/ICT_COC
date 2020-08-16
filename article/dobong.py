import requests
from bs4 import BeautifulSoup
from article.Article import Article


def clean_xml(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/DobongNewsNoticeList/1/{}/".format(article_count)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    rows = soup.find_all("row")
    return rows


def get_dobong(article_count):
    articles = []
    rows = clean_xml(article_count)
    for row in rows:
        number = row.ID.get_text(strip=True)
        title = row.TITLE.get_text(strip=True)
        content = row.DESCRIPTION.get_text(strip=True)
        date = row.PUBDATE.get_text(strip=True)
        url = row.LINK.get_text(strip=True)
        tmp_article = Article(number, title, content, date, url)
        '''if tmp_article.is_duplicate("http://175.193.68.230/sendData"):
                    print(tmp_article.number + " is duplicate")
                else:
                    articles.append(tmp_article)'''
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    dobong_articles = get_dobong(5)
    for dobong_article in dobong_articles:
        dobong_article.print_article()