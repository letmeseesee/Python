# Created by yhwang on 2017/8/2.
import threading
import time

event = threading.Event()


def guide():
    count = 0
    while True:
        if count < 20:
            event.set()
            print("Green light is on......")
        elif 20 <= count < 30:
            event.clear()
            print("Red light is on.....")
        else:
            count = 0
        time.sleep(1)
        count = count + 1


def car():
    while True:
        if event.is_set():
            print("run")
        else:
            print("wait")
            event.wait()


light = threading.Thread(target=guide, args=())
light.start()
car = threading.Thread(target=car, args=())
car.start()
