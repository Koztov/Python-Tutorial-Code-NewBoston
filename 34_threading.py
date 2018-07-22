import threading

class Demo(threading.Thread):
    def run(self):
        x = 0
        for _ in range(10):
            x += 1
            print(x)

x = Demo(name="Thread 1")
y = Demo(name="Thread 2")

x.start()
y.start()
