'''
    Author: David Madrigal Buendía
    This is an example or basic implementation for vigenere CTR mod
'''
import os
import random

class vigenere_CTR:
    '''
    A class used from basic vigenere cipher CTR mod

    Attributes
    ----------
    alfabetoIngles : str[]
        The english alphabet
    alfabeto : str[]
        The alphabet to will use the class that need to be 2^n size
    tam_llave_in : int
        Minimun key size
    tam_llave_max : int
        Maximun key size

    Methods
    -------
    recibirArchivo(nombreArchivo)
        Simple function to read bits from a file, using the same directory
    concatenar_bloques(texto)
        Concat an array strings, into a simple string
    GuardarDatos(nombreA, datos)
        Save data in a file, using default directory
    logical_xor(num1, num2)
        Apply xor of two numbers
    random_char()
        Get a character pseudo-aleatory from the alphabet
    generate_counts(self, n, llave)
        Generates random counts for CTR mod
    generate_iv(tam_llave)
        Get random iv from the alphabet, using random_char() function
    generate_key()
        Get random key from the alphabet, using random_char() function
    bloquesTexto(texto, llave)
        Break text into blocks by key size
    completarBloques(bloques, size)
        Complete blocks with spaces if any element don't have the size
    indice_caracter(c)
        Gets index from the alphabet by c
    cifrar_ctr(bloques, llave, contadores)
        Encipher using vigenere CTR mod
    cifrar_bloque_ctr(bloque, llave, contador)
        Encipher using vigenere CTR mod, block cipher
    decifrar_ctr(bloques, llave, contadores)
        Decipher using vigenere CTR mod
    decifrar_bloque_ctr(bloque, llave, contador)
        Decipher using vigenere CTR mod, block cipher
    '''
    alfabetoIngles = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z',' ','-','/','*','<','0']
    alfabeto = alfabetoIngles
    tam_llave_min = 2
    tam_llave_max = 7

    def __init__(self, tam_min, tam_max):
        self.tam_llave_min = tam_min
        self.tam_llave_max = tam_max

    def recibirArchivo(self, nombreArchivo):
        '''
        Simple function to read bits from a file, using the same directory

        Parameters
        ----------
        nombreArchivo : str
            File name

        Returns
        -------
        str
            Data from the found file
        '''
        rutaDirectorio = os.path.dirname(__file__)
        filepath = f'{rutaDirectorio}/{nombreArchivo}'
        f = open(filepath, 'r')
        data = ''
        for line in f:
            data += line
        f.close()
        return data

    def concatenar_bloques(self, texto):
        '''
        Concat an array strings, into a simple string

        Parameters
        ----------
        texto : str[]
            Blocks text

        Returns
        -------
        str
            Text into a str
        '''
        str1 = ''
        for i in range(len(texto)):
            for j in range(len(texto[i])):
                str1 += texto[i][j]
        return str1

    def GuardarDatos(self, nombreA, datos):
        '''
        Save data in a file, using default directory

        Parameters
        ----------
        nombreA : str
            File name
        datos : str
            Data
        '''
        rutaDirectorio = os.path.dirname(__file__)
        filepath = f'{rutaDirectorio}/{nombreA}'
        f = open(filepath, 'w')
        f.write(str(datos))
        f.close
        
    def logical_xor(self, num1, num2):
        '''
        Apply xor of two numbers

        Parameters
        ----------
        num1 : int
            First number
        num2 : int
            Second number

        Returns
        -------
        int
            Output xor by the two numbers
        '''
        return num1 ^ num2

    def random_char(self):
        '''
        Get a character pseudo-aleatory from the alphabet

        Returns
        -------
        str
            A random key generated
        '''
        return self.alfabeto[random.randint(0, len(self.alfabeto) - 1)]

    def generate_counts(self, n, llave):
        '''
        Generates random counts for CTR mod

        Parameters
        ----------
        n : int
            Number of blocks for cipher or counts required
        llave : str
            Key for cipher

        Returns
        -------
        str[]
            Counts for CTR cipher in array
        '''
        contadores = []
        for i in range(n):
            cont = ''
            for j in range(len(llave)):
                cont += self.random_char()
            contadores.append(cont)
        return contadores

    def generate_key(self):
        '''
        Get random key from the alphabet, using random_char() function

        Returns
        -------
        str
            A random key generated
        '''
        num = random.randint(self.tam_llave_min, self.tam_llave_max)
        llave = ''
        for i in range(num):
            llave += self.random_char()
        return llave

    def bloquesTexto(self, texto, llave):
        '''
        Break text into blocks by key size

        Parameters
        ----------
        texto : str
            The text to break into blocks
        llave : str
            Vigenere Key

        Returns
        -------
        str[]
            A list of strings where each element has the key size
        '''
        bloques = []
        for i in range(0, len(texto), len(llave)):
            bloques.append(texto[i:i+len(llave)])
        return bloques

    def completarBloques(self, bloques, size):
        '''
        Complete blocks with spaces if any element don't have the size

        Parameters
        ----------
        bloques : str[]
            Blocks of text
        size : int
            Size for blocks

        Returns
        -------
        str[]
            A list of strings that have same size block for each element
        '''
        a = bloques[-1]
        for i in range(size - len(a)):
            a += ' '
        bloques.pop()
        bloques.append(a)
        return bloques

    def indice_caracter(self, c):
        '''
        Gets index from the alphabet by c

        Parameters
        ----------
        c : str
            A character

        Returns
        -------
        int
            Index from the alphabet by c
        '''
        return self.alfabeto.index(c)

    def cifrar_ctr(self, bloques, llave, contadores):
        '''
        Encipher using vigenere CTR mod

        Parameters
        ----------
        bloques : str[]
            Text into blocks by key size
        llave : str
            Key for vigenere cipher
        contadores : str[]
            Counts into blocks by key size
        
        Returns
        -------
        str[]
            Blocks of ciphertext
        '''
        ciphertext = []
        #All blocks
        for i in range(0, len(bloques)):
            bloque_ciphertext = self.cifrar_bloque_ctr(bloques[i], llave, contadores[i])
            ciphertext.append(bloque_ciphertext)
            
        return ciphertext

    def cifrar_bloque_ctr(self, bloque, llave, contador):
        '''
        Encipher using vigenere mod CTR, block cipher

        Parameters
        ----------
        bloque : str
            A text
        llave : str
            Key for vigenere cipher
        contador : str
            A count

        Returns
        -------
        str
            Block of ciphertext
        '''
        bloque_ciphertext = []
        #Step: Vigenere
        for j in range(len(contador)):
            caracter_cifrado = (self.indice_caracter(contador[j]) + self.indice_caracter(llave[j])) % len(self.alfabeto)
            bloque_ciphertext.append(self.alfabeto[caracter_cifrado])
        #Step: TODO: Truncate
        #Step: Xor
        for j in range(len(bloque_ciphertext)):
            caracter_cifrado = self.logical_xor(self.indice_caracter(bloque[j]), self.indice_caracter(bloque_ciphertext[j])) % len(self.alfabeto)
            bloque_ciphertext[j] = self.alfabeto[caracter_cifrado]
            
        return bloque_ciphertext

    def decifrar_ctr(self, bloques, llave, contadores):
        '''
        Decipher using vigenere CTR mod

        Parameters
        ----------
        bloques : str[]
            Ciphertext into blocks by key size
        llave : str
            Key for vigenere cipher
        contadores : str[]
            Counts into blocks by key size

        Returns
        -------
        str[]
            Blocks of plaintext
        '''
        plaintext = []
        #All blocks
        for i in range(0, len(bloques)):
            bloque_plaintext = self.decifrar_bloque_ctr(bloques[i], llave, contadores[i])
            plaintext.append(bloque_plaintext)
            
        return plaintext

    def decifrar_bloque_ctr(self, bloque, llave, contador):
        '''
        Decipher using vigenere mod CTR, block cipher

        Parameters
        ----------
        bloque : str
            A ciphertext
        llave : str
            Key for vigenere cipher
        contador : str
            A count

        Returns
        -------
        str
            Block of plaintext
        '''
        bloque_plaintext = []
        #Step: Vigenere
        for j in range(len(contador)):
            caracter = (self.indice_caracter(contador[j]) + self.indice_caracter(llave[j])) % len(self.alfabeto)
            bloque_plaintext.append(self.alfabeto[caracter])
        #Step: TODO: Truncate
        #Step: Xor
        for j in range(len(bloque_plaintext)):
            caracter = self.logical_xor(self.indice_caracter(bloque[j]), self.indice_caracter(bloque_plaintext[j])) % len(self.alfabeto)
            bloque_plaintext[j] = self.alfabeto[caracter]
            
        return bloque_plaintext
