# init is like a constructor

class Tuna:
    def __init__(self):
        print("Hello1")

    def swim(self):
        print("Hello2")


t = Tuna()
t.swim()


class Factory:
    def __init__(self, x):
        self.food = x

    def producer(self):
        self.food += 1

    def consumer(self):
        self.food -= 1

    def display(self):
        print(self.food)


a = Factory(100)
b = Factory(150)

a.producer()
a.producer()
b.producer()
b.producer()
b.producer()
a.display()
b.display()
