class Factory:

    food = 0

    def producer(self):
        self.food += 1

    def consumer(self):
        self.food -= 1
a = Factory()

a.producer()
a.producer()
a.consumer()
print(a.food)
