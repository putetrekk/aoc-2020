with open("day12input.txt") as f:
    my_string = f.read().strip()

instructions = [{'drn': r[0], 'dst': int(r[1:])} for r in my_string.split("\n")]

absolute_direction = ['N', 'E', 'S', 'W']
movement_vectors = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Ship:
    direction = 1
    x = 0
    y = 0

    def move(self, direction, value):
        if direction in absolute_direction:
            self.__move_abs(direction, value)
        elif direction == 'F':
            self.__move_forward(value)
        elif direction == 'R':
            self.__rotate_right(value//90)
        elif direction == 'L':
            self.__rotate_left(value//90)
        else:
            raise Exception("Unrecognised Instruction. Instruction: " + direction)

    def __move_abs(self, direction, distance):
        index = absolute_direction.index(direction)
        self.x += distance * movement_vectors[index][0]
        self.y += distance * movement_vectors[index][1]

    def __move_forward(self, distance):
        self.x += distance * movement_vectors[self.direction][0]
        self.y += distance * movement_vectors[self.direction][1]

    def __rotate_right(self, n):
        self.direction = (self.direction + 1 * n) % 4

    def __rotate_left(self, n):
        self.direction = (self.direction + 3 * n) % 4


if __name__ == '__main__':
    ship = Ship()
    for i in instructions:
        ship.move(i['drn'], i['dst'])

    print(ship.x + ship.y)
