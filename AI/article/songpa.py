from article.Article import Article, clean_ptags, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/SpNotice/1/{}/".format(article_count)
    return clean_xml(url)


def get_songpa(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.seq.get_text(strip=True)
        title = row.title.get_text(strip=True)
        title = clean_string(title)
        content = row.content.find_all("p")
        content = clean_ptags(content)
        content = clean_string(content)
        try:
            date = row.reg_date.get_text(strip=True) #송파구 날짜 이상함
        except AttributeError:
            date = "NULL"
        url = "http://www.songpa.go.kr/user.kdf?a=songpa.openadmin.news.NewsApp&c=1001&code=1&cate_id=AG0401000000"
        tmp_article = Article(number, title, content, date[0:10], url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    gds = get_songpa(5)
    for gd in gds:
        gd.print_article()