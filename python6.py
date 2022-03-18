from os import sep


vocales=['a','e','i','o','u']
print(vocales)
print(vocales[0],vocales[1],sep="*")
for i in range(10):
    print(i,end="-")
for i in range(len(vocales)):
    print(f"{vocales[i]}",end=",")
else:
    print()
print(f"Longitud de vocales: {len(vocales)}")
for c in vocales:
    print(f"Vocal:  {c}")
for c in vocales:
    if c == 'b':
        break
else:
        print('no se ha encontrado el caracter b')