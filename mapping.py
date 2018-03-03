import sys
import pdb
from time import sleep

if len(sys.argv) < 4:
    print("Devem ser passados os seguintes parametros\n"
          "python3 mapping.py <arquivo_turing.txt>"
          "<mode (d ou n)> <breakpoint (passos)>")
else:
    castor = False
    mode = sys.argv[2]
    breakpoint = int(sys.argv[3])
    comandos = open(sys.argv[1]).readlines()
    
    if "busy" in  "".join(comandos): castor = True
    comandos = [i for i in comandos if i != "\n"]
    comandos = [i for i in comandos if i[0] != ";"]
    for i in range(len(comandos)):
        if ";" in comandos[i]:
            comandos[i] = " ".join(comandos[i].split(" ")[:5])

    comandos = [i.replace("\n", "") for i in comandos]

    comandos = [i.split() for i in comandos]

    estados = {}

    for com in comandos:
        estados[com[0]] = {}
    
    for com in comandos:
        estados[com[0]]['mov'] = {}
        
    for com in comandos:
        estados[com[0]]['mov'][com[1]] = {}
        
    for com in comandos:
        estados[com[0]]['mov'][com[1]][com[2]] = {com[3]: com[4]}
        
    
    entrada = input("entrada: ")
    print()
    
    if entrada == "":
        entrada = "_"
    else:
        entrada = entrada.strip()
    fita = list(entrada)

    head = 0
    passos = 0
    
    def set_ler(estados, estado, fita, head):
        valor = fita[head]
        if valor in estados[estado]['mov']:
            return valor
        else:
            return "*"
            
    def get_escrever(estados, estado, ler):
        return [*estados[estado]['mov'][ler]][0]
            
    def get_direcao(estados, estado, ler, escrever):
        return [*estados[estado]['mov'][ler][escrever]][0]
    
    def write_fita(fita, head, simbolo):
        if simbolo != "*":
            fita[head] = simbolo
            
    def set_fita(fita, head):
        if head >= len(fita):
            fita.append("_")
        elif head < 0:
            fita.insert(0, "_")
            return 1
        return 0
            
    def set_head(direcao, fita, head):
        if direcao == "r":
            return 1
        elif direcao == "l":
            return -1
        
        return 0
                
    def get_estado(estado, estados, ler, escrever, direcao):
        return estados[estado]['mov'][ler][escrever][direcao]
    
    estado = comandos[0][0]
    while True:
        if mode == "d" and passos == breakpoint:
            pdb.set_trace()    
        
        
        print("Atual: %s\nFita: '%s'\nHead: %d\nPassos: %s" % (estado, "".join(fita).replace("_", " "), head, passos))
        print()

        if estado in ["halt", "halt-accept", "halt-reject"]:
            break
        
        ler = set_ler(estados, estado, fita, head)
        escrever = get_escrever(estados, estado, ler)
        write_fita(fita, head, escrever)
        direcao = get_direcao(estados, estado, ler, escrever)
        head += set_head(direcao, fita, head)
        head += set_fita(fita, head)
        
        estado = get_estado(estado, estados, ler, escrever, direcao)
        
        passos += 1
