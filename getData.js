var logger = require('morgan');
var http = require('http');
var bodyParser = require('body-parser');
var express = require('express');
var FB = require('fb');
var fs = require('fs');
var path = require('path');
var request = require("request");
var app = express();
var server = http.createServer(app);
const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'], keyspace: 'test' });
app.use(logger('dev'));
app.use(bodyParser.json());
FB.options({version: 'v2.9'});
FB.setAccessToken('EAACZBaYXWHJoBAITE0KB4iGhvT0nLBHsuJOXZCXMCLqLlu0S1wZBi1ZCovCRBTD2gKICsy0KnhkI3204lcWV5AJ5AhFNY0teKmrZB1Un9V6lFMZAEr3l89m4bqQZC41IrwlzYhgphjou7ieBy6LXyiqLG1XDnW9EEQZD');
// Đây là đoạn code để tạo Webhook
app.get('/', (req, res) => {
  res.send("Home page. Server running okay.");
});
app.get('/webhook', function(req, res) {
  if (req.query['hub.verify_token'] === 'lay_comment') {
    res.send(req.query['hub.challenge']);
  }
  res.send('Error, wrong validation token');
});
// Xử lý khi có comment
app.post('/webhook', function(req, res) {
	var entries = req.body.entry;
  	for(var data of entries){
  		var entries = data.changes;
  		for(var data2 of entries){
  			var data_core = data2.value;
  			var commentID = data_core.comment_id;
  			var message = data_core.message;
        if(commentID && message ){
            const params = [ commentID, message ];
            const query = 'INSERT INTO tmp (id_comment,comment) VALUES (?, ?)';
            client.execute(query, params, { prepare: true });
            console.log(commentID);
        }
  		}
  	}
res.status(200).send("OK");
});

app.set('port', process.env.OPENSHIFT_NODEJS_PORT || process.env.PORT || 8081);
app.set('ip', process.env.OPENSHIFT_NODEJS_IP || process.env.IP || "127.0.0.1");
server.listen(app.get('port'), app.get('ip'), function() {
  console.log("Server waiting data with IP: %s || PORT: %d", app.get('ip'), app.get('port'));
});