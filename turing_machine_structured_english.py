import sys
import os
from time import sleep

def get_commands(archive):
    """
    It reads archive with the commands for tests

    :param archive: .txt archive with commands

    :return: The commands to the tests
    """
    commands = open(archive).readlines()

    commands = [i for i in commands if i != "\n"]
    commands = [i for i in commands if i[0] != ";"]
    for i in range(len(commands)):
        if ";" in commands[i]:
            commands[i] = " ".join(commands[i].split(" ")[:5])

        commands = [i.replace("\n", "") for i in commands]

        commands = [i.split() for i in commands]
    
    return commands
    
def get_statuses(commands):
    """
    It returns the statuses after to know the commands

    :param commands: Commands to turing machine

    :return: The statuses of turing machine based on the comands
    """

    statuses = {}

    for com in commands:
        statuses[com[0]] = {}
    
    for com in commands:
        statuses[com[0]]['mov'] = {}
        
    for com in commands:
        statuses[com[0]]['mov'][com[1]] = {}
        
    for com in commands:
        statuses[com[0]]['mov'][com[1]][com[2]] = {com[3]: com[4]}
        
    return statuses
    
def set_read(statuses, status, tape, head):
    """
    It sets and returns the values on the tape

    :param statuses: Statues of turing machine
    :param status: Each of status of turing machine
    :param tape: Values on the tape's turing machine
    :param head: Head's turing machine value

    :return: The tape's values
    """

        value = tape[head]
        if value in statuses[status]['mov']:
            return value
        else:
            return "*"
            
def get_write(statuses, status, read):
    return [*statuses[status]['mov'][read]][0]
        
def get_direcao(estados, estado, ler, escrever):
    return [*estados[estado]['mov'][ler][escrever]][0]

def write_tape(tape, head, symbol):
    if symbol != "*":
        tape[head] = symbol
        
def set_tape(tape, head):
    if head >= len(tape):
        tape.append("_")
    elif head < 0:
        tape.insert(0, "_")
        return 1
    return 0
        
def set_head(direcao, tape, head):
    if direcao == "r":
        return 1
    elif direcao == "l":
        return -1
    
    return 0
            
def get_status(status, statuses, read, write, direcao):
    return statuses[status]['mov'][read][write][direcao]

def console_log(status, tape, head, steps):
    tamanho = len(tape) + 6
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
    
    status = ["-Current state-", status, "---------------"]
    steps = ["-Steps-", str(steps), "-------"]
    
    print(status[0].ljust(0), steps[0].rjust(20))
    print(status[1].center(14), steps[1].rjust(19))
    print(status[2].ljust(0), steps[2].rjust(20))
 
def clear_screen():        
    #if estado not in ["halt", "halt-accept", "halt-reject"]:
    os.system('cls' if os.name == 'nt' else 'clear')

def turing_machine(inpt, conf_file, mode, speed):
    commands = get_commands(conf_file)

    statuses = get_statuses(commands)
    
    inpt = inpt.strip()
    if inpt == "":
        inpt = "_"
    else:
        inpt = inpt.replace(" ", "_")
    
    tape = list(inpt)
    head = 0
    passos = 0
    estado = comandos[0][0]

    while True:
        console_log(status, tape, head, steps)
        if mode == "n":
            sleep(speed)
        else:
            input()

        if status in ["halt", "halt-accept", "halt-reject"]:
            break
        else:
            clear_screen()
        
        read = set_read(statuses, status, tape, head)
        write = get_write(estados, estado, ler)
        write_tape(tape, head, write)
        direcao = get_direcao(estados, estado, ler, escrever)
        head += set_head(direcao, fita, head)
        head += set_tape(tape, head)
        
        status = get_status(status, statuses, read, write, direcao)
        
        steps += 1
        
    return ["".join(tape).strip("_").replace("_", " "), status, steps]
        
if __name__ == "__main__":
    def get_parameter(param):
        parameter = {}
        parameter["file"] = param[1]
        if len(param) == 2:
            parameter["speed"] = 0.05
            parameter["mode"] = "n"
        elif len(param) == 4:
            parameter["speed"] = float(param[2])
            parameter["mode"] = param[3]
        elif len(param) == 3 and param[2].isdigit():
            parameter["speed"] = float(param[2])
            parameter["mode"] = "n"
        else:
            parameter["speed"] = 0.05
            parameter["mode"] = param[2]
        return parameter

    parameter = get_parameter(sys.argv)
    inpt = input("Entrada > ")
    file_config = parameter["file"]
    mode = parameter["mode"]
    speed = parameter["speed"]
    
    turing_machine(inpt, file_config, mode, speed)
    
