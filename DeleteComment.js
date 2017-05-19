var FB = require('fb');
	var fs = require('fs');
	var path = require('path');
	FB.options({version: 'v2.9'});
	FB.setAccessToken('EAACZBaYXWHJoBAITE0KB4iGhvT0nLBHsuJOXZCXMCLqLlu0S1wZBi1ZCovCRBTD2gKICsy0KnhkI3204lcWV5AJ5AhFNY0teKmrZB1Un9V6lFMZAEr3l89m4bqQZC41IrwlzYhgphjou7ieBy6LXyiqLG1XDnW9EEQZD');
	var commentId = '317498452000609_317502362000218';
	FB.api(commentId,'delete', function (response) {
      if (response && !response.error) {
        console.log(response);
      }
    }
);
	// if(message == "xin chào"){
	// 			FB.api(commentID,'delete', function (response) {
	// 			    if (response && !response.error) {
	// 			    	console.log(response);
	// 			    }
	// 			});
 //  			} else{
 //  				continue;
 //  			}