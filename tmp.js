 var FB = require('fb');
	var fs = require('fs');
	var path = require('path');
	FB.options({version: 'v2.9'});
	FB.setAccessToken('EAAYqwy2qDE4BABh8JCdPw2LYfK4gwZA8StEqZCc8B2pxVZC5YOIwDSmhuUXD9UjL7b0sA5lXePCFZCVkFDUygH8E01sESTPuSzkeDDxT0ZC6oPoXUi7llcxNXAdwvcEoS7UAvbHcQXi5efEH202KFSsIaxsWfAl6KCEcEEOwdjZCbOmfw0m2sMLJFJeOVPzrV7UMyFv9bVkgZDZD');
	var commentId = '321731461577308_352160511867736';
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