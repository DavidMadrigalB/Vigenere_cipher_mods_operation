from vigenere import Vigenere, vig_CBC, vig_CFB, vig_CTR

def menu(vig):
    while(bool(1)):
        file = input("Ingresa el nombre del archivo: ")
        plaintext = vig.recibirArchivo(file)
        #Remove \n (enter)
        plaintext = plaintext.replace('\n', ' ')
        
        print("Opciones:\n\r 1. Cifrar \n\r 2. Decifrar \n\r 3. Salir")
        opc = input("Desea cifrar o decifrar?")
        
        if opc == '1':
            key = vig.generate_key()
            plaintext = vig.completarBloques(vig.bloquesTexto(plaintext.lower(), key), len(key))

            if isinstance(vig, vig_CTR):
                counts = vig.generate_counts(len(plaintext), key)
                ciphertext = vig.cifrar(plaintext, key, counts)
                ciphertext = vig.concatenar_bloques(ciphertext)

                file = file.split('.')
                vig.GuardarDatos("Cifrado_" + file[0] + ".vig", ciphertext)

                key_counts = key + ';' + vig.concatenar_bloques(counts)
                vig.GuardarDatos("key_" + file[0] + ".key", key_counts)
            else:
                iv = vig.generate_iv(len(key))
                ciphertext = vig.cifrar(plaintext, key, iv)
                ciphertext = vig.concatenar_bloques(ciphertext)

                file = file.split('.')
                vig.GuardarDatos("Cifrado_" + file[0] + ".vig", ciphertext)

                key_iv = key + ';' + iv
                vig.GuardarDatos("key_" + file[0] + ".key", key_iv)
            print("Cifrado.\n")
        elif opc == '2':
            ciphertext = plaintext
            file_key = input("Ingrese nombre del archivo donde se encuentra la llave: ")
            key = vig.recibirArchivo(file_key)

            key = key.split(";")
            if isinstance(vig, vig_CTR):
                counts = key[1]
                key = key[0]

                counts = vig.bloquesTexto(counts, key)
                decifrar_guardar(vig, file, ciphertext, key, counts)
            else: 
                iv = key[1]
                key = key[0]

                decifrar_guardar(vig, file, ciphertext, key, iv)
            print("Decifrado.\n")
        elif opc == '3':
            break
        else:
            continue

def decifrar_guardar(vig, file, ciphertext, key, aux):
    ciphertext = vig.completarBloques(vig.bloquesTexto(ciphertext.lower(), key), len(key))
    plaintext = vig.decifrar(ciphertext, key, aux)
    plaintext = vig.concatenar_bloques(plaintext)
    
    file = file.replace("Cifrado_", '')
    file = file.split('.')
    vig.GuardarDatos("Recover_" + file[0] + ".txt", plaintext)


#Prueba de cifrado de un archivo txt
print("Vigenere Operation Mods:\n CBC\n CFB\n CTR\n Salir");

while(bool(1)):
    mod_op = input("Ingresa el modo de operacion:");

    if mod_op == 'CBC':
        vig = vig_CBC(3,10)
        menu(vig)
    elif mod_op == 'CFB':
        vig = vig_CFB(3,10)
        menu(vig)
    elif mod_op == 'CTR':
        vig = vig_CTR(3,10)
        menu(vig)
    elif mod_op == 'Salir':
        break
    else:
        continue
