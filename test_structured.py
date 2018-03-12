from turing_machine_structured import turing_machine
from time import sleep


def testando():
    files = ['adicao_binaria.txt', 'alan_turing.txt', 'binario_decimal.txt', 
             'castor_ocupado.txt', 'checa_parentes.txt', 'multiplicacao_binaria.txt',
             'numeros_primos.txt', 'palindromos.txt', 'pilha.txt', 'universal_turing_machine.txt']
    
    files = ['files_for_machine/' + i for i in files]
    
    entradas = [["110110 101011", "10 10", "1111 10100"], 
                [], 
                ["10110", "101101"],
                [""], 
                ["12(2+(3^(4-1)))", "(8(3+4)", "())(()", "2/2(4^2))"], 
                ["1101 11010", "1010 11111", "1010 0", "101 1"], 
                ["101", "10", "110"], 
                ["1001001", "10100101", "001101", "11101111110111", "001000"], 
                ["10~1&|0|"], 
                ["[ L+,0R.,1R.!1L+,1L+,0L.:,0L.,1L.:]1011", "[0L++, R., R+!1L+, R., R-:,,:]01010", "[0L++, R., R+!1L+, R., R-:,,:]01011"]]
    
    #adicao
    assert turing_machine(entradas[0][0], files[0]) == ["1100001", "halt", 135]
    sleep(3)
    assert turing_machine(entradas[0][1], files[0]) == ["100", "halt", 30]
    sleep(3)
    # 15 + 20 = 35 e nao 34.
    assert turing_machine(entradas[0][2], files[0]) != ["100010", "halt", 96]
    sleep(3)
    

    #assert turing_machine(entradas[1][], files[1]) - nao para
    
    #binario decimal
    assert turing_machine(entradas[2][0], files[2]) == ["22", "halt", 340]
    sleep(3)
    assert turing_machine(entradas[2][1], files[2]) == ["45", "halt", 760]
    sleep(3)
    
    #castor ocupado
    assert turing_machine(entradas[3][0], files[3]) == ["1 111111111111", "halt", 108]
    sleep(3)

    
    #checa parenteses
    assert turing_machine(entradas[4][0], files[4]) == [":)", "halt-accept", 217]
    sleep(3)
    assert turing_machine(entradas[4][1], files[4]) == [":(", "halt-reject", 73]
    sleep(3)
    assert turing_machine(entradas[4][2], files[4]) == [":(", "halt-reject", 38]
    sleep(3)
    assert turing_machine(entradas[4][3], files[4]) == [":(", "halt-reject", 71]
    sleep(3)

        
    #multiplicacao binaria
    assert turing_machine(entradas[5][0], files[5]) == ["101010010", "halt", 980]
    sleep(3)
    assert turing_machine(entradas[5][1], files[5]) == ["100110110", "halt", 736]
    sleep(3)
    #Testando multiplicacao por 0
    assert turing_machine(entradas[5][2], files[5]) == ["0000", "halt", 294]
    sleep(3)
    #Testando multiplicacao por 1
    assert turing_machine(entradas[5][3], files[5]) == ["101", "halt", 189]
    sleep(3)

    
    #castor ocupado
    assert turing_machine(entradas[3][0], files[3]) == ["1 111111111111", "halt", 108]
    sleep(3)
    #checa parenteses
    assert turing_machine(entradas[4][0], files[4]) == [":)", "halt-accept", 217]
    sleep(3)
    #multiplicacao binaria
    assert turing_machine(entradas[5][0], files[5]) == ["101010010", "halt", 980]
    sleep(3)
    #numeros_primos
    #Testando o numero 5
    assert turing_machine(entradas[6][0], files[6]) == ["101 is prime!", "halt", 1574]
    sleep(3)
    # Testando o numero 2
    assert turing_machine(entradas[6][1], files[6]) == ["10 is prime!", "halt", 280]
    sleep(3)
    #Testando o numero 6
    assert turing_machine(entradas[6][2], files[6]) == ["110 is not prime.", "halt", 1127]
    sleep(3)
    
    #palindromos
    assert turing_machine(entradas[7][0], files[7]) == [":)", "halt-accept", 38]
    sleep(3)
    #Testando 10100101
    assert turing_machine(entradas[7][1], files[7]) == [":)", "halt-accept", 46]
    sleep(3)
    #Testando 001101 - Rejeita
    assert turing_machine(entradas[7][2], files[7]) == [":(", "halt-reject", 15]
    sleep(3)
    #Testando 11101111110111
    assert turing_machine(entradas[7][3], files[7]) == [":)", "halt-accept", 121]
    sleep(3)
    #Testando 001000 - Rejeita
    assert turing_machine(entradas[7][4], files[7]) == [":(", "halt-reject", 29]
    sleep(3)

    
    #pilha
    assert turing_machine(entradas[8][0], files[8]) == ["1", "halt", 141]
    
    
    #palindromos
    assert turing_machine(entradas[7][0], files[7]) == [":)", "halt-accept", 38]
    sleep(3)
    #pilha
    assert turing_machine(entradas[8][0], files[8]) == ["1", "halt", 141]
    sleep(3)
    #universal_turing_machine
    assert turing_machine(entradas[9][0], files[9]) == ["[ L+,0R.,1R.:1L+,1L+,0L.:,0L.,1L.!] 1100", "halt", 1974]
    sleep(3)
    # Testando bit de paridade(PAR) binaria
    # Numero: 01010 bit de paridade 0
    assert turing_machine(entradas[9][1], files[9]) == ["[0L++, R., R+:1L+, R., R-:,,!] 0", "halt", 1382]
    sleep(3)
    # Numero: 01011 bit de paridade 1
    assert turing_machine(entradas[9][2], files[9]) == ["[0L++, R., R+:1L+, R., R-:,,!] 1", "halt", 1296]
    sleep(3)
        
if __name__ == "__main__":
    testando()
