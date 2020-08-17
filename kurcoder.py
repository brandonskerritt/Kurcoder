#!/usr/bin/env python3
import os
import sys
import hashlib
import string
import base64
import ipcalc
from codecs import encode

# colors
W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan


# Decodes ROT13
def derot13():
    try:
        rot = str(input(P+' Input Cipher '+C+'> '+W))
        print(C+' > '+ (encode(rot, 'rot_13')))
        main()
    except Exception:
        print(C+'\n Incorrect Cipher, Please try again ')
    derot13()

# Converts Hex to ASCII
def hex2ascii():
    try:
        ascii = str(input(P+' Input Hexadecimal '+C+'> '+W))
        print(C+' > '+ (bytes.fromhex(ascii).decode('utf-8')))
        main()
    except Exception:
        print(C+'\n Incorrect Hexadecimal, Please try again ')
    hex2ascii()

# Converts ASCII to Hex
def ascii2hex():
    try:
        hex = str(input(P+' Input ASCII '+C+'> '+W))
        hex_binary = hex.encode(encoding='utf_8')
        hex_text = hex_binary.hex()
        print(R+' > '+ (hex_text))
        main()
    except Exception:
        print(R+'\n Incorrect ASCII, Please try again ')
    ascii2hex()

# Encodes Base64
def enbase64():
    try:
        encode_text = str(input(P+' Input Base64 to encode '+C+'> '+W))
        message_bytes = encode_text.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        encode_message = base64_bytes.decode('ascii')
        print(C+'> '+ (encode_message))
        main()
    except Exception:
        print(C+'\n Incorrect ASCII, Please try again')
    enbase64()

# Decodes Base64
def debase64():
    try:
        decode_text = str(input(P+' Input Base64 to decode '+C+'> '+W))
        base64_bytes = decode_text.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decode = message_bytes.decode('ascii')
        print(C+'> '+ (decode))
        main()
    except Exception:
        print(C+'\n Incorrect base64, Please try again')
    debase64()

# CIDR Calculator
def cidr():
    try:
        cidr_result = str(input(P+' Input IP with subnet '+C+'> '+W))
        subnet = ipcalc.Network(cidr_result)
        for c in subnet:
            print(C+'> '+ str(c))
        cmd = str(input(C+"Do you want to save this to a file called [ "+P+"subnet.txt"+C+" ] ? [ "+P+"Yes"+C+" ] or [ "+P+"No"+C+" ]\n \n > "+W))
        if cmd == 'y' or cmd == 'yes' or cmd == 'Yes' :
            with open('subnet.txt', 'a+') as f:
                for c in subnet:
                    f.write(str(c) + '\n')
            main()
        elif cmd == 'n' or cmd == 'no' or cmd == 'No' :
            main()
        else:
            main()
    except Exception:
        print(C + "\n Incorrect IP/Subnet, Please try again ")
    cidr()

# def subnet_results():
    

def banner() :
    os.system('clear')
    print ('')
    print (C+'  Welcome to Kurcoder v.1.0')
    print ('')
    print (C+' '+C+'    Created by: 0xKurome')
    print (P+'     GitHub: ['+C+'0xkurome'+P+']')
    print (P+'     Insta:  ['+C+'0xkurome'+P+']')
    print ('')

def menu() :
        print ('')
        print (C+' [1]'+P+' Decode ROT13 Cipher')
        print (C+' [2]'+P+' Convert Hexadecimal to ASCII')
        print (C+' [3]'+P+' Convert ASCII to Hexadecimal')
        print (C+' [4]'+P+' Encode Base64')
        print (C+' [5]'+P+' Decode Base64')
        print ('  -  ')
        print (C+' [6]'+P+' IP Subnet Calculator')

def main() :
    print ('')
    cmd = str(input(C+" Type [ "+P+"menu"+C+" ] to see available options\n Type [ "+P+"exit"+C+" ] to close the program\n \n > "+W))
    if cmd == 'exit' or cmd == 'quit' or cmd == 'q' or cmd == '-q' :
        exit()
    elif cmd == 'menu' or cmd == 'm' :
        menu()
        main()
    elif cmd == 'clear' :
        banner()
        main()
    elif cmd == 'rot13' or cmd == '1' :
        derot13()
    elif cmd == 'ascii' or cmd == '2' :
        hex2ascii()
    elif cmd == 'hex' or cmd == '3' :
        ascii2hex()
    elif cmd == '4' :
        enbase64()
    elif cmd == '5' :
        debase64()
    elif cmd == 'cidr' or cmd == '6' :
        cidr()
    else :
        print ('')
        print (P+" Command [ "+C+"" +cmd+ ""+P+" ] Not Found")
        main()

banner()
main()
