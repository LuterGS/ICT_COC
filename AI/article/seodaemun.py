from article.Article import Article, clean_ptags, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/SdmBoardNotice/1/{}/".format(article_count)
    return clean_xml(url)


def get_seodaemun(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.sdm_board_seq.get_text(strip=True)
        title = row.title.get_text(strip=True)
        title = clean_string(title)
        content = row.conts.find_all("p")
        content = clean_ptags(content)
        content = clean_string(content)
        date = row.reg_dt.get_text(strip=True)
        url = "https://www.sdm.go.kr/news/news/notice.do"
        tmp_article = Article(number, title, content, date[0:10], url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    gds = get_seodaemun(5)
    for gd in gds:
        gd.print_article()