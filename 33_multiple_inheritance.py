# over-loading is not possible
# over-riding is easily achieved

class student:
    def says(self):
        print("I am a student")

    def says(self, x):
        print(x)

class sportman:
    def says(self):
        print("I am a sportman")

class singer:
    def says(self):
        print("I am a singer")

class smart(student, sportman, singer):
    pass
s = smart()
s.says(52657)
