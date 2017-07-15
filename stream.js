var FB = require('fb');
var fs = require('fs');
var path = require('path');
const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'], keyspace: 'test' });
FB.options({version: 'v2.9'});
FB.setAccessToken('EAAYqwy2qDE4BAGuVIrOipLCE9yZCEa9U3fcueix0n5Q5TUibj1iur06ITSBWoTZBwq7VGGru7ZCKGGLMXZCiMfLGFKCpmsqpIIubhizCRz2HNJLwsMnNBOa6WCJti3MRDARlK6CTZA41gl1EKKbSeV0Ln5KtvkXDpZBUhYdgCGSZAiwsiWMc6CPc4UZBRDhRuCzMvRK6AuecZBAZDZD');
client.stream('SELECT * FROM add_neg')
  .on('readable', function () {
    // 'readable' is emitted as soon a row is received and parsed 
    var row;
    while (row = this.read()) {
      commentId = row.negative_comment;
      console.log(commentId);
      FB.api(commentId,'delete', function (response) {
      if (response && !response.error) {
         // console.log(response);
         // const query_del = "DELETE from add_neg WHERE negative_comment='"+ commentId + "'";
         // client.execute(query_del,{ prepare: true });
      }
      });
    }
  })
  .on('end', function () {
  //  client.shutdown(); 
  })
  .on('error', function (err) {
    // Something went wrong: err is a response error from Cassandra 
  });