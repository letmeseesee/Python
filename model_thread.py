# Created by yhwang on 2017/7/31.
import threading
import time
num = 1
# 互斥锁
Lock = threading.Lock()
# 信号量锁
# semaphore = threading.BoundedSemaphore(5)


def fun(count):
    Lock.acquire()
    global num
    print("thread %i" % count)
    time.sleep(2)
    num = num+1
    Lock.release()
    print("thread %i done" % count)


threads = list()
for n in range(500):
    thread = threading.Thread(target=fun, args=(n,))
    # thread.setDaemon(True)#主程序不会等待守护线程结束---->就是说无所谓了,主线程挂了,整个程序就挂了
    thread.start()
    threads.append(thread)

# 等待结果
for n in range(len(threads)):
    threads[n].join()

print("All finish")
print(num)
