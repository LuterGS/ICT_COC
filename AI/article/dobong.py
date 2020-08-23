from article.Article import Article, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/DobongNewsNoticeList/1/{}/".format(article_count)
    return clean_xml(url, parse='xml')


def change_url(url):
    num1 = url[40:48]
    num2 = url[49:]
    new_url = "http://www.dobong.go.kr/bbs.asp?bmode=D&pcode={}&code={}".format(num1, num2)
    return new_url


def get_dobong(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.ID.get_text(strip=True)
        title = row.TITLE.get_text(strip=True)
        title = clean_string(title)
        content = row.DESCRIPTION.get_text(strip=True)
        content = clean_string(content)
        date = row.PUBDATE.get_text(strip=True)
        url_origin = row.LINK.get_text(strip=True)
        url = change_url(url_origin)
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    #dss = get_ds("dobong", 5)
    datas = get_data("dobong", 5)
    for ds in datas:
        print(ds)
