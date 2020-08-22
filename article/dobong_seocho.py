from article.Article import Article, clean_xml, clean_string


def get_data(gu, article_count):
    if gu == "dobong":
        gu_tag = "DobongNewsNoticeList"
    elif gu == "seocho":
        gu_tag = "SeochoNewsNoticeList"
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/{}/1/{}/".format(gu_tag, article_count)
    return clean_xml(url)


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
    rows = get_data(gu, article_count)
    for row in rows:
        number = row.id.get_text(strip=True)
        title = row.title.get_text(strip=True)
        title = clean_string(title)
        content = row.description.get_text(strip=True)
        content = clean_string(content)
        date = row.pubdate.get_text(strip=True)
        url_origin = row.link.get_text(strip=True)
        url = change_url(gu, url_origin)
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    dss = get_ds("dobong", 5)
    for ds in dss:
        ds.print_article()
