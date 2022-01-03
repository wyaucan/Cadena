
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

f = input("Igrese una frase: ")
r = input("Seleccion letra a reemplazar en la frase: ")
c = input("Se cambiara por está letra en la frase: ")
palabra_reemplaza = ""

for i in f:
     if i == r:
         i = c.upper()
     palabra_reemplaza = palabra_reemplaza + i

print(palabra_reemplaza)
