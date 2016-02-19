Websocket Tests
===============

A benchmark test between Python 3 and Nodejs websocket servers.

Candidates
- Python 3.5.1 / [Websockets 3.0][pyws]
- Node 4.3.1 / [ws 1.01][jsws]
- Node 4.3.1 / [lws 0.2.1][jslws]

Server & Method
- AWS m3.medium
- [Artillery] 1.3.4


Results & Conclusion
====================

The full results provided by Artillery are located in the `results/` directory.
I encourage you to open those HTML files for further reading.

The aggregate metrics are:

|                  | Python / Websockets | Node / WS | Node / LWS |
|------------------|---------------------|-----------|------------|
| Time (seconds)   | 240                 | 240       | 240        |
| Requests         | 63,864              | 65,348    | 66,618     |
| RPS              | 265.0               | 271.2     | 276.48     |
| HTTP Errors      | 0                   | 0         | 0          |
| Latency Min (ms) | 0.02                | 0.05      | 0.02       |
| Latency Max (ms) | 6.79                | 53.2      | 19.87      |
| Latency Med (ms) | 0.05                | 0.73      | 0.04       |

As you can see, all are quite comparable. I think the most notable things are
that both WS and LWS had weird latency issues. LWS spiked near the start of the test
and then it leveled out, even under higher load. WS on the other hand, got worse
over time. 

All have very close requests per second (RPS). LWS was the winner though, at 
11.48 RPS more than Python.

Based on these numbers, I would say you're good with either Javascript/Node or 
Python. All of them perform admirably. Use what you know and prefer ;)


Running The Tests
=================

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
artillery run artillery.json
```


[pyws]: https://websockets.readthedocs.org/en/stable/
[jsws]: https://www.npmjs.com/package/ws
[jslws]: https://www.npmjs.com/package/lws
[Artillery]: https://github.com/shoreditch-ops/artillery
