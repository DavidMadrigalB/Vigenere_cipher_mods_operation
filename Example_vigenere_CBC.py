from vigenere_CBC import *

#Prueba de cifrado de un archivo txt
vig_CBC = vigenere_CBC(2,7)
archivo = input("Ingresa el nombre del archivo: ")
textoenplano = vig_CBC.recibirArchivo(archivo)
textoenplano = textoenplano.replace('\n', ' ')
#Generamos una llave
llave = vig_CBC.generate_key()
print("llave:", llave)
mensajeSeparado = vig_CBC.completarBloques(vig_CBC.bloquesTexto(textoenplano.lower(), llave), len(llave))
print("mensaje separado: ", mensajeSeparado)
#Generamos una iv
iv = vig_CBC.generate_iv(len(llave))
print("iv:", iv)

ciphertext_bloques = vig_CBC.cifrar_cbc(mensajeSeparado, llave, iv)
ciphertext = vig_CBC.concatenar_bloques(ciphertext_bloques)
print("ciphertext:", ciphertext)

#Guardamos los datos con extension en un archivo .vig (vigenere)
vig_CBC.GuardarDatos("CifradoCBC.vig", ciphertext)
#La llave y el iv lo guardamos en un mismo archivo separado por ;
llave_con_iv = llave + ';' + iv
vig_CBC.GuardarDatos("key.vig", llave_con_iv)

#Leemos los datos de los archivos
ciphertext = vig_CBC.recibirArchivo('CifradoCBC.vig')
llave_con_iv = vig_CBC.recibirArchivo('key.vig')
#Separamos la llave del iv
llave_con_iv = llave_con_iv.split(";")
llave = llave_con_iv[0]
iv = llave_con_iv[1]

#Deciframos texto
ciphertextSeparado = vig_CBC.completarBloques(vig_CBC.bloquesTexto(ciphertext.lower(), llave), len(llave))
print("cifrado separado: ", ciphertextSeparado)

texto_bloques = vig_CBC.decifrar_cbc(ciphertextSeparado, llave, iv)
texto = vig_CBC.concatenar_bloques(texto_bloques)
print("texto:", texto)
