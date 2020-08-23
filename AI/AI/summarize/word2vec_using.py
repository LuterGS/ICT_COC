from konlpy.tag import Hannanum, Okt
from gensim.models import Word2Vec

gisa = """iPhone 11 Pro 및 Pro Max는 18W 고속충전기를 기본으로 제공하는 데 반해, 11은 고속충전 자체는 지원하지만 고속 충전기가 아닌 여전히 5W 출력의 느린 완속 충전기를 
기본으로 지급하고 있다. 고속 충전을 하고 싶다면 직접 어댑터 39,000원, 케이블 1m 기준 25,000원으로 6만 4천 원에서 8만 4천 원을 들여서 구매해야 한다. 요즘은 굳이 애플에서 
사지 않아도 아이폰 및 다른 스마트폰들에 모두 쓸 수 있는 고속충전 어댑터가 시중에 많으므로 꼭 애플 공식 홈페이지에서 18W 혹은 30W 어댑터를 살 필요는 없으나 정품이 아닌 저가형 충전기를 사용했다가 
피봤다는 사례도 많아서 어느 정도 알아보고 사야하는 수고를 들여야한다. 안드로이드 진영에서 주로 사용하는 퀄컴 퀵차지는 기본적으로 퀄컴의 칩셋에서 사용되는 것을 전제로 개발된 규격이기 때문에 애플의 자체 칩셋을 
사용하는 애플 제품에서는 호환되지 않는다. 이를 모르고 타 안드로이드 폰의 번들 고속 충전기를 꽂으면 USB 충전 표준에 따라 5V×1A=5W의 기어가는 속도로 충전이 되는 불상사를 볼 수 있게 된다. 기껏 
고속 충전기라고 구매했다가 기본 번들 충전기나 다름없는 속도로 충전되는 셈. 이런 참사를 막기 위해서는 9V/2A 규격을 준수하는 USB-PD 2.0 규격의 충전기를 사용해야 한다. 비슷한 맥락에서 애플이 
기본으로 지급하는 Lightning Cable 을 보고 고속 충전기로 오해를 할 수 있는데, 한쪽 단자가 USB-C가 아니라 기존의 USB-A 단자로 되어있다면 그건 그냥 5W짜리 충전기이다. 적어도 애플 
기기에서 USB-PD를 사용한 고속충전은 무조건 입력 측 단자가 USB-C여야만 한다. 이에 반해 삼성과 LG 등은 모두 18W 이상의 고속 충전기를 기본 증정하고 있다. 다만 아이폰은 언제나 
타사 스마트폰보다 배터리의 양을 적게 탑재해도 그만큼 배터리의 소모도 적다는 옹호 의견도 있으나, 11 이전 아이폰의 배터리 타임은 이미 타사 대비 열세를 보이고 있었다. 더욱이 아이폰의 
배터리는 플러스 모델과 X 이후의 모델부터 급격이 증가하며 현재는 일반적인 안드로이드 스마트폰의 배터리인 3000 mAh 이상까지 올라왔으며 이미 5W로 커버할 수준이 아니라는 반론도 존재한다. 역시나 동급모델 
기준 충전 속도는 가장 느리다. 이미 아이폰 XS는 3시간, 아이폰 XS Max는 3시간 30분 가량에 달하는 엄청나게 긴 충전 시간을 보여주고 있었던 상황이었다! 10W 이상의 고속충전이 리튬이온 배터리의 
기대 수명을 해친다는 이야기가 나오고 있기 때문에 애플은 배터리가 8000 mAh가 넘어가는 아이패드나 맥북 등을 제외하고 아이폰은 아직 5W 충전기를 고수하려는 입장인 듯하다는 의견도 존재하나 이는 아이폰 
11 Pro의 경우 18W 고속충전기를 동봉해준 것을 설명할 수 없으므로 다소 무리가 있는 해석이다."""

splited = gisa.replace("\n", "").split(".")[:-1]
print(splited)

han = Hannanum()
okt = Okt()

han_tag = []
okt_tag = []
okt_noun = []

for texts in splited:
    han_tag.append(han.morphs(texts))
    okt_tag.append(okt.morphs(texts))
    okt_noun.append(okt.nouns(texts))


pretrained_model = Word2Vec.load("model/ko.bin")

# embedding_model = Word2Vec(sentences=okt_noun, size=30, window=2, min_count=3, workers=4, iter=100, sg=1)

similar_test = pretrained_model.wv.most_similar("충전")
print(similar_test)
