import sys
import pdb
from time import sleep

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

def console_log(estado, fita, head, passos, speed):
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
 
    sleep(speed)
    if estado not in ["halt", "halt-accept", "halt-reject"]:
        os.system('cls' if os.name == 'nt' else 'clear')

def turing_machine(entrada, arquivo_de_configuracao, speed=0):
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
        console_log(estado, fita, head, passos, speed)

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
        
    return ["".join(fita).strip("_").replace("_", " "), estado, passos]
        
def testando():
    files = ['adicao_binaria.txt', 'alan_turing.txt', 'binario_decimal.txt', 
             'castor_ocupado.txt', 'checa_parentes.txt', 'multiplicacao_binaria.txt',
             'numeros_primos.txt', 'palindromos.txt', 'pilha.txt', 'universal_turing_machine.txt']
    
    files = ['files_for_machine/' + i for i in files]
    
    entradas = [["110110 101011", "10 10"], 
                [], 
                ["10110"],
                [""], 
                ["12(2+(3^(4-1)))"], 
                ["1101 11010"], 
                ["101"], 
                ["1001001"], 
                ["10~1&|0|"], 
                ["[ L+,0R.,1R.!1L+,1L+,0L.:,0L.,1L.:]1011"]]
    
    #adicao
    assert turing_machine(entradas[0][0], files[0]) == ["1100001", "halt", 135]
    assert turing_machine(entradas[0][1], files[0]) == ["100", "halt", 30]
    
    #assert turing_machine(entradas[1][], files[1]) - nao para
    
    #binario decimal
    assert turing_machine(entradas[2][0], files[2]) == ["22", "halt", 340]
    
    #castor ocupado
    assert turing_machine(entradas[3][0], files[3]) == ["1 111111111111", "halt", 108]
    
    #checa parenteses
    assert turing_machine(entradas[4][0], files[4]) == [":)", "halt-accept", 217]
    
    #multiplicacao binaria
    assert turing_machine(entradas[5][0], files[5]) == ["101010010", "halt", 980]
    
    #numeros_primos
    assert turing_machine(entradas[6][0], files[6]) == ["101 is prime!", "halt", 1574]
    
    #palindromos
    assert turing_machine(entradas[7][0], files[7]) == [":)", "halt-accept", 38]
    
    #pilha
    assert turing_machine(entradas[8][0], files[8]) == ["1", "halt", 141]
    
    #universal_turing_machine
    assert turing_machine(entradas[9][0], files[9]) == ["[ L+,0R.,1R.:1L+,1L+,0L.:,0L.,1L.!] 1100", "halt", 1974]
        
if __name__ == "__main__":
    testando()
        
        
