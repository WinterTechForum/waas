const https = require('https');

var particleUrl = "https://api.particle.io/v1/devices/20002c000247343337373739/events\?access_token\=xxx";
var slackUrl = "https://slack.com/api/chat.postMessage?token=xxxx&channel=C0PUJPG2E&text=Drink%20being%20poured!&pretty=1";

function processResponse(response) {
  response.setEncoding('utf8');
  var str = "";
  response.on("data", function(data) {
    console.log(data);
    if (/drink_pour/.test(data)) {
	https.get(slackUrl, done);
    }
  });

  response.on("error", console.error);

  response.on("end", function() {
    console.log("closed connection to particle");
  });
}

function done(response) {
 console.log("response from slack");
}

https.get(particleUrl, processResponse);
