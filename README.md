# ICT COC AI 공모전
> ## Team 세줄요약장인
> ### 방준식 : ChatBot (KakaoTalk & Discord)
> ### 이관석 : AI
> ### 이호현 : APP, DB
> ### 윤동근 : 데이터수집
>
## ChatBot
 1. KakaoTalk Chatbot   
 Kakao i open builder 이용 자연어 처리 가능
    * 00구 새소식   
       해당 지역의 새 소식과 함께 원본글 링크 버튼을 제공합니다.
    * 더보기   
        리스트 형태로 한번 호출할 때 마다 최신 순으로 3개의 소식을 제공합니다. 각 소식을 터치하면 원본글로 이동합니다.
    * 사용법   
        입력 가능한 명령어 종류를 안내합니다.
    * 제작자   
        제작자 정보와 GitHub 링크 버튼을 제공합니다.

 2. Discord Chatbot   
 Node.js의 Discord 모듈 사용
    * 00구 새소식   
        해당 지역의 새 소식을 제공합니다.
    * 더보기   
        한번 호출할 때 마다 최신 순으로 3개의 소식을 제공합니다.
    * 알림
        * 알림 켜/꺼 명령으로 매일 19시에 알림을 보내주는 기능입니다.
        * 알림 지역 00구 명령으로 알림 지역 설정 가능합니다.
    * 사용법   
        '/help', '도움말' 명령어도 가능합니다. 
    * 서울시 새소식 봇 정보   
        제작자 정보를 볼 수 있습니다.
        
        
## React-Native(with Expo Framework, 이하 Expo)

1.1 개요

 * Expo 를 이용한 Android 앱 개발
   
1.2 기능

 * 현재 총 9개의 구(관악,도봉,송파 등)의 새소식을 Node.js 서버와의 통신을 통해 받아온다.
    
 * 임의의 구의 새소식을 구 별로 최신 10개 순으로 제공한다.
  
 * 임의의 구의 목록을 제공해, 원하는 구의 새소식을 볼 수 있다.
 
 * 원문보기 터치시 해당 글의 원본 웹 사이트로 이동한다.(단, API에서 원본 글의 URL을 제공하지 않는 경우 해당 구의 홈페이지 URL 제공)
    
 * 새로고침 기능 제공한다.(화면을 아래로 당길 시)
     
     
     
## Node.js(with MariaDB)

1.1 개요

 * Node.js(on Rasberry Pi) 를 이용한 서버 구축
 
 1.2 기능
 
 * 임의의 구의 새소식이 저장된 MariaDB 서버와 연동
 
 * React-Native로 제작된 App과의 통신을 통해 DB서버에 저장된 데이터를
   App 에 전송한다.
   
 * App 과의 통신에서 받은 구 이름으로 특정 구에 대한 정보만 App에게 전송한다.


## 데이터 수집(ICT_COC/AI/article)

1.1 개요

 * Python(Requests, Beautifulsoup)을 이용해 구별 공지사항 데이터 수집, xml parsing, 및 정리
 
 * 주기적으로 공지사항 데이터가 업데이트 되는 9개 구 지원
 
 1.2 기능
 
 * 서울시공공데이터포털 Open API로부터 데이터 획득 및 필요 데이터 추출
 
 * 데이터의 DB 저장을 위해 구별로 데이터 형태 통일
   
 * 데이터에 포함된 불필요한 문자열 정리 및 잘못된 데이터 수정
 
 * 함수 하나로 손쉽게 원하는 구의 데이터를 불러올 수 있도록 코드 작성
 
 1.3 예시 코드
 ```python
from AI.article.get_articles import get_articles
gwanak_articles = get_articles("gwanak", 5) #관악구의 최신 글 5개를 통일 된 형식으로 반환
```