from AI.summarize.summary import line3_summary
from article.get_articles import get_articles
from DB.main import query_mysql
import time


def get_onetool(location="nowon", length=10, db_name="news_2", sentence_tokenizer="kss + re", decay_factor=0.85, max_iteration_num=15):
    articles = get_articles(location, length)
    for article in articles:
        article.content, hashtag_string = line3_summary(article.content, sentence_tokenizer, decay_factor, max_iteration_num)
        # print(article.url)
        # print(article.content)
        query_mysql(db_name, article.number, article.title, article.content, article.date, article.url, hashtag_string)


if __name__ == "__main__":
    gus = ['gwanak', 'dobong', 'seocho', 'dongdaemun', 'dongjak', 'gangdong', 'seodaemun', 'songpa', 'yangchun']
    while True:
        for gu in gus:
            get_onetool(gu, 10, gu)
        time.sleep(3600)
