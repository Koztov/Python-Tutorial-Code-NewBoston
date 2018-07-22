__author__ = 'Koztov'


def print_me():
    print("HI")
    val = convert_me(19)
    print "hi again", val

def convert_me(dollar):
    rupee = dollar * 50
    print(rupee)
    return rupee


def convert_return(dollar):
    rupee = dollar * 50
    return rupee


print_me()                      # case 1
convert_me(10)                  # case 2
value = convert_return(100)     # case 3
print(value)
