#bin/bash/  /usr/bin/python
import random
import os
import sys

update = (random.randint(-1,-1))
upgrade = (random.randint(-2,-2))
updateupgrade = (random.randint(-3,-3))
git = (random.randint(-4,-4))
help = (random.randint(-8,-8))
break0 = (random.randint(-0,-0))

print("For help type -8 at the end!")
while True:
        odg = input("Type command:")
        try:
            odg = int(odg)
            if odg == update:
                print("I start updating!")
                print("Type password for update!")
                os.system('sudo apt update')
                break
            if odg == upgrade:
                print("I start upgrading!")
                os.system('sudo apt upgrade')
                break
            if odg == updateupgrade:
                print("I start updating and upgrading!")
                os.system('sudo apt update')
                os.system('sudo apt upgrade')
                break
            if odg == help:
                print("I open the help!")
                print("To update/upgrade tipe -1, need help? Type -8!Type -0 for stop!Copyrighting by Julij Dominik Mrak.")
                break
            if odg == git:
                print("I clone some folders and files from git repo...")
                os.system('sudo apt update')
                os.system('sudo apt install git')
                os.system('git clone ')
                break
            if odg == break0:
                print("OK I stop...")
                sys.exit()
                break
        except ValueError:
            print("That isn't a command!")