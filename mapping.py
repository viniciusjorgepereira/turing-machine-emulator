from time import sleep
from pdb import set_trace

texto = open("texto_machine.txt").readlines()
texto = [i for i in texto if i != "\n"]
texto = [i for i in texto if i[0] != ";"]
for i in range(len(texto)):
    if ";" in texto[i]:
        texto[i] = " ".join(texto[i].split(" ")[:5])

texto = [i.replace("\n", "") for i in texto]

texto = [i.split() for i in texto]

estados = {}

for i in texto:
    estados[(i[0], i[1])] = i[2:]

fita = list("_101_")

limite = len(fita)

#inicialmente
head = 1
passos = 0
estadoinicial = (texto[0][0], fita[head])
atual = estadoinicial

def set_head(direcao):
    if direcao == "r":
        return 1
    elif direcao == "l":
        return -1
    return 0

def set_atual(estado, estados, fita, head):
    disponiveis = [i[1] for i in estados if i[0] == estado]

    if len(disponiveis) == 1:
        status = status = (estado, disponiveis[0])
    elif fita[head].isnumeric():
        if not '0' in disponiveis and not '1' in disponiveis:
            status = (estado, "*")
        else:
            status = (estado, fita[head])
    else:
        if fita[head] == "_":
            status = (estado, "_")
        else:
            status = (estado, "*")

    return status

#set_trace()
accept = False
while True:

    print(atual, fita, passos)
    print()

    if atual[0] in ["halt", "halt-accept"]:
        accept = True
        break

    escrever = estados[atual][0]
    if escrever != '*':
        fita[head] = escrever

    prox_estado = estados[atual][2]
    head += set_head(estados[atual][1])
    atual = set_atual(prox_estado, estados, fita, head)
    passos += 1


if accept:
    print("=)")
else:
    print("=(")

