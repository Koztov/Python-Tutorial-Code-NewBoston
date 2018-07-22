class worker:

    def name(self):
        print("I am a worker")

class carpenter(worker):

    def name(self):
        print("I am a carpenter")

c = carpenter()
c.name()

