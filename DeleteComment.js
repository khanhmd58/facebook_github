var FB = require('fb');
var fs = require('fs');
var path = require('path');
const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'], keyspace: 'getfb' });
FB.options({version: 'v2.9'});
FB.setAccessToken('EAAYqwy2qDE4BAEv9eLznhgZAUTK5XQUmGWhmNhwsykscpzsU02YPaUNR1aPhLwMXqaAgHWywRIw1ioOxE6jD8AXmrZBLDgaJJodqQxbhiKlXK7v1lGLJACyZCGXE6ZCXwZAYspaA4YEjDlNjPFZA3FH32nfJjhS9RZC3ZAZBV7Nhid6gv9O86afUPGx2KSKmcUnMBiQEF6R71VgZDZD');
const query = 'SELECT negative_comment FROM add_neg ';
client.execute(query, function(err, result) {
  var all_data = result.rows;
  for(var value of all_data ){
  		var commentId = value.negative_comment;
		  FB.api(commentId,'delete', function (response) {
    	  if (response && !response.error) {
        	console.log(response);
        	const query_del = "DELETE from add_neg WHERE negative_comment='"+ commentId + "'";
  			client.execute(query,{ prepare: true });
    	}
	});
  }
  client.shutdown();
});

	// if(message == "xin chào"){
	// 			FB.api(commentID,'delete', function (response) {
	// 			    if (response && !response.error) {
	// 			    	console.log(response);
	// 			    }
	// 			});
 //  			} else{
 //  				continue;
 //  			}
