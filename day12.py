import unittest

with open("day12input.txt") as f:
    my_string = f.read().strip()

instructions = [{'drn': r[0], 'dst': int(r[1:])} for r in my_string.split("\n")]

absolute_direction = ['N', 'E', 'S', 'W']
movement_vectors = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Ship1:
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


class Ship2:
    x = 0
    y = 0
    wpx = None
    wpy = None

    def __init__(self, wpx: int, wpy: int):
        self.wpx = wpx
        self.wpy = wpy

    def move(self, direction: str, value: int):
        if direction in absolute_direction:
            self.__move_wp(direction, value)
        elif direction == 'F':
            self.__move_forward(value)
        elif direction == 'R':
            self.__rotate_right(value//90)
        elif direction == 'L':
            self.__rotate_left(value//90)
        else:
            raise Exception("Unrecognised Instruction. Instruction: " + direction)

    def __move_wp(self, direction: str, distance: int):
        index = absolute_direction.index(direction)
        self.wpx += distance * movement_vectors[index][0]
        self.wpy += distance * movement_vectors[index][1]

    def __move_forward(self, distance: int):
        self.x += distance * self.wpx
        self.y += distance * self.wpy

    def __rotate_right(self, n: int):
        for _ in range(n):
            self.wpx, self.wpy = self.wpy * -1, self.wpx

    def __rotate_left(self, n: int):
        for _ in range(n):
            self.wpx, self.wpy = self.wpy, self.wpx * -1


class Ship2Tests(unittest.TestCase):
    integers = [-50, -9, 3, -1, 0, 1, 2, 7, 129]

    def test_initialization(self):
        wps = [{'x': wpx, 'y': wpy} for wpx in self.integers for wpy in self.integers]
        for wp in wps:
            s = Ship2(wp['x'], wp['y'])
            self.assertEqual(s.x, 0)
            self.assertEqual(s.y, 0)
            self.assertEqual(s.wpx, wp['x'])
            self.assertEqual(s.wpy, wp['y'])

    def test_sample(self):
        sample = [
            'W4',
            'F11',
            'L90',
            'E5',
            'L90',
            'F67',
            'W3',
            'S3',
            'F15',
            'E4',
        ]

        sample_instructions = [{'drn': r[0], 'dst': int(r[1:])} for r in sample]

        s = Ship2(0, 0)
        for inst in sample_instructions:
            s.move(inst['drn'], inst['dst'])

        self.assertEqual(s.wpx, 5)
        self.assertEqual(s.wpy, -2)
        self.assertEqual(s.x, 239)
        self.assertEqual(s.y, -365)

    def test_sample_2(self):
        sample = [
            'F18',
            'S3',
            'E4',
            'F97',
            'N2',
            'R90',
            'E5',
            'F79',
            'R180',
            'F12',
        ]

        sample_instructions = [{'drn': r[0], 'dst': int(r[1:])} for r in sample]

        s = Ship2(-5, -5)
        for inst in sample_instructions:
            s.move(inst['drn'], inst['dst'])

        self.assertEqual(s.wpx, -9)
        self.assertEqual(s.wpy, 1)
        self.assertEqual(s.x, 416)
        self.assertEqual(s.y, -351)

    def test_forward_movement(self):
        wps = [{'x': wpx, 'y': wpy} for wpx in self.integers for wpy in self.integers]
        for wp in wps:
            s = Ship2(wp['x'], wp['y'])
            s.move('F', 1)

            self.assertEqual(s.x, wp['x'])
            self.assertEqual(s.y, wp['y'])

            s = Ship2(wp['x'], wp['y'])
            s.move('F', 27)

            self.assertEqual(s.x, 27*wp['x'])
            self.assertEqual(s.y, 27*wp['y'])

    def test_right_rotation(self):
        s1 = Ship2(2, 1)
        s1.move('R', 90)
        self.assertEqual(s1.wpx, -1)
        self.assertEqual(s1.wpy, 2)

        s2 = Ship2(2, 1)
        s2.move('R', 180)
        self.assertEqual(s2.wpx, -2)
        self.assertEqual(s2.wpy, -1)

        s3 = Ship2(2, 1)
        s3.move('R', 270)
        self.assertEqual(s3.wpx, 1)
        self.assertEqual(s3.wpy, -2)

        s4 = Ship2(2, 1)
        s4.move('R', 360)
        self.assertEqual(s4.wpx, 2)
        self.assertEqual(s4.wpy, 1)

    def test_left_rotation(self):
        s1 = Ship2(2, 1)
        s1.move('L', 90)
        self.assertEqual(s1.wpx, 1)
        self.assertEqual(s1.wpy, -2)

        s2 = Ship2(2, 1)
        s2.move('L', 180)
        self.assertEqual(s2.wpx, -2)
        self.assertEqual(s2.wpy, -1)

        s3 = Ship2(2, 1)
        s3.move('L', 270)
        self.assertEqual(s3.wpx, -1)
        self.assertEqual(s3.wpy, 2)

        s4 = Ship2(2, 1)
        s4.move('L', 360)
        self.assertEqual(s4.wpx, 2)
        self.assertEqual(s4.wpy, 1)


if __name__ == '__main__':
    # unittest.main()

    ship = Ship2(10, -1)
    for i in instructions:
        ship.move(i['drn'], i['dst'])

    print(abs(ship.x) + abs(ship.y))
