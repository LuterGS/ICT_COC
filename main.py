from AI.summarize.summary import line3_summary
from article.get_articles import get_articles
from DB.main import query_mysql


def get_onetool(location="gwanak", length=10, db_name="news_2", sentence_tokenizer="re", decay_factor=0.85, max_iteration_num=15):
    articles = get_articles(location, length)
    for article in articles:
        article.content = line3_summary(article.content, sentence_tokenizer, decay_factor, max_iteration_num)
        query_mysql(article.number, article.title, article.content, article.date, article.url, db_name)


if __name__ == "__main__":
    get_onetool()
