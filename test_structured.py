from turing_machine_structured import turing_machine
from time import sleep

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
    sleep(3)
    assert turing_machine(entradas[0][1], files[0]) == ["100", "halt", 30]
    sleep(3)

    #assert turing_machine(entradas[1][], files[1]) - nao para
    
    #binario decimal
    assert turing_machine(entradas[2][0], files[2]) == ["22", "halt", 340]
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
    assert turing_machine(entradas[6][0], files[6]) == ["101 is prime!", "halt", 1574]
    sleep(3)
    #palindromos
    assert turing_machine(entradas[7][0], files[7]) == [":)", "halt-accept", 38]
    sleep(3)
    #pilha
    assert turing_machine(entradas[8][0], files[8]) == ["1", "halt", 141]
    sleep(3)
    #universal_turing_machine
    assert turing_machine(entradas[9][0], files[9]) == ["[ L+,0R.,1R.:1L+,1L+,0L.:,0L.,1L.!] 1100", "halt", 1974]
        
if __name__ == "__main__":
    testando()
