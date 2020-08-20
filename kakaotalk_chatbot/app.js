const http = require('http');
const express = require('express');
const axios = require('axios');

var app = express();
app.use(express.json());

const port = 8080;

var allow = ['관악구', '도봉구', '서초구']
var data = [];
var index = 1;
var selected_city = '';


function getData(input_city, res){
  axios.post('http://175.193.68.230/sendData', {
    city: input_city
  })
  .then(function (response) {
    selected_city = input_city;
    data = response.data;
    index = 1;
    res.send({
      version: "2.0",
      template: {
        outputs: [
            {
              "basicCard": {
                "title": "[" + input_city + "] " + data[0].title,
                "description": data[0].content,
                "buttons": [
                  {
                    "action":  "webLink",
                    "label": "원본 링크",
                    "webLinkUrl": data[0].url
                  }
                ]
              }
            }
          
        ]
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  });
}

app.post("/news", function(req, res) {
  var city = req.body.action.params.city;
  if(allow.indexOf(city) !== -1){
    getData(city, res);
  }
  else{
    selected_city = '';
    res.send({
      version: "2.0",
      template: {
        outputs: [
          {
            simpleText: {
              text: city + "는 서비스 준비중인 지역입니다. \n현재 서비스 가능 지역은 관악구, 도봉구, 서초구 입니다."
            }
          }
        ]
      }
    });
  }
    
});

app.post("/more", function(req, res){
  if(selected_city !== ''){
    let max = data.length;
    if(index+2 < max){
      res.send({
        version: "2.0",
        template: {
          outputs: [
            {
              listCard: {
                header: {
                  title: selected_city + " 새소식 더보기"
                },
                items: [
                  {
                    title: data[index].title,
                    description: data[index].content,
                    link: {
                      web: data[index].url
                    }
                  },
                  {
                    title: data[index+1].title,
                    description: data[index+1].content,
                    link: {
                      web: data[index+1].url
                    }
                  },
                  {
                    title: data[index+2].title,
                    description: data[index+2].content,
                    link: {
                      web: data[index+2].url
                    }
                  }
                ]
              }
            }
          ]
        }
      })
      index += 3;
    }
    else{
      res.send({
        version: "2.0",
        template: {
          outputs: [
            {
              simpleText: {
                text: "더 이상 볼 수 있는 소식이 없습니다."
              }
            }
          ]
        }
      });
    }
  }
  else{
    res.send({
      version: "2.0",
      template: {
        outputs: [
          {
            simpleText: {
              text: "00구 새소식 명령으로 지역을 먼저 선택해 주세요."
            }
          }
        ]
      }
    });
  }
  
})

app.listen(port, function() {
	console.log("server start");
});


app.get('/', (req, res) => {
  res.send('서울시 새소식 카카오톡 챗봇 API 서버');
})

