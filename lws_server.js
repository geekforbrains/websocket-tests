var lws = require('lws');
var server = new lws.Server({ port: 8000 });

server.on('connection', function (socket) {
  console.log('connected to client');
});

server.on('message', function (socket, message, binary) {
  console.log(message.toString());
  server.send(socket, message, false);
});

server.on('close', function (socket) {
  console.log('disconnected from client');
});

console.log('Running server on port 8000');