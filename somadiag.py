i = int (input("Digite o número de linhas: "))
j = int (input("Digite o número de colunas: ")) 
soma = 0
matriz= []
for linha in range(0,i):
    matriz.append([])
    for coluna in range(0,j):
        matriz[linha].append(int(input ("Digite o número de {}x{}: ".format(linha+1, coluna+1))))
a = 0 
b = 0 
for linha in matriz:
    for coluna in matriz[a]: 
        if a == b: 
            soma += coluna
        print ("\t {}".format(coluna), end = "")
        b +=1
    print() 
    a+=1
    b=0 
print ("A soma da diagona principal é {}".format(soma))