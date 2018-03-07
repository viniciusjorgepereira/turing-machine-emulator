from machine import Machine

archive = open("files_for_machine/palindromos.txt")
transitions = [i.split() for i in archive if i != "\n" and i[0] != ";"]

machine = Machine(transitions[0][0])
machine.add_word(str(input()))

for i in transitions:
    machine.add_status(i[0], i[1], i[2], i[3], i[4])

machine.analyze()
print(machine.steps, machine.tape, machine.current)