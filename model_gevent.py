# Created by yhwang on 2017/8/6.
import time
import select
import socket
import sys
import queue

server = socket.socket()
server.bind('localhost',90000)
server.listen(1000)
server.setblocking(False)

inputs = [server,]
outputs = []

select.select(inputs, outputs, inputs)
server.accept()