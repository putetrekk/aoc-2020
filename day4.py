with open("day4input.txt") as f:
    my_string = f.read()

my_strings = my_string.split("\n\n")

valid = 0

for my_str in my_strings:
    if 'byr' in my_str and 'iyr' in my_str and 'eyr' in my_str and 'hgt' in my_str and 'hcl' in my_str and 'ecl' in my_str and 'pid' in my_str:
        valid += 1

print(valid)
