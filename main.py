from turing_machine import Turing_Machine

maq = Turing_Machine("0", "halt", "r")

maq.add_word("10~1&|0|")
texto = open("texto.txt")
transitions = [i for i in texto if i != "\n"]
transitions = [i.split()[:5] for i in transitions if i[0] != ";"]

for i in transitions:
    maq.add_status(i[0], i[1], i[2], i[3], i[4])

maq.analyze()
print("".join(maq.tape))