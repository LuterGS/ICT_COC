from article.Article import Article, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/SeochoNewsNoticeList/1/{}/".format(article_count)
    return clean_xml(url)


def change_url(url):
    num = url[60:]
    new_url = "https://www.seocho.go.kr/site/seocho/ex/bbs/View.do?cbIdx=57&bcIdx={}".format(num)
    return new_url


def get_seocho(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.id.get_text(strip=True)
        title = row.title.get_text(strip=True)
        title = clean_string(title)
        content = row.description.get_text(strip=True)
        content = clean_string(content)
        date = row.pubdate.get_text(strip=True)
        url_origin = row.link.get_text(strip=True)
        url = change_url(url_origin)
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    #dss = get_ds("dobong", 5)
    datas = get_data("dobong", 5)
    for ds in datas:
        print(ds)
