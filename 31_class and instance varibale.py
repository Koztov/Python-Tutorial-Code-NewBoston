class Factory:

    factory = "warehouse"  # class variable

    def __init__(self):     # instance variable
        self.food = 0

    def producer(self):
        self.food += 1

    def consumer(self):
        self.food -= 1

a = Factory()
print(a.food)
