from turing_machine import Turing_Machine

maq = Turing_Machine("0", "a", "r")

maq.add_word("101 101")
texto = open("texto.txt")
transitions = [i.split()[:5] for i in texto]

for i in transitions:
    maq.add_status(i[0], i[1], i[2], i[3], i[4])

maq.analyze()
print("".join(maq.tape))