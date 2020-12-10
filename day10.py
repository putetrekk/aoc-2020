with open("day10input.txt") as f:
    my_string = f.read().strip()

adapters = [int(num) for num in my_string.split("\n")]

adapters.append(0)
adapters.append(max(adapters)+3)

adapters.sort()


single = 0
triple = 0


for i in range(1, len(adapters)):
    if adapters[i] - adapters[i-1] == 1:
        single += 1
    if adapters[i] - adapters[i-1] == 3:
        triple += 1


print(single*triple)


result_cache = {}
user_equipment = max(adapters)


def get_valid_paths(adapter):
    if adapter == user_equipment:
        return 1
    if adapter in result_cache:
        return result_cache[adapter]
    paths = 0
    if adapter + 1 in adapters:
        paths += get_valid_paths(adapter + 1)
    if adapter + 2 in adapters:
        paths += get_valid_paths(adapter + 2)
    if adapter + 3 in adapters:
        paths += get_valid_paths(adapter + 3)
    result_cache[adapter] = paths
    return paths


print(get_valid_paths(0))
