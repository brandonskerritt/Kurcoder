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
    rot = str(input(P+' Input Cipher '+C+'> '+W))
    print(C+' > '+ (encode(rot, 'rot_13')))
    main()


# Converts Hex to ASCII
def hex2ascii():
    ascii = str(input(P+' Input Hexadecimal '+C+'> '+W))
    print(C+' > '+ (bytes.fromhex(ascii).decode('utf-8')))
    main()

# Converts ASCII to Hex
def ascii2hex():
    hex = str(input(P+' Input ASCII '+C+'> '+W))
    hex_binary = hex.encode(encoding='utf_8')
    hex_text = hex_binary.hex()
    print(C+' > '+ (hex_text))
    main()

# Encodes Base64
def enbase64():
    encode_text = str(input(P+' Input Base64 to encode '+C+'> '+W))
    message_bytes = encode_text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encode_message = base64_bytes.decode('ascii')
    print(C+'> '+ (encode_message))
    main()

# Decodes Base64
def debase64():
    decode_text = str(input(P+' Input Base64 to decode '+C+'> '+W))
    base64_bytes = decode_text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decode = message_bytes.decode('ascii')
    print(C+'> '+ (decode))
    main()

# Encodes ASCII85
def enbase85():
    encode_text = str(input(P+'Input ASCII to encode '+C+'> '+W))
    message_bytes = encode_text.encode('ascii')
    base85_bytes = base64.a85encode(message_bytes)
    encode_message = base85_bytes.decode('ascii')
    print(C+'> '+ (encode_message))
    main()

# Decodes ASCII85
def debase85():
    decode_text = str(input(P+' Input ASCII85 to decode '+C+'> '+W))
    base85_bytes = decode_text.encode('ascii')
    message_bytes = base64.a85decode(base85_bytes)
    decode = message_bytes.decode('ascii')
    print(C+'> '+ (decode))
    main()

# CIDR Calculator
def cidr():
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

# def subnet_results():
    

def banner() :
    os.system('clear')
    print ('')
    print (C+'  Welcome to Kurcoder v.0.0.1')
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
        print (C+' [6]'+P+' Encode ASCII85')
        print (C+' [7]'+P+' Decode ASCII85')
        print ('  -  ')
        print (C+' [8]'+P+' IP Subnet Calculator')

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
            print(C+'\n Incorrect Cipher, Please try again ')
            derot13()
    elif cmd == 'ascii' or cmd == '2' :
            hex2ascii()
            print(C+'\n Incorrect Hexadecimal, Please try again ')
            hex2ascii()
    elif cmd == 'hex' or cmd == '3' :
            ascii2hex()
            print(C+'\n Incorrect format, Please try again ')
            ascii2hex()
    elif cmd == '4' :
            enbase64()
            print(C+'\n Incorrect format, Please try again ')
            enbase64()
    elif cmd == '5' :
            debase64()
            print(C+'\n Incorrect Base64, Please try again ')
            debase64()
    elif cmd == '6' :
            enbase85()
            print(C+'\n Incorrect format, Please try again ')
    elif cmd == '7' :
            debase85()
            print(C+'\n Incorrect ASCII85, Please try again ')
    elif cmd == 'cidr' or cmd == '8' :
            cidr()
            print(C+'\n Incorrect Cipher, Please try again ')
            cidr()
    else :
        print ('')
        print (P+" Command [ "+C+"" +cmd+ ""+P+" ] Not Found")
        main()

banner()
main()
