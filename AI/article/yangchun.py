from article.Article import Article, clean_ptags, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/YcNotice/1/{}/".format(article_count)
    return clean_xml(url)


def get_yangchun(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.bbs_seq.get_text(strip=True)
        title = row.bbs_title.get_text(strip=True)
        title = clean_string(title)
        content = row.bbs_conts.get_text(strip=True)
        content = clean_string(content)
        date = row.bbs_supply_dt.get_text(strip=True)
        url = "http://www.yangcheon.go.kr/site/yangcheon/ex/bbs/List.do?cbIdx=254"
        tmp_article = Article(number, title, content, date[0:10], url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    gds = get_yangchun(5)
    for gd in gds:
        gd.print_article()