#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(int("[*] Enter The Host to Scan: "))
port = input("[*] Enter the Port to Scan: ")


def portscanner(port): 
	if sock.connect_ex((host,port)):
		print ("The port is closed: ", port)
	else:
		print ("The por is opened: ", port)


portscanner(port)


