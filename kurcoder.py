#!/usr/bin/env python3
import hashlib, os, string
import base64
from codecs import encode

# colors
W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
P  = '\033[1;35m' # purple
#C  = '\033[1;36m' # cyan

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

ascii_list = ascii_letters


def derot13():
    rot = str(input(P+' Input Cipher '+R+'> '+W))
    print(R+' > '+ (encode(rot, 'rot_13')))
    main()

def hex2ascii():
    hex = str(input(P+' Input Hex '+R+'> '+W))
    print(R+' > '+ (bytes.fromhex(hex).decode('utf-8')))
    main()

def debase64():
    text = str(input(P+' Input Base64 '+R+'> '+W))
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decode = message_bytes.decode('ascii')
    print(R+'> '+ (decode))

def banner() :
    os.system('clear')
    print ('')
    print (R+'  Welcome to Kurcoder v.1.0')
    print ('')
    print (R+' '+R+'    Created by: 0xKurome')
    print (P+'     GitHub: ['+R+'0xkurome'+P+']')
    print (P+'     Insta:  ['+R+'0xkurome'+P+']')
    print ('')

def menu() :
        print ('')
        print (R+' [1]'+P+' Decode ROT13 Cipher')
        print (R+' [2]'+P+' Decode Hex to ASCII')
        print (R+' [3]'+P+' Decode Base64')

def main() :
    print ('')
    cmd = str(input(P+" Type [ "+R+"menu"+P+" ] to see available options\n Type [ "+R+"exit"+P+" ] to close the program\n \n > "+W))
#    cmd = str(input(R+' Type menu to see available options\n Type exit to close the program\n \n  > '+W))
    if cmd == 'exit' or cmd == 'q' or cmd == '-q' :
        exit()
    elif cmd == 'menu' :
        menu()
        main()
    elif cmd == 'clear' :
        banner()
        main()
    elif cmd == 'rot13' or cmd == '1' :
        derot13()
    elif cmd == 'hex' or cmd == '2' :
        hex2ascii()
    elif cmd == 'base64' or cmd == '3' :
        debase64()
    else :
        print ('')
        print (P+" Command "+cmd+" Not Found")
        main()

banner()
main()
