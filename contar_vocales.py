Frase = input("Ingrese una frase : \n")
frasemin = Frase.lower()
i =0
for vocales in frasemin:
    if vocales== "a" or vocales== "e" or vocales== "i" or vocales== "o" or vocales== "u":
        i+=1
        True
print(f"La frase tiene {i} vocales")