from scapy.all import *
import os

os.system("cls")

def http_header(packet):
        http_packet=str(packet)
        if http_packet.find('POST'):
        	print(POST_print(packet))
        #print(packet)

def POST_print(packet1):
    print("***************************************POST PACKET****************************************************\n")
    print("\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n")))
    print("*****************************************************************************************************\n")

#sniff(prn=http_header, filter="port 80")
sniff(prn=POST_print, lfilter=lambda p: "POST" in str(p), filter="port 80")