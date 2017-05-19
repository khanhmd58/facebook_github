console.log("hello world!");
var http = require('http'); // goi toi module can dung
http.createServer(function(request,response){
	response.writeHead(200);
	response.write('hello');
	response.end();
	console.log("client connected...");
}).listen(8080)
