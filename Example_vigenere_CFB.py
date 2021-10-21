from vigenere_CFB import *

#Prueba de cifrado de un archivo txt
vig_CFB = vigenere_CFB(2,7)
archivo = input("Ingresa el nombre del archivo: ")
textoenplano = vig_CFB.recibirArchivo(archivo)
textoenplano = textoenplano.replace('\n', ' ')
#Generamos una llave
llave = vig_CFB.generate_key()
print("llave:", llave)
mensajeSeparado = vig_CFB.completarBloques(vig_CFB.bloquesTexto(textoenplano.lower(), llave), len(llave))
print("mensaje separado: ", mensajeSeparado)
#Generamos una iv
iv = vig_CFB.generate_iv(len(llave))
print("iv:", iv)

ciphertext_bloques = vig_CFB.cifrar_cfb(mensajeSeparado, llave, iv)
ciphertext = vig_CFB.concatenar_bloques(ciphertext_bloques)
print("ciphertext:", ciphertext)

#Guardamos los datos con extension en un archivo .vig (vigenere)
vig_CFB.GuardarDatos("CifradoCFB.vig", ciphertext)
#La llave y el iv lo guardamos en un mismo archivo separado por ;
llave_con_iv = llave + ';' + iv
vig_CFB.GuardarDatos("key.vig", llave_con_iv)

#Leemos los datos de los archivos
ciphertext = vig_CFB.recibirArchivo('CifradoCFB.vig')
llave_con_iv = vig_CFB.recibirArchivo('key.vig')
#Separamos la llave del iv
llave_con_iv = llave_con_iv.split(";")
llave = llave_con_iv[0]
iv = llave_con_iv[1]

#Deciframos texto
ciphertextSeparado = vig_CFB.completarBloques(vig_CFB.bloquesTexto(ciphertext.lower(), llave), len(llave))
print("cifrado separado: ", ciphertextSeparado)

texto_bloques = vig_CFB.decifrar_cfb(ciphertextSeparado, llave, iv)
print("texto", texto_bloques)
texto = vig_CFB.concatenar_bloques(texto_bloques)
print("texto:", texto)
