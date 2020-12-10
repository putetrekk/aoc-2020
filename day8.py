with open("day8input.txt") as f:
    my_string = f.read().strip()

instructions = my_string.split("\n")


def evaluate_program(program_instructions):
    i_history = []
    i = 0
    acc = 0

    while i not in i_history:
        if i >= len(program_instructions):
            print(acc)
            break
        i_history.append(i)
        instruction, value = program_instructions[i].split()
        if instruction == 'acc':
            if value[0] == '+':
                acc += int(value[1:])
            else:
                acc -= int(value[1:])
            i += 1
        elif instruction == 'jmp':
            if value[0] == '+':
                i += int(value[1:])
            else:
                i -= int(value[1:])
        elif instruction == 'nop':
            i += 1
        else:
            print("Error, no instruction recognized")

    return acc


for index in range(len(instructions)):
    instruction, value = instructions[index].split()
    instructions_copy = instructions.copy()
    if instruction == 'acc':
        continue
    elif instruction == 'jmp':
        instructions_copy[index] = 'nop ' + value
    elif instruction == 'nop':
        instructions_copy[index] = 'jmp ' + value
    evaluate_program(instructions_copy)
