from article.Article import Article, clean_ptags, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/DdmNewsGujungList/1/{}/".format(article_count)
    return clean_xml(url)


def change_url(url):
    num = url[48:53]
    new_url = "https://www.ddm.go.kr/ddm/gujungNewsview.jsp?pid={}".format(num)
    return new_url


def get_ddm(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.listno.get_text(strip=True)
        title = row.subject.get_text(strip=True)
        title = clean_string(title)
        content = row.description.find_all("p")
        content = clean_ptags(content)
        content = clean_string(content)
        date = row.pubdate.get_text(strip=True)
        url_origin = row.linkurl.get_text(strip=True)
        url = change_url(url_origin)
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    ddms = get_ddm(5)
    for ddm in ddms:
        ddm.print_article()