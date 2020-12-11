from copy import deepcopy

with open("day11input.txt") as f:
    my_string = f.read().strip()

rows = [[seat for seat in row] for row in my_string.split("\n")]

n_rows = len(rows)
n_cols = len(rows[0])


def get_adjacent_seats(row, col, current_rows):
    seats = []
    r_to_check = [row-1, row, row+1]
    c_to_check = [col-1, col, col+1]
    r_to_check = [r for r in r_to_check if r != -1 and r != n_rows]
    c_to_check = [c for c in c_to_check if c != -1 and c != n_cols]

    for r in r_to_check:
        for c in c_to_check:
            seats.append(current_rows[r][c])

    seats.remove(current_rows[row][col])

    return seats


direction_vectors = [{'r': i, 'c': j} for i in range(-1,2) for j in range(-1,2) if [i, j] != [0, 0]]


def get_directional_seats(row, col, current_rows):
    seats = []
    for d in direction_vectors:
        target = {'r': row, 'c': col}
        searching = True
        while searching:
            target['r'] += d['r']
            target['c'] += d['c']

            if target['r'] in range(0, n_rows) and target['c'] in range(0, n_cols):
                if not current_rows[target['r']][target['c']] == '.':
                    seats.append(current_rows[target['r']][target['c']])
                    searching = False
            else:
                searching = False

    return seats


if __name__ == '__main__':
    updated = True
    current_rows = deepcopy(rows)

    for row in current_rows:
        print(''.join(row))

    while updated:
        updated = False
        next_rows = deepcopy(current_rows)

        for row in range(n_rows):
            for col in range(n_cols):
                current_seat = current_rows[row][col]
                if current_seat == '.':
                    next_rows[row][col] = '.'
                    continue
                adjacent_seats = get_directional_seats(row, col, current_rows)

                if current_seat == 'L':
                    if adjacent_seats.count('#') == 0:
                        next_rows[row][col] = '#'
                        updated = True
                    else:
                        next_rows[row][col] = 'L'

                elif current_seat == '#':
                    if adjacent_seats.count('#') >= 5:
                        next_rows[row][col] = 'L'
                        updated = True
                    else:
                        next_rows[row][col] = '#'

                else:
                    print("NO MATCH FOR SEAT TYPE ERROR ERROR ERROR")

        current_rows = deepcopy(next_rows)

        print('----')
        for row in current_rows:
            print(''.join(row))

    count = 0
    for row in current_rows:
        for seat in row:
            if seat == '#':
                count += 1

    print(count)
