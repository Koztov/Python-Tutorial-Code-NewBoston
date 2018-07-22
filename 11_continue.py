

players = [12, 24, 45, 57, 77, 89, 95]
for p in range(100):
    if p in players:
        continue
    print(p)

# write the code to check all the elements in the list which is not divisible by 55






players = [12, 55, 45, 57, 77, 89, 110]
for p in players:
    if p % 55 == 0:
        continue
    print(p)
