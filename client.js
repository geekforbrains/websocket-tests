var WebSocket = require('ws');
var ws = new WebSocket('ws://localhost:8000');
 
ws.on('open', function open() {
  console.log('connected to server');
  var msg = 'to server: hello from node client';
  console.log(msg);
  ws.send(msg);
});
 
ws.on('message', function(data, flags) {
  console.log('from server: %s', data);
});

ws.on('close', function() {
  console.log('disconnected from server');
});