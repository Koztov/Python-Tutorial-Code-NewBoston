__author__ = 'Koztov'

players = [12, 24, 45, 57, 77, 89, 95]
print(players[0])

players[0] = 15
print(players)
print(players + [1, 2, 3])
print(players)

players.append(120)
print(players)
print(players[:2])

players[:2] = [0, 0]
print(players)

players[:2] = []        # remove selective elements
print(players)

players[:] = []         # remove all elements
print(players)
