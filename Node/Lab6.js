let http = require("http");
let fs = require("fs");
let os = require("os");
let ip = require("ip");

http.createServer(function(req, res){
	if(req.url === "/"){
		fs.readFile("./public/index.html", "UTF-8", function(err, body){
			res.writeHead(200, {"Content-Type":"text/html"});
			res.end(body);
		});
	} else if (req.url.match("/sysinfo")){
		let myHostName = os.hostname();
		let myServerUptime = new Date(os.uptime());
	
		let uptimeDays = Math.floor(myServerUptime / (3600*24));
		let uptimeHours = Math.floor(myServerUptime % (3600*24) / 3600);
		let uptimeMinutes = Math.floor(myServerUptime % 3600 / 60);
		let uptimeSeconds = Math.floor(myServerUptime % 60);
		
		let totalMemory = (os.totalmem() / 1048576).toFixed(3); //this is the amount of bytes in a megabyte
		let freeMemory = (os.freemem() / 1048576).toFixed(3);
		
		let cpuCount = os.cpus().length;
		
		html=`
		<!DOCTYPE html>
		<html>
			<head>
				<title>Lab 6 Sysinfo</title>
			</head>
			<body>
				<p>Hostname: ${myHostName}</p>
				<p>IP: ${ip.address()}</p>
				<p>Server Uptime: Days: ${uptimeDays}, Hours: ${uptimeHours}, Minutes: ${uptimeMinutes}, Seconds: ${uptimeSeconds}</p>
				<p>Total Memory: ${totalMemory} MB</p>
				<p>Free Memory: ${freeMemory} MB</p>
				<p>CPUs: ${cpuCount}</p>
			</body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);
	}
	else{
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end('404 File Not Found at ${req.url}');
	}
}).listen(3000);

