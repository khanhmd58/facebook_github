const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'], keyspace: 'test' });
const params = [ '4', 'hello' ];
const query1 = 'INSERT INTO tmp (id_comment,comment) VALUES (?, ?)';
client.execute(query1, params, { prepare: true })
const query = 'SELECT id_comment,comment FROM tmp';
client.execute(query, function(err, result) {
  var row = result.rows;
  for(var data of row){
  	console.log(data.id_comment);
  	console.log(data.comment);  
  }
  process.exit(0);
});
