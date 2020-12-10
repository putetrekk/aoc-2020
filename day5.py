def get_index(string: str):
    length = len(string)
    if length == 0:
        return 0

    factor = 2 ** (length - 1)

    if string[0] == 'B' or string[0] == 'R':
        return factor + get_index(string[1:])
    else:
        return get_index(string[1:])


with open("day5input.txt") as f:
    my_string = f.read()

seats = my_string.split("\n")

reserved = []

for seat in seats:
    row = seat[0:7]
    col = seat[7:10]

    row_num = get_index(row)
    col_num = get_index(col)

    reserved.append((row_num * 8) + col_num)

reserved.sort()
n_reserved = len(reserved)

for i in range(n_reserved):
    if i+1 < n_reserved and reserved[i+1] - reserved[i] != 1:
        print(reserved[i + 1], reserved[i])
