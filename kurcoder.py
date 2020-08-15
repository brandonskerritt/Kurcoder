#!/usr/bin/env python3
import hashlib, os, string
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
    print(R+'> '+ (encode(rot, 'rot_13')))
    main()

def hex2ascii():
    hex = str(input(P+' Input Hex '+R+'> '+W))
    print(R+'> ' + (bytes.fromhex(hex).decode('utf-8')))
    main()

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
    else :
        print ('')
        print (P+" Command "+cmd+" Not Found")
        main()

banner()
main()
