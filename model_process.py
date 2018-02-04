# Created by yhwang on 2017/7/30.
# 进程示例
import multiprocessing
import time
import threading
import os

# import Pipes
# ssh客户端
# import paramiko
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='cl.salt.com',port='22',username='yhwang',password='123456')
# stdin,stderr,stdout = ssh.exec_command('ll')
#
#
# sct = paramiko.Transport('hostname','22')
# sct.connect(sername='yhwang',password='123456')
# sftp = paramiko.SFTPClient.from_transport(sct)
# sftp.put()
# sftp.get()

print("----多进程----")


def run(q):
    q.put(1)
    time.sleep(2)
    print("hello", multiprocessing.current_process())


def run1(pipe):
    pipe.send(123)


def f(d, l):
    pass


q = multiprocessing.Queue()
parent_conn, child_conn = multiprocessing.Pipe()  # send,recv可以相互接受和发送

# 队列
p = multiprocessing.Process(target=run, args=(q,))
p.start()
p.join()
print(q.get())  # 实际上是两个变量,只是有程序在不听相互同步

# 管道
p1 = multiprocessing.Process(target=run1, args=(child_conn,))
p1.start()
p1.join()
print(parent_conn.recv())

# manage--->可以在多个进程中共享的数据
with multiprocessing.Manager() as manage:
    d = manage.dict()
    l = manage.list()
    p_list = []
    for i in range(50):
        p = multiprocessing.Process(target=f, args=(d, l))
        p.start()
        p_list.append(p)

    for res in p_list:
        res.join()

        # 进程池
        # pool = multiprocessing.Pool(processes=5)
        # for i in range(10):
        #     pool.apply_async(target=f,args=(d,l),callback=run(q))
