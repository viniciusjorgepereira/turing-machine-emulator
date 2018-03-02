import sys
from time import sleep
from pdb import set_trace

texto = open(sys.argv[1]).readlines()
texto = [i for i in texto if i != "\n"]
texto = [i for i in texto if i[0] != ";"]
for i in range(len(texto)):
    if ";" in texto[i]:
        texto[i] = " ".join(texto[i].split(" ")[:5])

texto = [i.replace("\n",  "") for i in texto]

texto = [i.split() for i in texto]

estados = {}

for i in texto:
    estados[(i[0], i[1])] = i[2:]

#set_trace()
    
atual = texto[0][0]

fita = list("101")
head = 0
passos = 0
old_head = head

def set_head(d):
    if d == "l":
        return -1
    elif d == "r":
        return 1
    
    return d
    
def set_fita(fita, escreve, i):
    if escreve != "*":    
        fita[i] = escreve
        

set_trace()
while True:
    if atual in ["halt", "halt-accept"]:
        break
        
    print("atual", atual)
    print("passos", passos)
    print("".join(fita))
    print()
    
    leu = fita[head]
    passos +=1
    escrever = estados[(atual, fita[head])][0]
    if escrever != "*":
        set_fita(fita, estados[(atual, fita[head])][0], head)
        
    head = set_head(estados[(atual, leu)][1])
    atual = estados[(atual, escrever)][2]
    sleep(2)
   
   

