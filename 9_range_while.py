
for x in range(12, 34):
    print(x)

for x in range(20, 36, 5):
    print(x)

count = 12
while count < 15:
    print(count)
    count += 1

# write the code to find fibonacci series 0 1 1 2 3 5 8 .....
# write the code to find the multiplication table of 11

i = 0
for x in range(11, 111, 11):
    i += 1
    output = "11x" + i.__str__() + "=" + x.__str__()
    print(output)

