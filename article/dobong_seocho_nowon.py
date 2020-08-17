import requests
from bs4 import BeautifulSoup
from article.Article import Article


def clean_xml(gu, article_count):
    if gu == "dobong":
        gu_tag = "DobongNewsNoticeList"
    elif gu == "seocho":
        gu_tag = "SeochoNewsNoticeList"
    elif gu == "nowon":
        gu_tag = "NowonNewsNoticeList"
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/{}/1/{}/".format(gu_tag, article_count)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    pretty_xml = soup.prettify(formatter=None)
    pretty_soup = BeautifulSoup(pretty_xml, 'xml')
    rows = pretty_soup.find_all("row")
    return rows


def clean_ptags(ptags):
    result = ""
    for ptag in ptags:
        text = ptag.get_text(strip=True)
        text = text.replace(u'\xa0', u' ')
        if len(text):
            result = result + text + " "
    return result


def get_dsn(gu, article_count):
    articles = []
    rows = clean_xml(gu, article_count)
    for row in rows:
        number = row.ID.get_text(strip=True)
        title = row.TITLE.get_text(strip=True)
        if gu == "nowon":
            ptags = row.DESCRIPTION.find_all("p")
            content = clean_ptags(ptags)
        else:
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

    #xmls = clean_xml("nowon", 5)
    #print(xmls)

    dobong_articles = get_dsn("nowon", 5)
    for dobong_article in dobong_articles:
        dobong_article.print_article()