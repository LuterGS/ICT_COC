import requests
from bs4 import BeautifulSoup
from article.Article import Article
import re


def clean_xml(gu, article_count):
    if gu == "dobong":
        gu_tag = "DobongNewsNoticeList"
    elif gu == "seocho":
        gu_tag = "SeochoNewsNoticeList"
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/{}/1/{}/".format(gu_tag, article_count)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    pretty_xml = soup.prettify(formatter=None)
    pretty_soup = BeautifulSoup(pretty_xml, 'xml')
    rows = pretty_soup.find_all("row")
    return rows


def change_url(gu, url):
    if gu == "dobong":
        num1 = url[40:48]
        num2 = url[49:]
        new_url = "http://www.dobong.go.kr/bbs.asp?bmode=D&pcode={}&code={}".format(num1, num2)
        return new_url
    elif gu == "seocho":
        num = url[60:]
        new_url = "https://www.seocho.go.kr/site/seocho/ex/bbs/View.do?cbIdx=57&bcIdx={}".format(num)
        return new_url
    return url


def get_ds(gu, article_count):
    articles = []
    rows = clean_xml(gu, article_count)
    for row in rows:
        number = row.ID.get_text(strip=True)
        title = row.TITLE.get_text(strip=True)
        title = title.replace("'", "''")
        title = title.replace('"', '\"')
        content = row.DESCRIPTION.get_text(strip=True)
        content = content.replace('lt', '')
        content = content.replace('gt', '')
        content = content.replace("'", "''")
        content = content.replace('"', '\"')
        date = row.PUBDATE.get_text(strip=True)
        url_origin = row.LINK.get_text(strip=True)
        url = change_url(gu, url_origin)
        change_url(gu, url)
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":

    #xmls = clean_xml("nowon", 5)
    #print(xmls)

    dobong_articles = get_ds("seocho", 5)
    for dobong_article in dobong_articles:
        dobong_article.print_article()
