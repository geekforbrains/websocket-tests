Websocket Tests
===============

A benchmark test between Python 3 and Nodejs websockets.

Candidates
- Python 3.5.1 / `pip websockets 3.0`
- Node 4.3.1 / `npm ws 1.0.1`
- Node 4.3.1 / `npm lws 0.2.1`

Test Server
- AWS m3.medium
- Artillery 1.3.4


Results
=======

The full results provided by Artillery are located in the `results/` directory.

Here are the key metrics:


Running Tests
=============

Tests are done using [Artillery]. The test configs are found in the `artillery.json` file.

Each time a test was ran, I would boot-up the individual server for testing. All 
of them listen on the same port. All servers do the same thing; echo back a message.

Start Server

```
node lws_server.js
// waiting for connections...
```

Run Tests

```
artillery quick -60 -r 10 ws://testserver:8000
```


[Artillery]: https://github.com/shoreditch-ops/artillery
