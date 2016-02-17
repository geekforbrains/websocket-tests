#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
  print('connected to client')

  try:
    msg = await websocket.recv()
    print('from client: {}'.format(msg))

    greeting = 'hello from python server'
    print('to client: {0}'.format(greeting))
    await websocket.send(greeting)

    while True:
      new_msg = await websocket.recv()
      print('from client: {}'.format(new_msg))
  except websockets.exceptions.ConnectionClosed:
      print('disconnected from client')


start_server = websockets.serve(hello, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
