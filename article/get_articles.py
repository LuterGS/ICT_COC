from article.dobong_seocho_nowon import get_dsn
from article.gwanak import get_gwanak


def get_articles(gu, article_count):
    gu_names = ["gwanak", "dobong", "seocho", "nowon"]

    if gu == gu_names[0]:
        return get_gwanak(article_count)
    elif gu in gu_names:
        return get_dsn(gu, article_count)
    else:
        print("\"gwanak\" \"dobong\" \"seocho\" \"nowon\" 중 하나를 함수의 인자로 주세요")


if __name__ == "__main__":
    gwanaks = get_articles("gwanak", 5)
    for article in gwanaks:
        article.print_article()
    dobongs = get_articles("dobong", 5)
    for article in dobongs:
        article.print_article()
    seochos = get_articles("seocho", 5)
    for article in seochos:
        article.print_article()
    nowons = get_articles("nowon", 5)
    for article in nowons:
        article.print_article()