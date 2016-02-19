Websocket Tests
===============

A benchmark test between Python 3 and Nodejs websockets.

To install Python 3 on OSX, do:

```
brew install python3
pyvenv env
. env/bin/activate
pip install -r requirements.txt
```

For node, do:

```
npm install
```

Running Tests
=============

Tests are run using [Artillery]

```
artillery quick -60 -r 10 ws://localhost:8000
```

[Artillery]: https://github.com/shoreditch-ops/artillery
