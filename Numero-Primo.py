num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:                   #código principal
        contador += 1
    else:
        pass

print("O número {} foi divisível {} vezes!".format(num, contador))          #Informa os valores

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")