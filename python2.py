# Escribe un programa que pregunte el nombre y después de que
#  el usuario lo introduzca muestre por pantalla el nombre en mayúsculas y 
#  el número de caracteres que tiene. Después deberá escribir el nombre tantas
#   veces como letras contiene el nombre en líneas distintas.
name = input("¿Como te llamas?")

n = len(name)
print(name.upper() + " tiene " + str(len(name)) + " letras")

txt = "{} tiene {} letras"
print(txt.format(name.upper(),n))
print(f'{name.upper()} tiene {n} letras')

print(name.upper(), "tiene", str(len(name)), "letras", sep=" ")

for i in range(n):
    print(name)