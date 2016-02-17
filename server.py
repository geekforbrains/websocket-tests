#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
  print('connected to client')

  try:
    while True:
      msg = await websocket.recv()
      print(msg)
      await websocket.send(msg)
  except websockets.exceptions.ConnectionClosed:
      print('disconnected from client')


start_server = websockets.serve(hello, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
