var FB = require('fb');
var fs = require('fs');
var path = require('path');
const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'], keyspace: 'getfb' });
FB.options({version: 'v2.9'});
FB.setAccessToken('EAAYqwy2qDE4BAGuVIrOipLCE9yZCEa9U3fcueix0n5Q5TUibj1iur06ITSBWoTZBwq7VGGru7ZCKGGLMXZCiMfLGFKCpmsqpIIubhizCRz2HNJLwsMnNBOa6WCJti3MRDARlK6CTZA41gl1EKKbSeV0Ln5KtvkXDpZBUhYdgCGSZAiwsiWMc6CPc4UZBRDhRuCzMvRK6AuecZBAZDZD');
const query = 'SELECT * FROM add_neg ';
client.execute(query, function(err, result) {
  var all_data = result.rows;
  for(var value of all_data ){
  		var commentId = value.negative_comment;
		  FB.api(commentId,'delete', function (response) {
    	if (response && !response.error) {
        	console.log(response);
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