with open("day9input.txt") as f:
    my_string = f.read().strip()

numbers = [int(num) for num in my_string.split("\n")]
preamble_len = 25


def find_contiguous_at(index: int, target_sum: int):
    for j in range(index, len(numbers)):
        cs = numbers[index:j]
        if len(cs) > 1 and sum(cs) == target_sum:
            return min(cs) + max(cs)
        elif sum(cs) > target_sum:
            return None


def has_addends(index):
    for j in range(index - preamble_len, index):
        for k in range(j + 1, index):
            if numbers[j] + numbers[k] == numbers[index]:
                return True
    return False


magic_number = None
print("FINDING NUMBER WITHOUT ADDENDS IN PREVIOUS 25")
for i in range(preamble_len, len(numbers)):
    if not has_addends(i):
        print(f"i: {i}")

        magic_number = numbers[i]

print(f"magic_number: {magic_number}")

print("FINDING RANGE OF NUMBERS SUMMING TO MAGIC NUMBER")
for i in range(len(numbers)):
    if find_contiguous_at(i, magic_number) is not None:
        print(find_contiguous_at(i, magic_number))

