import sys
import os
from time import sleep
from pickle import load
import glob

def get_comandos(arquivo):
    comandos = open(arquivo).readlines()
    
    comandos = [i for i in comandos if i != "\n"]
    comandos = [i for i in comandos if i[0] != ";"]
    for i in range(len(comandos)):
        if ";" in comandos[i]:
            comandos[i] = " ".join(comandos[i].split(" ")[:5])

    comandos = [i.replace("\n", "") for i in comandos]

    comandos = [i.split() for i in comandos]
    
    return comandos
    
def get_estados(comandos):
    estados = {}

    for com in comandos:
        estados[com[0]] = {}
    
    for com in comandos:
        estados[com[0]]['mov'] = {}
        
    for com in comandos:
        estados[com[0]]['mov'][com[1]] = {}
        
    for com in comandos:
        estados[com[0]]['mov'][com[1]][com[2]] = {com[3]: com[4]}
        
    return estados
    
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

def console_log(estado, fita, head, passos):
    tamanho = len(fita) + 6
    tracos = "-" * (tamanho//2)
    cab = tracos + "Tape" + tracos
    m = " " * (len(cab))
    b = "-" * len(cab)
    fit = "".join(fita).replace("_", " ")
    h = [" " for i in fita]
    h[head] = "^"
    header = "".join(h)
    tape = [cab,m,fit,header,b]
    just = len(cab)+12
    
    print((" " * 12 + tape[0]).center(just))
    print((" " * 12 + tape[1]).center(just))
    print((" " * 12 + tape[2]).center(just))
    print((" " * 12 + tape[3]).center(just))
    print((" " * 12 + tape[4]).center(just))
    print()
    
    status = ["-Current state-", estado, "---------------"]
    steps = ["-Steps-", str(passos), "-------"]
    
    print(status[0].ljust(0), steps[0].rjust(20))
    print(status[1].center(14), steps[1].rjust(19))
    print(status[2].ljust(0), steps[2].rjust(20))
 
def clear_screen():        
    os.system('cls' if os.name == 'nt' else 'clear')

def turing_machine(entrada, arquivo_de_configuracao, modo, speed):
    comandos = get_comandos(arquivo_de_configuracao)

    estados = get_estados(comandos)
    
    entrada = entrada.strip()
    if entrada == "":
        entrada = "_"
    else:
        entrada = entrada.replace(" ", "_")
    
    fita = list(entrada)
    head = 0
    passos = 0
    estado = comandos[0][0]

    while True:
        console_log(estado, fita, head, passos)
        if modo == "n":
            sleep(speed)
        else:
            input()

        if estado in ["halt", "halt-accept", "halt-reject"]:
            break
        else:
            clear_screen()
        
        ler = set_ler(estados, estado, fita, head)
        escrever = get_escrever(estados, estado, ler)
        write_fita(fita, head, escrever)
        direcao = get_direcao(estados, estado, ler, escrever)
        head += set_head(direcao, fita, head)
        head += set_fita(fita, head)
        
        estado = get_estado(estado, estados, ler, escrever, direcao)
        
        passos += 1
        
    return ["".join(fita).strip("_").replace("_", " "), estado, passos]
        
if __name__ == "__main__":
    def menu(files):
        menu_string = """
              -TURINHA-
      Turing Machine Simulator

      Welcome

      Please select a file configuration

       1. Binary Addition
       2. Binary Multiplication 
       3. Binary to decimal
       4. Palindrome Detector
       5. Parentheses checker
       6. Primality test
       7. Reverse polish boolean calculator
       8. Turing's sequence machine
       9. Universal Turing Machine
      10. 4-state busy beaver
"""

        exced = [*filter(lambda x: x > 10, map(int, [*files]))]
        exced.sort()
        for i in exced:
            name = files[i].split("/")[1].replace("_", " ").replace(".txt", "").title()
            menu_string += "      %d. %s\n" % (i, name)

        return menu_string

    def get_parameter(param):
        parameter = {}
        if len(param) == 1:
            parameter["speed"] = 0.05
            parameter["mode"] = "n"
        else:
            try:
            	value = float(param[1])
            except ValueError:
            	value = param[1]
            if type(value) == float:
                parameter["speed"] = value
                parameter["mode"] = "n"
            else:
                parameter["speed"] = 0.05
                parameter["mode"] = "s"

        return parameter


    default_files = open("default_files_config.pkl", "rb")
    default_files = load(default_files)
    others_files = list({*glob.glob("files_config/*.txt")}.difference({*default_files.values()}))
    for i in range(len(others_files)):
        default_files[11+i] = others_files[i]

    print(menu(default_files))
    option = int(input("> "))
    file_config = default_files[option]

    parameter = get_parameter(sys.argv)
    entrada = input("Entrada > ")

    mode = parameter["mode"]
    speed = parameter["speed"]

    turing_machine(entrada, file_config, mode, speed)
    
