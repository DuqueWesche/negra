import os
import time
from pyfiglet import Figlet
from colorama import Fore, init

yess = ["yes", "Yes", "Si","Sip","si","sip","Sii","Siii"]
noo = ["no","No","nop"]
init(autoreset=True)
def clearscreen():
    os.system('cls' if os.name =='nt' else 'clear')

def textanimation(text, delay=1.0, clear=True):
    fig=Figlet(font='Slant')
    if clear:
        clearscreen()
    for line in text.splitlines():
        print(Fore.RED + fig.renderText(line))
        time.sleep(delay)

def questions(question):
    print(Fore.GREEN + question)
    response = input(Fore.YELLOW + "Yes or No?: ".lower())
    return response

def main():
    textanimation("I", delay=0.5)
    textanimation("I like", delay=0.5)
    textanimation("I like you", delay=0.5)

    response = questions("You like me?")
    for yez in yess:
        pass
    
    for nio in noo:
        pass
    if response == "yes":
        textanimation("I", delay=0.5)
        textanimation("I love", delay=0.5)
        textanimation("I love you", delay=0.5)
        print(Fore.RED + "jsjsjs ♡")

    elif response == "no":
        textanimation("Tmr", delay=0.5)
        textanimation("Tmr fue", delay=0.5)
        textanimation("Tmr fue p", delay=0.5)
        clearscreen()
        textanimation("Tmr fue p", delay=0.5)

if __name__ == '__main__':
    main()