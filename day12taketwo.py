with open("day12input.txt") as f:
    my_string = f.read().strip()

instructions = [(r[0], int(r[1:])) for r in my_string.split("\n")]

if __name__ == '__main__':
    wpx = 10
    wpy = -1
    x = 0
    y = 0

    for action, value in instructions:
        if action == 'N':
            wpy -= value
        elif action == 'S':
            wpy += value
        elif action == 'E':
            wpx += value
        elif action == 'W':
            wpx -= value
        elif action == 'R':
            for _ in range(value//90):
                wpx, wpy = wpy, wpx
                wpx *= -1
        elif action == 'L':
            for _ in range(value//90):
                wpx, wpy = wpy, wpx
                wpy *= -1
        elif action == 'F':
            x += wpx * value
            y += wpy * value
        else:
            print("SOMETHING IS HORRIBLY WRONG!!")
            print(action)

    print(abs(x) + abs(y))
