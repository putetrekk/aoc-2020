with open('day2input.txt') as f:
    my_strings = f.readlines()

valid_count = 0

for my_string in my_strings:
    split_string = my_string.split(' ')

    min = int(split_string[0].split('-')[0])
    max = int(split_string[0].split('-')[1])

    character = split_string[1][0]
    password = split_string[2][0:-1]

    # if (password.count(character) in range(min, max + 1)):
    #     valid_count += 1

    matches = 0

    for i in range(len(password)):
        if (i+1 == min or i+1 == max) and password[i] == character:
            matches += 1

    if matches == 1:
        valid_count += 1

print(valid_count)
