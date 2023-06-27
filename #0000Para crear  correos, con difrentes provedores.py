#Crear un programa que generere 5 correos de difrerentes provedores,
#Mesclando letras de la A a la Z y los numeros de l al 9 sin repetirse
#Una letra mayuscula al principio
#Y a la ves,  crear una funcion que extraiga tres  numeros y tres letras
#Y agregue un signo y al final  .!@#$%^&*()_+


import random
import string

def generar_palabra():
    palabra = ""
    for i in range(9):
        if i % 3 == 2:
            palabra += str(random.randint(1, 9))
        else:
            palabra += random.choice(string.ascii_lowercase)
    return palabra + "@mailbox.org"#AQUI PUEDES CAMBIAR EL PROVEDOR DE EMAIL
#AQUI PUEDES SEGUIR AGREGANDO PROVEDORES DE EMAIL
#gmail.com
#hotmail.com
#oulook.com
#yahoo.es
#protonmail.com
#aolmail.com
#zoho
#iclod
#gmx
#mail.com
#mailbox.org
#tutanota.com

for i in range(10):#AQUI PUEDES CAMBIAR LA CANTIDAD DE SUGERENCIAS 

    print(generar_palabra())
