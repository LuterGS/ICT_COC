from krwordrank.word import KRWordRank
from krwordrank.hangle import normalize
from konlpy.tag import Okt
import kss
import re

def line3_summary(text, sentence_tokenizer="re", decay_factor=0.85, max_iteration_num=15):
    original_splited, splited_sentence, splited_sentence_num = __get_splited_sentence(text, sentence_tokenizer)
    keyword = __get_keyword(splited_sentence, decay_factor, max_iteration_num)
    if keyword == "NULL" or len(keyword) == 0:
        print("문장 요약 실패")
        final_result = ""
        for text in original_splited:
            final_result += text + "\n"
        return final_result
    print(keyword)
    result_sentence_num = __get_score(splited_sentence, splited_sentence_num, keyword)
    final_result = ""
    for i in range(len(result_sentence_num)):
        final_result += original_splited[i] + "\n"

    return final_result


def __get_splited_sentence(whole_text, sentence_tokenizer="re"):
    """
    :param whole_text: 기사의 원문
    :param sentence_tokenizer: 어떤 tokenizer를 사용할 것인지
        re : . ? ! 3개를 기준으로 분리
        enter : 엔터로 구분
        jum : . 하나로 구분
        kss : kss 토크나이저 사용
        만약 특수기호가 있을 경우 특수기호 분류 후 kss 사용
    :return:
    """
    # print(whole_text)
    # 처음 입력이 리스트일 경우
    if type(whole_text) == list:
        splited = [normalize(sentence, english=True, number=True) for sentence in whole_text]
        splited_num = len(splited)
        return splited, splited_num

    # 문자열에 특수기호가 있을 경우
    special_character = ['○','□', '▣', '※', '①', '②', '③', '◇']
    special_counter = 0
    for special in special_character:
        special_counter += whole_text.count(special)
    if special_counter > 0:
        special_splited = re.split("[○□▣※◇①②③]", whole_text.replace("\n", "")[:-1])
        splited = []
        for sentence in special_splited:
            sentence = kss.split_sentences(sentence)
            if type(sentence) == list:
                for sentence_splited in sentence:
                    splited.append(sentence_splited)
            else:
                splited.append(sentence)
        sentence_tokenizer = "special_character"
        # print("TEST ", splited)

    if sentence_tokenizer == "re":
        splited = re.split("[.!?]", whole_text.replace("\n", "")[:-1])
    elif sentence_tokenizer == "kss":
        splited = kss.split_sentences(whole_text.replace("\n", ""))
    elif sentence_tokenizer == "enter":  # 아직 구현중, normalize 부분으로 찾으면 될거같은데...
        splited = whole_text.split("\n")
    elif sentence_tokenizer == "jum":
        splited = whole_text.split(".")

    splited = __get_limited_length_sentence(splited, 600)
    keyword_splited = [normalize(sentence, english=True, number=True) for sentence in splited]
    print(len(splited), splited)
    splited_num = len(splited)

    return splited, keyword_splited, splited_num

def __get_limited_length_sentence(sentences, max_length):
    sentences_result = []
    for sentence in sentences:
        if len(sentence) < max_length:
            sentences_result.append(sentence)
    return sentences_result

def __get_keyword(splited_sentence, decay_factor, max_iteration_num):
    try:
        pick_keyword = KRWordRank(min_count=4, max_length=10, verbose=True)
        decay_factor = decay_factor  # 이 단어가 계속 선호하는 단어인지 (소멸되지 않을 확률), 보통 85%로 잡는다.
        max_iteration_num = max_iteration_num  # 최대 반복횟수
        keyword, _, _ = pick_keyword.extract(splited_sentence, decay_factor, max_iteration_num)  # 키워드 추출
    except ValueError:
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
    result_num = [result_sliced[i][0] for i in range(len(result_sliced))]
    print(result_num)

    return result_num
