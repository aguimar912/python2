#Escribe los números pares del 2 hasta un número que se pida por teclado previamente.
num = input("Introduce un número: ")
for i in num:
    if i % 2:
        print(i,end="-")
     