# coding: utf-8
import socket, os, time
from colorama import Fore, init

### Fonction Port Scan ###

def portScan():
	host = raw_input("Hote a scanner : ")
	print("Choisir la range de port a scanner : ")
	minimum = int(raw_input("Port Minimum : "))
	maximum = int(raw_input("Port Maximum : "))
	maximum = maximum+1
	print("")
	print("Lancement du scan de port sur " + str(host))
	print("")
	print("[+] " +Fore.YELLOW+"Debut du scan a " + time.strftime("%X"))
	print("")
	
	for port in range (minimum, maximum):
		try:
			s = socket.socket()
			s.settimeout(1)
			retour = s.connect_ex((host, port))
			if retour == 0:
				print("[+] Port \t" + str(port) + Fore.GREEN + "\tOpen")
			else:
				print("[-] Port \t" + str(port) + Fore.RED + "\tClosed")
			s.close()
		except KeyboardInterrupt:
			print("Error KeyboardInterrupt")
			exit(1)
	print("")
	print("[+] " +Fore.YELLOW+"Fin du scan a " + time.strftime("%X"))


### Fonction Main ###

def main():
	banner = """
	d8888b. db    db     .d8888.  .o88b.  .d8b.  d8b   db
	88  `8D `8b  d8'     88'  YP d8P  Y8 d8' `8b 888o  88
	88oodD'  `8bd8'      `8bo.   8P      88ooo88 88V8o 88
	88~~~      88          `Y8b. 8b      88~~~88 88 V8o88
	88         88        db   8D Y8b  d8 88   88 88  V888
	88         YP        `8888Y'  `Y88P' YP   YP VP   V8P
	"""
	os.system("cls")
	init(autoreset=True)
	print(Fore.GREEN + banner)
	print("\t> Author : Remi GUEDON")
	print("")
	### Lance le scan de ports ###
	portScan()

### Lancement du programme ###
main()