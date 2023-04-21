import os
from colorama import *
import string
import random
from time import *
from banner import *

codes_list = list(string.ascii_letters + string.digits)
Fore.RESET


def loading(image1, image2, image3):
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image1)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image2)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(image3)
        sleep(0.3)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")


def Generator():
    count_generator=0
    for i in range(1, 9):
        loading(banner_generator1, banner_generator2, banner_generator3)
    Fore.RESET
    valid_url = random.randint(1, 1000)
    valid_test = -1
    while True:
        #reset codes variable
        codes=""
        essay = input("Number of tests (type end if you want to exit):\n\n")
        if essay == "end":
            Menu()
        if not essay.isdigit() or int(essay) < 1:
            print("Invalid input")
            continue
        for i in range(int(essay)):
            codes=""
            sleep(0.1)
            valid_test = random.randint(1, 1000) 
            #codes generation
            for i in range(17):
                code = random.choice(codes_list)
                codes += code
            url = "http://discord.gift/"+codes
            count_generator =+ 1
            print(Fore.RED+"ERROR:404 "+Fore.RED+"--> "+Fore.LIGHTRED_EX+url+Fore.LIGHTRED_EX)
            if valid_test == valid_url:
                print(Fore.GREEN+"FOUND "+Fore.LIGHTGREEN_EX+"--> "+Fore.LIGHTGREEN_EX+url+Fore.LIGHTGREEN_EX)
                file = os.path.join("hit.txt")
                with open(file, "a+") as file_hit:
                    file_hit.write("\n--->  "+url)
                    Fore.RESET

        
def Menu():
    print(Fore.MAGENTA+banner_main)
    choice = ""
    while choice not in ["1", "2", "3"]:
        print(Fore.WHITE+"["+Fore.CYAN+"1"+Fore.WHITE+"]"+Fore.CYAN+" Generator")
        print(Fore.WHITE+"["+Fore.CYAN+"2"+Fore.WHITE+"]"+Fore.CYAN+" hit") 
        print(Fore.WHITE+"["+Fore.CYAN+"3"+Fore.WHITE+"]"+Fore.CYAN+" Exit")
        choice = input("\n--->  ")
        if choice == "1":
            print("")
            Generator()
        elif choice == "2":
            Hit()
        elif choice == "3":
            SystemExit
        else:
            print(Fore.RED+"Error: your choice is not in the menu")
  
  
def Hit():
    file = os.path.join("hit.txt")
    with open(file, "r") as file_hit:
        hit = file_hit.read()
        print(hit)
    hit_choice = input("Return Menu : (Y) ")
    while hit_choice not in ["Y","Yes","yes","y"]:
        hit_choice = input("Return Menu ? (Y) ")
    Fore.RESET
    Menu()
  
  
def main():
    filename = os.path.join("hit.txt")
    if not os.path.exists(filename):
        with open(filename, "w") as fichier:
            fichier.write("You can see your hit here, Im Glad You Got A Hit :")
    Menu()
            

main()