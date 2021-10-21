'''
    Author: David Madrigal Buendía
    This is an example or basic implementation for vigenere CFB mod
'''
import os
import random

class vigenere_CFB:
    '''
    A class used from basic vigenere cipher CFB mod

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
    cifrar_cfb(bloques, llave, iv)
        Encipher using vigenere CFB mod
    cifrar_bloque_cfb(bloque, llave, iv)
        Encipher using vigenere CFB mod, block cipher
    decifrar_cfb(bloques, llave, iv)
        Decipher using vigenere CFB mod
    decifrar_bloque_cfb(bloque, llave, iv)
        Decipher using vigenere CFB mod, block cipher
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

    def generate_iv(self, tam_llave):
        '''
        Get random iv from the alphabet, using random_char() function

        Parameters
        ----------
        tam_llave : int
            The key size

        Returns
        -------
        str
            A random iv generated
        '''
        iv = ''
        for i in range(tam_llave):
            iv += self.random_char()
        return iv

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

    def cifrar_cfb(self, bloques, llave, iv):
        '''
        Encipher using vigenere mod CFB

        Parameters
        ----------
        bloques : str[]
            Text into blocks by key size
        llave : str
            Key for vigenere cipher
        iv : str
            The iv for vigenere cipher mod CFB

        Returns
        -------
        str[]
            Blocks of ciphertext
        '''
        ciphertext = []

        #First block
        bloque_ciphertext = self.cifrar_bloque_cfb(bloques[0], llave, iv)
        ciphertext.append(bloque_ciphertext)

        #Follow blocks
        for i in range(1, len(bloques)):
            bloque_ciphertext = self.cifrar_bloque_cfb(bloques[i], llave, ciphertext[i-1])
            ciphertext.append(bloque_ciphertext)
            
        return ciphertext

    def cifrar_bloque_cfb(self, bloque, llave, iv):
        '''
        Encipher using vigenere mod CFB, block cipher
        The texto, llave and iv, needs to have the same size

        Parameters
        ----------
        bloque : str
            A text from block texts
        llave : str
            Key for vigenere cipher
        iv : str
            The iv for vigenere cipher mod CFB, later is previus ciphertext

        Returns
        -------
        str
            Block of ciphertext
        '''
        bloque_ciphertext = []
        #Step: Vigenere
        for j in range(len(bloque)):
            caracter_cifrado = (self.indice_caracter(iv[j]) + self.indice_caracter(llave[j])) % len(self.alfabeto)
            bloque_ciphertext.append(self.alfabeto[caracter_cifrado])
        #Step: Xor
        for j in range(len(bloque_ciphertext)):
            caracter_cifrado = self.logical_xor(self.indice_caracter(bloque_ciphertext[j]), self.indice_caracter(bloque[j])) % len(self.alfabeto)
            bloque_ciphertext[j] = self.alfabeto[caracter_cifrado]
            
        return bloque_ciphertext

    def decifrar_cfb(self, bloques, llave, iv):
        '''
        Decipher using vigenere mod CFB

        Parameters
        ----------
        bloques : str[]
            Ciphertext into blocks by key size
        llave : str
            Key for vigenere cipher
        iv : str
            The iv for vigenere cipher mod CFB

        Returns
        -------
        str[]
            Blocks of plaintext
        '''
        plaintext = []

        #First block
        bloque_plaintext = self.decifrar_bloque_cfb(bloques[0], llave, iv)
        plaintext.append(bloque_plaintext)

        #Follow blocks
        for i in range(1, len(bloques)):
            bloque_plaintext = self.decifrar_bloque_cfb(bloques[i], llave, bloques[i-1])
            plaintext.append(bloque_plaintext)
            
        return plaintext

    def decifrar_bloque_cfb(self, bloque, llave, iv):
        '''
        Decipher using vigenere mod CFB, block cipher
        The ciphertext, llave and iv, needs to have the same size

        Parameters
        ----------
        bloque : str
            A ciphertext from block of ciphertext
        llave : str
            Key for vigenere cipher
        iv : str
            The iv for vigenere cipher mod CFB, later is previus ciphertext

        Returns
        -------
        str
            Block of plaintext
        '''
        bloque_plaintext = []
        #Step: Vigenere
        for j in range(len(llave)):
            caracter = (self.indice_caracter(iv[j]) + self.indice_caracter(llave[j])) % len(self.alfabeto)
            bloque_plaintext.append(self.alfabeto[caracter])
        #Step: Xor
        for j in range(len(bloque_plaintext)):
            caracter = self.logical_xor(self.indice_caracter(bloque_plaintext[j]), self.indice_caracter(bloque[j])) % len(self.alfabeto)
            bloque_plaintext[j] = self.alfabeto[caracter]
            
        return bloque_plaintext
