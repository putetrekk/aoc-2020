with open("day7input.txt") as f:
    my_string = f.read()

my_string = my_string.strip()
all_bags = my_string.split("\n")


def find_bag(description):
    for bag in all_bags:
        if bag.startswith(description):
            return bag
    return None


def get_bag_number(bag: str) -> int:
    if 'no other bags' in bag:
        return 1
    contents = bag.split(' contain ')
    nested_bags = contents[1].split(', ')
    nested_total = 0
    for bag in nested_bags:
        bag_parts = bag.split()
        nested_total += int(bag_parts[0]) * get_bag_number(find_bag(bag_parts[1] + ' ' + bag_parts[2]))
    return 1 + nested_total


gold_bag_capable = ['shiny gold']

bag_added = True

while bag_added:
    bag_added = False
    for bag in all_bags:
        for capable in gold_bag_capable:
            if capable in bag:
                bag_parts = bag.split(' ')
                master_bag = f"{bag_parts[0]} {bag_parts[1]}"
                if master_bag not in gold_bag_capable:
                    gold_bag_capable.append(master_bag)
                    bag_added = True


print(len(gold_bag_capable)-1)

shiny_gold = find_bag('shiny gold')

print(get_bag_number(shiny_gold) - 1)
