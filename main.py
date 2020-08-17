from AI.summarize.summary import line3_summary
from article.gwanak import get_gwanak
from DB.main import query_mysql

if __name__ == "__main__":
    gwanark_article = get_gwanak(5)
    summary3 = []
    for test in gwanark_article:
        summary3.append(line3_summary(test.content, sentence_tokenizer="jum"))
    print("\n\n\n")
    for i in range(5):
        # print(gwanark_article[i].content)
        #print(summary3[i])
        print("\n")

        query_mysql(gwanark_article[i].number, gwanark_article[i].title, summary3[i], gwanark_article[i].date, gwanark_article[i].url)
