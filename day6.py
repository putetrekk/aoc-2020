with open("day6input.txt") as f:
    my_string = f.read()

my_string = my_string.strip()
groups = my_string.split("\n\n")

yes_sum = 0

for group in groups:
    yes_questions = {}
    forms = group.split('\n')
    for form in forms:
        for q in form:
            if q in yes_questions:
                yes_questions[q] += 1
            else:
                yes_questions[q] = 1

    for key in yes_questions:
        if yes_questions[key] == len(forms):
            yes_sum += 1

    # yes_sum += len(yes_questions.keys())

print(yes_sum)
