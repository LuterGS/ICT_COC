from AI.summarize.summary import line3_summary
from article.gwanak import get_gwanak

if __name__ == "__main__":
    gwanark_article = get_gwanak(5)
    summary3 = []
    for test in gwanark_article:
        summary3.append(line3_summary(test.content))
    print("\n\n\n")
    for i in range(5):
        print(gwanark_article[i].content)
        print(summary3[i])
        print("\n")