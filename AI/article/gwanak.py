from article.Article import Article, clean_ptags, clean_xml, clean_string


# API에서 데이터 xml 획득 및 게시글 기준으로 정리
def get_data(article_count):
    url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/GwanakNewsList/1/{}/".format(article_count)
    return clean_xml(url)


def format_time(time):
    return time[0:4] + "-" + time[4:6] + "-" + time[6:8] + " " + time[8:10] + ":" + time[10:12] + ":" + time[12:14]


# xml을 parsing하여 게시글마다 Article 객체 생성 후 객체들을 리스트에 담아 반환
def get_gwanak(article_count):
    articles = []
    rows = get_data(article_count)
    for row in rows:
        number = row.seq.get_text(strip=True)
        title = row.title.get_text(strip=True)
        title = clean_string(title)
        ptags = row.content.find_all("p")
        content = clean_ptags(ptags)
        content = clean_string(content)
        origin_date = row.writeday.get_text(strip=True)
        date = format_time(origin_date)
        url = row.expanded_url.get_text(strip=True).replace(";", "")
        tmp_article = Article(number, title, content, date, url)
        articles.append(tmp_article)
    return articles  # Article 객체들을 담는 리스트


if __name__ == "__main__":
    #url = "http://openapi.seoul.go.kr:8088/766248667572616d373354516d6b42/xml/GwanakNewsList/1/{}/".format(5)
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #pretty_xml = soup.prettify(formatter=None)
    #pretty_soup = BeautifulSoup(pretty_xml, 'html.parser')
    #print(pretty_soup)

    gwanak_articles = get_gwanak(5)
    for gwanak_article in gwanak_articles:
        gwanak_article.print_article()
