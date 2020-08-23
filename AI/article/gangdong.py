from article.Article import Article, clean_ptags, clean_xml, clean_string


def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/GdTnBbs/1/{}/".format(article_count)
    return clean_xml(url)


def get_gangdong(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.ntt_sn.get_text(strip=True)
        title = row.ntt_sj.get_text(strip=True)
        title = clean_string(title)
        content = row.bbsctt_cn.find_all("p")
        content = clean_ptags(content)
        content = clean_string(content)
        date = row.regist_dt_hm.get_text(strip=True)
        url = "https://www.gangdong.go.kr/web/koRenew_3/app/uiList.do?ap=B1140&menuId=tpl:16234"
        tmp_article = Article(number, title, content, date[0:10], url)
        articles.append(tmp_article)
    return articles


if __name__ == "__main__":
    gds = get_gangdong(5)
    for gd in gds:
        gd.print_article()