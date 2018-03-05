from turing_machine import Turing_Machine

maq = Turing_Machine("0", "halt-accept", "halt-reject")

maq.add_word("")
texto = open("files_for_machine/alan_turing.txt")
transitions = [i for i in texto if i != "\n"]
transitions = [i.split()[:5] for i in transitions if i[0] != ";"]

for i in transitions:
    maq.add_status(i[0], i[1], i[2], i[3], i[4])

maq.analyze()
print("".join(maq.tape).strip("_").replace("_", " "))