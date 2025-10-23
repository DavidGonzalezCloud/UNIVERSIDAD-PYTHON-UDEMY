
# EJEMPLO CON BREAK
for numero in range(1,10):
    if numero % 2 == 0:
        print(f'El {numero} es un numero par')
        break # cuando encuentre el primer numero par se va a detener

# EJEMPLO CON CONTINUE
for numero in range(1,10):
    if numero % 2 == 1: # numero impar
        continue # Cuando encuentra un numero impar lo ignora y continua el ciclo for
    print(numero) # imprime numero pares
