const Discord = require('discord.js');
const client = new Discord.Client();
const axios = require('axios');
const { send } = require('process');

real_token = ' ';
test_token = ' ';

data = [];
select = '';
index = 0;
user_alert = false;
today_alert = false;

function getData(input_city, msg){
  axios.get('http://175.193.68.230/sendData', {
    city: input_city
  })
  .then(function (response) {
    data = response.data;
    msg.reply(' [' + input_city + ' 새소식] ');
    msg.reply('제목 : ' + data[0].title);
    msg.reply('내용 : ' + data[0].content);
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
      today_alert = true;
    }
    if(date.getSeconds() == 23) today_alert = false;
  }
}

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);

});


client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }

  if (msg.content.slice(0, 2) === '알림') {
    let onoff =  msg.content.split(' ')[1];
    if(onoff.slice(0, 1) == '켜') {
      user_alert = true;
      today_alert = false;
      msg.reply('19초 알림을 켭니다. (19시 알림으로 변경 예정)');
      setInterval(send_alert.bind(null, msg), 1000);
    }
    if(onoff.slice(0, 1) == '꺼') {
      user_alert = false;
      msg.reply('알림을 끕니다.');
    }
  }

  
  if (msg.content.slice(-3) === '새소식'){
    select = msg.content.split(' ')[0];
    getData(select, msg);
  }

  if (msg.content === '더보기') {
      if(select != ''){
          for (var i = index; i < index + 3; i++) {
            msg.reply('날짜 : ' + data[i].date);
            msg.reply('제목 : ' + data[i].title);
            msg.reply('내용 : ' + data[i].content.slice(0,1000));
            msg.reply('__________');
          }
          index += 3;
      }
      else{
        msg.reply('지역을 먼저 선택해주세요.');
      }
  }

});

client.login(test_token);
