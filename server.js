var WebSocketServer = require('ws').Server;
var wss = new WebSocketServer({ port: 8000 });

wss.on('connection', function connection(ws) {
  console.log('connected to client');

  ws.on('message', function incoming(message) {
    console.log('from client: %s', message);
    msg = 'hello from javascript server';
    console.log('to client: %s', msg);
    ws.send(msg);
  });

  ws.on('close', function() {
    console.log('disconnected from client');
  });
});