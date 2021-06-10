# -*- coding: utf-8 -*-
"""
βιτ Created on Sun Mar 14 16:41:26 2021

@author: user
"""

import binascii
import random
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        #cipher = AES.new(self.key, AES.MODE_CBC, iv)
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
    
    


avg=0
for j in range(0,35):
    print('Pair no: ', j+1)
    str1=''
    str2=''
    for i in range(0,48):
        str1+=str((random.randint(0,1)))
    str2=str1.replace('0','1',1)
    cipher=AESCipher('This is the secret key')
    #print('First str encrypted: ')
    k1=cipher.encrypt(str1)
    k2=(cipher.encrypt(str2))
    counts=sum ( k1[i] != k2[i] for i in range(len(k1)))
    avg+=counts
    print('Differences between the two cipher texts :',counts)
    print('_______________')

print('Average : ' , avg/35)