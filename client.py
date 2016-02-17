#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8000') as websocket:
        try:
          print("connected to server")

          msg = "hello from python client"
          print("to server: {0}".format(msg))
          await websocket.send(msg)

          while True:
              msg = await websocket.recv()
              print("from server: {0}".format(msg))
        except websockets.exceptions.ConnectionClosed:
            print('disconnected from server')


asyncio.get_event_loop().run_until_complete(hello())