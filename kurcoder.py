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

# Hexdump
def hexdumper():
    filename = str(input(P+' Input filename to hexdump: '+C+'> '+W))
    try:
        filedump = open(filename, 'rb')
    except:
        print(C+' File not found. Please verify the filename, and the file is in your current directory'+W) #+W, sys.exc_info()[0])
        hexdumper()
    counter = 0
    offset = 0
    byte = filedump.read(8)
    ascii_list = []
    i = 1
    if len(byte) == 0:              # checks if the file is empty
        print(C+' File is empty, Please try again'+W)
        hexdumper()
    print(C+'%08x ' % (offset), end = ' ')
    offset += int(len(byte))
    while len(byte)>0:
        for b in byte:
            print('%02x' %b, end = ' ')
            c = chr(b)
            ascii_list.append(c)
        print(' ', end = '')
        if len(ascii_list)>=16:      # prints ascii values of hex
            print('|', end = '')
            for c in ascii_list:
                if ord(c) < 33:
                    print ('.',end ='')
                elif ord(c) > 126:
                    print ('.',end='')
                else:
                    print(c,end ='')
            print('|',end='')
            ascii_list[:] = []
        if (offset % 16 == 0):      # pints previous bits
                print('')
                print('%08x ' % (offset), end = ' ')
        prev = byte                 # refreshes all values 
        byte = filedump.read(8)
        offset += int(len(byte))
    if ascii_list:                   # verifies if a list has a value inside
        if (offset % 16 < 8):       # formats the last line if less than 8 bytes are read
            while i <= 25:
                print(' ',end='')
                i= i+1
        i = 1
        while i <= 24 - (len(prev)*3): # formatting the last line
            print (' ', end ='')
            i= i+1
        print('|', end ='')
        for c in ascii_list:
            if ord(c) < 33:
                print ('.',end ='')
            elif ord(c) > 126:
                print ('.',end='')
            else:
                print(c,end ='')
        print('|')
        print('%08x ' % (offset))
        main()
    else:
        print('')

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

# IP to Binary
def ip2bin():
    ip2bin_text = str(input(P+' Input IP '+C+'> '+W))
    ip2bin_result = '.'.join(map(str,['{0:08b}'.format(int(x)) for x in ip2bin_text.split('.')]))
    print(C+'> '+ (ip2bin_result))
    main()

def banner():
    try:
        os.system('cls')
        raise ValueError('Error')
    except Exception:
        os.system('clear')
    print ('')
    print (C+'  Welcome to Kurcoder v.0.0.1')
    print ('')
    print (C+' '+C+'    Created by: 0xKurome')
    print (P+'     GitHub: ['+C+'0xkurome'+P+']')
    print (P+'     Insta:  ['+C+'0xkurome'+P+']')
    print ('')

def menu():
        print ('')
        print (C+' [1]'+P+' Decode ROT13 Cipher')
        print (C+' [2]'+P+' Convert Hexadecimal to ASCII')
        print (C+' [3]'+P+' Convert ASCII to Hexadecimal')
        print (C+' [4]'+P+' Hexdump a file (file must be in current dir)')
        print (C+' [5]'+P+' Encode Base64')
        print (C+' [6]'+P+' Decode Base64')
        print (C+' [7]'+P+' Encode ASCII85')
        print (C+' [8]'+P+' Decode ASCII85')
        print ('  -  ')
        print (C+' [9]'+P+' IP Subnet Calculator')
        print (C+' [10]'+P+' Convert IP to Binary')

def main():
    print ('')
    cmd = str(input(C+" Type [ "+P+"menu"+C+" ] to see available options\n Type [ "+P+"exit"+C+" ] to close the program\n \n > "+W))
    if cmd == 'exit' or cmd == 'quit' or cmd == 'q' or cmd == '-q' :
        exit()
    elif cmd == 'menu' or cmd == 'm' :
        menu()
        main()
    elif cmd == 'clear' or cmd == 'c' :
        banner()
        main()
    elif cmd == '1' :
        try:
            derot13()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            derot13()
    elif cmd == '2' :
        try:
            hex2ascii()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            hex2ascii()
    elif cmd == '3' :
        try:
            ascii2hex()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            ascii2hex()
    elif cmd == '4' :
        try:
            hexdumper()
        except Exception:
            print(C+'\n Incorrect file, Please try again')
            hexdumper()
    elif cmd == '5' :
        try:
            enbase64()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            enbase64()
    elif cmd == '6' :
        try:
            debase64()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            debase64()
    elif cmd == '7' :
        try:
            enbase85()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            enbase85()
    elif cmd == '8' :
        try:
            debase85()
        except Exception:
            print(C+'\n Incorrect ASCII85, Please try again ')
            debase85()
    elif cmd == '9' :
        try:
            cidr()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            cidr()
    elif cmd == '10' :
        try:
            ip2bin()
        except Exception:
            print(C+'\n Incorrect format, Please try again ')
            ip2bin()
    else :
        print ('')
        print (P+" Command [ "+C+"" +cmd+ ""+P+" ] Not Found")
        main()

banner()
main()

