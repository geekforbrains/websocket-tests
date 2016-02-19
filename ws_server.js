var WebSocketServer = require('ws').Server;
var wss = new WebSocketServer({ port: 8000 });

wss.on('connection', function connection(ws) {
  console.log('connected to client');

  ws.on('message', function incoming(message) {
    console.log(message);
    ws.send(message);
  });

  ws.on('close', function() {
    console.log('disconnected from client');
  });
});