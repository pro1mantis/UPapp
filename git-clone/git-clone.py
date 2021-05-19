#bin/bash/  /usr/bin/python
import random
import os
import sys

git = (random.randint(-1,-1))


print("Go to the git-clone folder. Open file named git-clone.py and type to the os.system git clone repo!")
while True:
        odg = input("Type command:")
        try:
            odg = int(odg)
            if odg == git:
                print("I clone some folders and files from git repo...")
                os.system('sudo apt update')
                os.system('sudo apt install git')
                os.system('git clone ')
                break
        except ValueError:
            print("That isn't a command!")