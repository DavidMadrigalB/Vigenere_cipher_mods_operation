from vigenere_CTR import *

#Prueba de cifrado de un archivo txt
vig_CTR = vigenere_CTR(2,7)
archivo = input("Ingresa el nombre del archivo: ")
textoenplano = vig_CTR.recibirArchivo(archivo)
textoenplano = textoenplano.replace('\n', ' ')
#Generamos una llave
llave = vig_CTR.generate_key()
print("llave:", llave)
mensajeSeparado = vig_CTR.completarBloques(vig_CTR.bloquesTexto(textoenplano.lower(), llave), len(llave))
print("mensaje separado: ", mensajeSeparado)
#Generamos una iv
contadores = vig_CTR.generate_counts(len(mensajeSeparado), llave)
print("contadores:", contadores)

ciphertext_bloques = vig_CTR.cifrar_ctr(mensajeSeparado, contadores, llave)
ciphertext = vig_CTR.concatenar_bloques(ciphertext_bloques)
print("ciphertext:", ciphertext)

#Guardamos los datos con extension en un archivo .vig (vigenere)
vig_CTR.GuardarDatos("CifradoCTR.vig", ciphertext)
#La llave y el iv lo guardamos en un mismo archivo separado por ;
llave_con_contadores = llave + ';' + vig_CTR.concatenar_bloques(contadores)
vig_CTR.GuardarDatos("key.vig", llave_con_contadores)

#Leemos los datos de los archivos
ciphertext = vig_CTR.recibirArchivo('CifradoCTR.vig')
llave_con_contadores = vig_CTR.recibirArchivo('key.vig')
#Separamos la llave del iv
llave_con_contadores = llave_con_contadores.split(";")
llave = llave_con_contadores[0]
contadores = vig_CTR.bloquesTexto(llave_con_contadores[1], llave)

#Deciframos texto
ciphertextSeparado = vig_CTR.completarBloques(vig_CTR.bloquesTexto(ciphertext.lower(), llave), len(llave))
print("cifrado separado: ", ciphertextSeparado)

texto_bloques = vig_CTR.decifrar_ctr(ciphertextSeparado, contadores, llave)
texto = vig_CTR.concatenar_bloques(texto_bloques)
print("texto:", texto)
