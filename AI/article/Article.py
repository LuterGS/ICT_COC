import requests
import json
from bs4 import BeautifulSoup


class Article:
    def __init__(self, number, title, content, date, url):
        self.number = number  # 글 번호 String
        self.title = title  # 게시 제목 String
        self.content = content  # 글 내용 String
        self.date = date  # 게시 날짜 String
        self.url = url  # 게시글 링크 String
    
    # 신규 글인지 아닌지 확인
    def is_duplicate(self, url):
        response = requests.get(url)
        jsn = json.loads(response.text)
        latest_num = jsn[0]['number']
        if latest_num >= int(self.number):
            return True
        else:
            return False

    def print_article(self):
        print("--------------------------------------")
        print("number: ", self.number)
        print("title: ", self.title)
        print("content: ", self.content)
        print("date: ", self.date)
        print("url: ", self.url)


# xml <p> 태그 정리
def clean_ptags(ptags):
    result = ""
    for ptag in ptags:
        text = ptag.get_text(strip=True)
        text = text.replace(u'\xa0', u' ')
        if len(text):
            result = result + text + " "
    return result


def clean_xml(url, parse='html.parser'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    pretty_xml = soup.prettify(formatter=None)
    pretty_soup = BeautifulSoup(pretty_xml, parse)
    rows = pretty_soup.find_all("row")
    return rows


def clean_string(string):
    string = string.replace("'", "''")
    string = string.replace('"', '\"')
    string = string.replace('lt', '')
    string = string.replace('gt', '')
    return string