from krwordrank.word import KRWordRank
from krwordrank.hangle import normalize
from konlpy.tag import Okt
import kss
import re

def line3_summary(text, sentence_tokenizer="re", decay_factor=0.85, max_iteration_num=15):
    splited_sentence, splited_sentence_num = __get_splited_sentence(text, sentence_tokenizer)
    keyword = __get_keyword(splited_sentence, decay_factor, max_iteration_num)
    if keyword == "NULL" == 0:
        print("문장 요약 실패")
        return text
    print(keyword)
    result = __get_score(splited_sentence, splited_sentence_num, keyword)
    final_result = result[0][1] + "\n" + result[1][1] + "\n" + result[2][1]
    return final_result


def __get_splited_sentence(whole_text, sentence_tokenizer="re"):

    if type(whole_text) == list:
        splited = [normalize(sentence, english=True, number=True) for sentence in whole_text]
        splited_num = len(splited)
        return splited, splited_num

    if sentence_tokenizer == "re":
        splited = re.split("[.!?] ", whole_text.replace("\n", "")[:-1])
    elif sentence_tokenizer == "kss":
        splited = kss.split_sentences(whole_text.replace("\n", ""))
    elif sentence_tokenizer == "enter":  # 아직 구현중, normalize 부분으로 찾으면 될거같은데...
        splited = whole_text.split("\n")
    elif sentence_tokenizer == "jum":
        splited = whole_text.split(".")
    splited = [normalize(sentence, english=True, number=True) for sentence in splited]
    print(splited)
    splited_num = len(splited)

    return splited, splited_num

def __get_keyword(splited_sentence, decay_factor, max_iteration_num):
    try:
        pick_keyword = KRWordRank(min_count=4, max_length=10, verbose=True)
        decay_factor = decay_factor  # 이 단어가 계속 선호하는 단어인지 (소멸되지 않을 확률), 보통 85%로 잡는다.
        max_iteration_num = max_iteration_num  # 최대 반복횟수
        keyword, _, _ = pick_keyword.extract(splited_sentence, decay_factor, max_iteration_num)  # 키워드 추출
    except FileNotFoundError:
        keyword = "NULL"
    finally:
        return keyword


def __get_score(splited_sentence, splited_num, keywords):
    split_score_list = [[i, splited_sentence[i], 0] for i in range(splited_num)]
    for keyword in list(keywords.keys()):
        for i in range(splited_num):
            split_score_list[i][2] += split_score_list[i][1].count(keyword) * keywords[keyword]

    result_sliced = sorted(split_score_list, key=lambda split_score_list: split_score_list[2], reverse=True)[0:3]
    result_sliced = sorted(result_sliced, key=lambda result_sliced: result_sliced[0])

    return result_sliced
