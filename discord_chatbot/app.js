const Discord = require('discord.js');
const client = new Discord.Client();
const axios = require('axios');

real_token = ' ';
test_token = ' ';

allow = ['관악구', '도봉구', '서초구'];
help_str = ['/help', '도움말', '사용법'];
data = [];
select = '';
index = 0;
user_alert = false;
today_alert = false;
alert_select = '관악구';

function getData(input_city, msg){
  axios.post('http://175.193.68.230/sendData', {
    city: input_city
  })
  .then(function (response) {
    data = response.data;
    msg.reply(' [' + input_city + ' 새소식] '+ '\n제목 : ' + data[0].title + '\n내용 : ' + data[0].content);
    index = 0;
  })
  .catch(function (error) {
    console.log(error);
  });
}

function send_alert(msg){
  if(user_alert){
    var date = new Date();
    console.log(date.getSeconds());
    if(date.getSeconds() == 19 && !today_alert){
      msg.channel.send('19초 알림 (19시 알림으로 변경 예정)')
      getData(alert_select, msg);
      today_alert = true;
    }
    if(date.getSeconds() == 23) today_alert = false;
  }
}

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);

});


client.on('message', msg => {
  if (msg.content === '서울시 새소식 봇 정보') {
    msg.reply('ICT COC AI 공모전 - 세줄요약장인 팀 \n방준식 : Chat Bot (KakaoTalk & Discord) \n이관석 : AI \n이호현 : APP \n윤동근 : DB');
  }

  if (msg.content.slice(0, 2) === '알림') {
    let command =  msg.content.split(' ');
    if(command[1].slice(0, 1) === '켜') {
      user_alert = true;
      today_alert = false;
      msg.reply('19초 알림을 켭니다. (19시 알림으로 변경 예정)');
      msg.reply('현재 알림 설정된 지역은 ' + alert_select + '입니다. 지역 변경은 [알림 지역 (지역이름)] 명령으로 가능합니다.');
      setInterval(send_alert.bind(null, msg), 1000);
    }
    if(command[1].slice(0, 1) === '꺼') {
      user_alert = false;
      msg.reply('알림을 끕니다.');
    }
    if(command[1] === '지역'){
      if(allow.indexOf(command[2]) == -1){
        msg.reply('서비스되지 않는 지역입니다.');
      }
      else{
        alert_select = command[2];
        msg.reply('알림 지역을 ' + alert_select + '로 변경했습니다.');
      }
    }
  }

  
  if (msg.content.slice(-3) === '새소식'){
    if(allow.indexOf(msg.content.split(' ')[0]) == -1){
      msg.reply('서비스되지 않는 지역입니다.');
    }
    else{
      select = msg.content.split(' ')[0];
      getData(select, msg);
    }
  }

  if (msg.content === '더보기') {
      if(select != ''){
          let max = data.length;
          for (var i = index; i < index + 3; i++) {
            if(i <= max){
              msg.reply('날짜 : ' + data[i].date + '\n제목 : ' + data[i].title + '\n내용 : ' + data[i].content.slice(0,1000) + '\n__________');
            }
            else{
              msg.reply('더 볼 수 있는 소식이 없습니다.');
              break;
            }
          }
          index += 3;
      }
      else{
        msg.reply('지역을 먼저 선택해주세요.');
      }
  }

  if(help_str.indexOf(msg.content) > 0){
    msg.reply('[챗봇 사용법]\n1. "00구 새소식" 명령으로 해당 구의 새 소식을 확안할 수 있습니다.\n2. "더보기" 명령으로 새 소식을 3개씩 더 볼 수 있습니다.\n3. "알림 켜/꺼" 명령으로 알림을 켜고 끌 수 있습니다. 또한 "알림 지역 00구" 명령으로 알림 설정된 지역 변경이 가능합니다.')
  }

});

client.login(test_token);
