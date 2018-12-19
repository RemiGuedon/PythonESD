# coding: utf-8
import os, time
from colorama import Fore, init
from scapy.all import *


### Fonction Main ###

def main():
	banner = """ 
		d8888b. db    db     .d8888.  .o88b.  .d8b.  d8b   db   db    db .d888b.
		88  `8D `8b  d8'     88'  YP d8P  Y8 d8' `8b 888o  88   88    88 VP  `8D
		88oodD'  `8bd8'      `8bo.   8P      88ooo88 88V8o 88   Y8    8P    odD'
		88~~~      88          `Y8b. 8b      88~~~88 88 V8o88   `8b  d8'  .88'  
		88         88        db   8D Y8b  d8 88   88 88  V888    `8bd8'  j88.   
		88         YP        `8888Y'  `Y88P' YP   YP VP   V8P      YP    888888D 
		"""
	os.system("cls")
	init(autoreset=True)
	print(Fore.GREEN + banner)
	print("\t> Author : Remi GUEDON")
	print("\t> Version : 2 (scapy)")
	print("")
	### Lance le scan de ports ###
	portScan()



def portScan():
	host = raw_input("Hote a scanner : ")
	print("Choisir la range de port a scanner : ")
	minimum = int(raw_input("Port Minimum : "))
	maximum = int(raw_input("Port Maximum : "))
	maximum = maximum+1
	conf.verb = 0
	print("")
	print("Lancement du scan de port sur " + str(host))
	print("")
	print("[+] " +Fore.YELLOW+"Debut du scan a " + time.strftime("%X"))
	print("")

	for port in range (minimum, maximum):
		try:
			SYN = 0x02
			ACK = 0x10
			SYNACK = SYN | ACK
			scanTcp = IP(dst=host)/TCP(dport=port, flags='S')
			synack_pkt = sr1(scanTcp, timeout=1)
			if synack_pkt is None:
				print("[!] Port " + str(port) + " Unreacheable")
			elif synack_pkt['TCP'].flags == SYNACK:
				print("[+] Port \t" + str(port) + Fore.GREEN + "\tOpen")
			else:
				print("[-] Port \t" + str(port) + Fore.RED + "\tClosed")

		except KeyboardInterrupt:
			print("Error KeyboardInterrupt")
			exit(1)


	print("")
	print("[+] " +Fore.YELLOW+"Fin du scan a " + time.strftime("%X"))



def isHostUp(d, s):
	a = IP()
	b = ICMP()
	a.dst = d
	a.src = s
	ping = a/b
	res = sr1(ping)
	if res.code == 0:
		return True
	else:
		return False

#print (isHostUp("10.101.200.28", "10.101.200.5"))


### Lancement du programme ###
main()