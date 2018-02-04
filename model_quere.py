# Created by yhwang on 2017/8/2.
import queue

q = queue.Queue(50)
q.put(1)
q.put(2)# put也是会卡住的
print(q.qsize())
print(q.get())
print(q.get())
# print(q.get(timeout=5))# 没有数据时会直接等待 get_nowait不会等待,但是如果没有取到时就报错

q1 = queue.LifoQueue(50)# 后入先出队列

q2 = queue.PriorityQueue(50)
q2.put((10,'yhwang'))
q2.put((9,'yhwang1'))
