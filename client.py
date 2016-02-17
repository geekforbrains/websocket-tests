#!/usr/bin/env python

import os
import sys
import time
import asyncio
from multiprocessing import Pool

import websockets

async def handler(pid, cid, messages):
  async with websockets.connect('ws://localhost:8000') as websocket:
    try:
      print("connected to server")

      for i in range(messages): 
        msg = "pid: {0} - client: {1} message #{2}".format(pid, cid, i)
        print("> {0}".format(msg))
        await websocket.send(msg)

        resp = await websocket.recv()
        print("< {0}".format(resp))
    except websockets.exceptions.ConnectionClosed:
        print('disconnected from server')


def connect(cid, messages=10):
  pid = os.getpid()
  asyncio.get_event_loop().run_until_complete(handler(pid, cid, messages))


if __name__ == '__main__':
  clients = int(sys.argv[1]) if len(sys.argv) >= 2 else 100
  concurrency = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
  messages = int(sys.argv[3]) if len(sys.argv) >= 4 else 1

  p = Pool(concurrency)
  # p.map(connect, [[x, messages] for x in range(clients)])
  start = time.time()
  p.map(connect, range(clients))
  end = time.time()
  elapsed = end - start
  rps = clients / elapsed

  print('-' * 30)
  print('Clients: {0}'.format(clients))
  print('Concurrency: {0}'.format(concurrency))
  print('Messages: {0}'.format(messages))
  print('-' * 30)
  print('Time: {0}'.format(elapsed))
  print('RPS: {0}'.format(rps))


