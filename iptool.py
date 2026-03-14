import subprocess
import time
from rich.console import *
console = Console()



def animation():
    print(".", end="", flush=True)
    time.sleep(0.5)
    print("..", end="", flush=True)
    time.sleep(0.5)
    print(".", end="", flush=True)
    time.sleep(0.5)
    print("....", end="", flush=True)
    time.sleep(0.5)
    print(".. : ", end="", flush=True)
    time.sleep(0.5)
    
def dots():
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)

while True:
    print("""------IP TOOL------""")
    print("Loading.", end="", flush=True)
    dots()
    print("\r              ")
    ip = input("- ip adress? (skip if no ip) :").strip()
    print("""- what do you want to do ? :

    1) PING
    2) TRACEROUTE
    3) IPCONFIG
    4) PUBLIC IPV4
    5) IP COUNTRY LOCATER
    6) MESSAGE ENCRYPTER
    7) MESSAGE DECRYPTER""")
    action = int(input(": "))
    
    if action == 1 and ip != "":
        with console.status("[bold green]Pinging IP...[/bold green]", spinner="line", spinner_style="bold green"):
            time.sleep(4)  
        subprocess.run(["ping", "-c", "4", ip])
    
    
    elif action == 2:
        with console.status("[bright_red]Tracing IP....[bright_red]", spinner="bounce", spinner_style="bright_red"):
            time.sleep(4)
        subprocess.run(["traceroute", ip])
        
        
    elif action == 3:
        with console.status("[bold black]Executing Command....[bold black]", spinner="dots", spinner_style="bold black"):
            time.sleep(4)
        subprocess.run(["ip", "a"])
        
        
    elif action == 4:
        with console.status("[bold magenta]Finding your public IP.....[bold magenta]", spinner="moon", spinner_style="magenta"):
            time.sleep(4)
        subprocess.run(["curl", "-4", "-s", "ifconfig.me"])
        
        
    elif action == 5:
        with console.status("[bold green]Locating IP[bold green]", spinner="earth", spinner_style="green"):
            time.sleep(4)
        subprocess.run(["curl","-s", f"ipinfo.io/{ip}"])
        
        
    elif action == 6:
        message = input("message :").lower().strip()
        decalage = int(input("gap size :"))
        print("RESULT OF ENCRYPTION :", end="")
        for lettre in message:
            if lettre.isalpha():
                decaler = (ord(lettre) - 97 + decalage) % 26 + 97
                time.sleep(0.3)
                print(chr(decaler), end="", flush=True)
            else:
                print(lettre)
            
            
    elif action == 7:
        message = input("message :").lower().strip()
    
        console.print("[bold black]BRUTE FORCING SENTENCE = ", end="")
        for essais in range(26):
            console.print(f"\ntry n'[bold black]{essais}[/bold black] : ", end="")
            for lettre in message:
                if lettre.isalpha():
                    decaler = (ord(lettre) - 97 - essais) % 26 + 97
                    time.sleep(0.05)
                    print(chr(decaler), end="", flush=True)
                else:
                    print(lettre)
        
        console.print("""

[bold black]Original Message:""", message)
        
    else:
        console.print("""[bold white on red]Not a valid choice.

RESTARTING......""")
        time.sleep(4)
        continue
        
    time.sleep(2)
    console.print("\n[bold green]Next task ? (Y/N) [/ bold green]", end="")
    choice = input(":").strip().lower()

    if choice == "y":
        console.print("[bold green]ok. Restarting...")
        time.sleep(2)
        continue
    else:
        console.print("[bold red]ok. Stopping.")
        time.sleep(1)
        break