#!/usr/bin/env python3
import hashlib, os, string
import base64
from codecs import encode

# colors
W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan


# Decodes ROT13
def derot13():
    rot = str(input(P+' Input Cipher '+R+'> '+W))
    print(R+' > '+ (encode(rot, 'rot_13')))
    main()

# Converts Hex to ASCII
def hex2ascii():
    ascii = str(input(P+' Input Hexadecimal '+R+'> '+W))
    print(R+' > '+ (bytes.fromhex(ascii).decode('utf-8')))
    main()

# Converts ASCII to Hex
def ascii2hex():
    hex = str(input(P+' Input ASCII '+R+'> '+W))
    hex_binary = hex.encode(encoding='utf_8')
    hex_text = hex_binary.hex()
    print(R+' > '+ (hex_text))
    main()

# Decodes Base64
def debase64():
    decode_text = str(input(P+' Input Base64 to decode '+R+'> '+W))
    base64_bytes = decode_text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decode = message_bytes.decode('ascii')
    print(R+'> '+ (decode))
    main()

# Encodes Base64
def enbase64():
    encode_text = str(input(P+' Input Base64 to encode '+R+'> '+W))
    message_bytes = encode_text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encode_message = base64_bytes.decode('ascii')
    print(R+'> '+ (encode_message))
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
        print (R+' [2]'+P+' Convert Hexadecimal to ASCII')
        print (R+' [3]'+P+' Convert ASCII to Hexadecimal')
        print (R+' [4]'+P+' Encode Base64')
        print (R+' [5]'+P+' Decode Base64')

def main() :
    print ('')
    cmd = str(input(P+" Type [ "+R+"menu"+P+" ] to see available options\n Type [ "+R+"exit"+P+" ] to close the program\n \n > "+W))
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
    else :
        print ('')
        print (P+" Command "+cmd+" Not Found")
        main()

banner()
main()
