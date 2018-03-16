import sys
import os
from time import sleep
import glob
from pickle import load

def get_commands(archive):
    """
    It reads archive with the commands for tests

    :param archive: .txt archive with commands

    :return: The commands to the tests
    """
    commands = open(archive).readlines()

    commands = [i for i in commands if i != "\n"]
    commands = [i for i in commands if i[0] != ";"]
    for com in range(len(commands)):
        if ";" in commands[com]:
            commands[com] = " ".join(commands[com].split(" ")[:5])

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
    :param status: Each of statuses of turing machine
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
    """
    It returns the turing machine's write

    :param statuses: Statuses of turing machine
    :param status: Each of statuses of turing machine
    :param read: Reading by turing machine

    :return: The curretly writing
    """

    return [*statuses[status]['mov'][read]][0]
        
def get_way(statuses, status, read, write):
    """
    It returns the correct way of turing machine

    :param statuses: Statuses of turing machine
    :param status: Each of statuses of turing machine
    :param read: Reading by turing machine
    :param write: Writing by turing machine

    :return: The ways of turing machine
    """

    return [*statuses[status]['mov'][read][write]][0]

def write_tape(tape, head, symbol):
    """


    :param tape:
    :param head:
    :param symbol:

    :return:
    """

    if symbol != "*":
        tape[head] = symbol
        
def set_tape(tape, head):
    """
    It writes on the tape

    :param tape: Turing machine's tape
    :param head: Head of turing machine

    :return: The curretly writing on the tape
    """

    if head >= len(tape):
        tape.append("_")
    elif head < 0:
        tape.insert(0, "_")
        return 1
    return 0
        
def set_head(way, tape, head):
    """


    :param way:
    :param tape:
    :param head:

    :return:
    """

    if way == "r":
        return 1
    elif way == "l":
        return -1
    
    return 0
            
def get_status(status, statuses, read, write, way):
    """

    :param status:
    :param statuses:
    :param read:
    :param write:
    :param way:

    :return:
    """

    return statuses[status]['mov'][read][write][way]

def console_log(status, tape, head, steps):
    """


    :param status:
    :param tape:
    :param head:
    :param steps:

    :return:
    """

    size = len(tape) + 6
    tracos = "-" * (size//2)
    cab = tracos + "Tape" + tracos
    m = " " * (len(cab))
    b = "-" * len(cab)
    fit = "".join(tape).replace("_", " ")
    h = [" " for i in tape]
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
    """


    :param inpt:
    :param conf_file:
    :param mode:
    :param speed:

    :return:
    """

    commands = get_commands(conf_file)

    statuses = get_statuses(commands)
    
    inpt = inpt.strip()
    if inpt == "":
        inpt = "_"
    else:
        inpt = inpt.replace(" ", "_")
    
    tape = list(inpt)
    head = 0
    steps = 0
    status = commands[0][0]

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
        write = get_write(statuses, status, read)
        write_tape(tape, head, write)
        way = get_way(statuses, status, read, write)
        head += set_head(way, tape, head)
        head += set_tape(tape, head)
        
        status = get_status(status, statuses, read, write, way)
        
        steps += 1
        
    return ["".join(tape).strip("_").replace("_", " "), status, steps]
        
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
        for i in exced:
            menu_string += "%d. %s" % (i, files[str(i)].split("/")[1].replace("_", " ").title()+"\n")

        return menu_string

    def get_parameter(param):
        parameter = {}
        if len(param) == 1:
            parameter["speed"] = 0.05
            parameter["mode"] = "n"
        elif len(param) == 2:
            if param[2].isdigit():
                parameter["speed"] = float(param[2])
                parameter["mode"] = "n"
            else:
                parameter["speed"] = 0.05
                parameter["mode"] = "s"
        else:
            parameter["speed"] = param[2]
            parameter["mode"] = param[3]
        return parameter


    default_files = open("default_files_config.pkl", "rb")
    default_files = load(default_files)
    others_files = list({*glob.glob("files_config/*.txt")}.difference({*default_files.values()}))
    for i in range(len(others_files)):
        default_files[str(11+i)] = others_files[i]

    print(menu(default_files))
    file_config = default_files[int(input("> "))]

    parameter = get_parameter(sys.argv)
    input = input("Entrada > ")

    mode = parameter["mode"]
    speed = parameter["speed"]
    import pdb; pdb.set_trace()
    turing_machine(input, file_config, mode, speed)
    
