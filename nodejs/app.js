var express = require('express');
var app = express();
var mysql = require('./db/mysql.js');
var session = require('express-session');
var fs = require('fs');
var bodyParser = require('body-parser');
var path = require('path');
var convert = require('xml-js');
var request = require('request');
var http = require('http').createServer(app);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(express.static(path.join(__dirname, '/public')));
mysql.connect();

app.post('/sendData',function(req,res){

    var city = req.body.city;
    var sql;
    console.log(city);
    if(city == '관악구'){
         sql = 'SELECT * FROM gwanak ORDER BY number DESC LIMIT 10';
    }
    else if(city == '강동구'){
        sql = 'SELECT * FROM gangdong ORDER BY number DESC LIMIT 10';
    }
    else if(city == '동대문구'){
        sql = 'SELECT * FROM dongdaemun ORDER BY number DESC LIMIT 10';
    }
    else if(city == '도봉구'){
        sql = 'SELECT * FROM dobong  ORDER BY number DESC LIMIT 10';
    }
    else if(city == '서초구'){
        sql = 'SELECT * FROM seocho ORDER BY number DESC LIMIT 10';
    }
    else if(city == '송파구'){
        sql = 'SELECT * FROM songpa  ORDER BY number DESC LIMIT 10';
    }
    else if(city == '동작구'){
        sql = 'SELECT * FROM dongjak ORDER BY number DESC LIMIT 10';
    }
    else if(city == '서대문구'){
        sql = 'SELECT * FROM seodaemun ORDER BY number DESC LIMIT 10';
    }
    else if(city == '양천구'){
        sql = 'SELECT * FROM yangchun  ORDER BY number DESC LIMIT 10';
    }


    mysql.query(sql,function(err,result){
        if(err) console.log(err);
        else{
           console.log("send Data!");
           res.send(result);
        }
    });
});


//open server
app.get('/', function(req, res) {
    res.writeHead(200, {
        'Content-Type': 'text/html'
    });
    res.end(data);
});
app.listen(80, function() {
    console.log('ICT server on');
});


