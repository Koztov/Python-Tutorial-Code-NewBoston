
def calculate(a, b, c):
    z = a + b + c
    print(z)

my_list = [1, 200, 1500]

calculate(my_list[0], my_list[1], my_list[2])
calculate(*my_list)
