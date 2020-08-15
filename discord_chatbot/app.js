const Discord = require('discord.js');
const client = new Discord.Client();
const axios = require('axios');

real_token = ' ';
test_token = ' ';

data = [];
select = '';
index = 0;

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

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
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
