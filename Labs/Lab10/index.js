var express = require('express')
var app = express()
var config = require('config')
var data = require("./widgets.json");


app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/', function(request, response) {
  response.send('<b>Hello World! My name is = <em>' + process.env.MYNAME + '</em <br /> My Node Environemnt is :' + config.util.getEnv('NODE_ENV') + '</em></b>' + 
  '<p><a href="/env">What Environment are you in?</a></p>'+
  '<p><a href="/api">Read API data.</a></p>')
})

app.get('/env', function(request, response) { 
    if (config.util.getEnv("NODE_ENV") === "Testing") {
            response.send('<b>You are working in the <em>TEST</em> environment.</b>')
        }  
else if (config.util.getEnv("NODE_ENV") === "HerokuTest") {
        response.send('<b>You are working in the <em>TEST</em> environment that is in Heroku.</b>')
      }  
else if (config.util.getEnv("NODE_ENV") === "Production") {
        response.send('<b>You are working in Production</b>')
      }
else {
        response.send('<b>Environment is unknown</b>')
  }
})

app.get('/api', function(request, response){
    response.writeHead(200, {"Content-Type": "text/json"});
    response.end(JSON.stringify(data));
})


app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
