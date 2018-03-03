import sys
import pdb
from time import sleep

if len(sys.argv) < 6:
    print("Devem ser passados os seguintes parametros\n"
          "python3 mapping.py <arquivo_turing.txt> <entrada_maquina> <time_sleep> "
          "<mode (d ou n)> <breakpoint (passos)>")
else:
    tempo = int(sys.argv[3])
    mode = sys.argv[4]
    breakpoint = int(sys.argv[5])
    texto = open(sys.argv[1]).readlines()
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

    entrada = sys.argv[2].replace("-", " ")
    fita = list(entrada)

    #inicialmente
    head = 0
    passos = 0


    def set_head(direcao):
        if direcao == "r":
            return 1
        elif direcao == "l":
            return -1
        return 0

    def set_atual(estado, estados, fita, head):
        disponiveis = [i[1] for i in estados if i[0] == estado]

        if len(disponiveis) == 1:
            status = (estado, disponiveis[0])
        elif fita[head].isnumeric():
            valor = fita[head]
            if not valor in disponiveis:
                status = (estado, "*")
            else:
                status = (estado, fita[head])
        else:
            if fita[head] == "_":
                status = (estado, "_")
            else:
                status = (estado, "*")

        return status

    estadoinicial = (texto[0][0], fita[head])
    atual = set_atual(estadoinicial[0], estados, fita, head)

    accept = False
    while True:
        if mode == "d" and passos == breakpoint:
            pdb.set_trace()

        print("Atual: %s\nFita: %s\nPassos: %s" % (atual[0], "".join(fita).replace("_", ""), passos))
        print()

        if atual[0] in ["halt", "halt-accept", "halt-reject"]:
            break


        escrever = estados[atual][0]
        if escrever != '*':
            fita[head] = escrever

        prox_estado = estados[atual][2]
        head += set_head(estados[atual][1])

        if head >= len(fita):
            fita.append("_")
        if head < 0:
            fita.insert(0, "_")
            head = 0
        atual = set_atual(prox_estado, estados, fita, head)
        passos += 1
        sleep(tempo)

