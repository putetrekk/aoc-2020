with open("day3input.txt") as f:
    map = f.readlines()

for i in range(len(map)):
    map[i] = map[i][0:-1]

x = 0
encounters = 0

for i in range(0, len(map), 2):
    print(f'i: {i}, x: {x}')

    if map[i][x] == '#':
        encounters += 1

    x += 1
    if x >= len(map[i]):
        x %= len(map[i])


print(encounters)
