from article.dobong import get_dobong
from article.seocho import get_seocho
from article.gwanak import get_gwanak
from article.dongdaemun import get_ddm
from article.dongjak import get_dongjak
from article.gangdong import get_gangdong
from article.seodaemun import get_seodaemun
from article.songpa import get_songpa
from article.yangchun import get_yangchun


def get_articles(gu, article_count):
    gus = {'dongdaemun': get_ddm, 'dongjak': get_dongjak, 'gangdong': get_gangdong, 'gwanak': get_gwanak,
           'seodaemun': get_seodaemun, 'songpa': get_songpa, 'yangchun': get_yangchun, 'seocho': get_seocho,
           'dobong': get_dobong}
    if gu in gus.keys():
        return gus[gu](article_count)
    else:
        print("올바른 구 이름을 입력하세요")
        exit()


if __name__ == "__main__":
    gus = ['gwanak', 'dobong', 'seocho', 'dongdaemun', 'dongjak', 'gangdong', 'seodaemun', 'songpa', 'yangchun']
    for gu in gus:
        print('*********************'+gu+'******************************')
        articles = get_articles(gu, 10)
        for article in articles:
            article.print_article()

