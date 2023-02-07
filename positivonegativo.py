vetor = []

def positivoOuNao(vetor, value):
    if(value >= 0):
        vetor.append(1)
    else:
        vetor.append(0)
    print(vetor)

for i in range (0,3):
    value = int(input('Digite um valor: '))
    positivoOuNao(vetor, value)
