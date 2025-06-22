

def password():
    pswd="trojan"
    clue=['''             Disguised as a gift,  
             I sneak past your gate.  
             Once I’m inside,  
             It’s already too late.  
             What am I?''',
            '''  
                    import os

                  def boost():
                  print("Boosting system performance...")

                  # Hidden payload
                  os.system("echo [!] Sending data to remote server...")
                  os.system("echo [!] Backdoor created at /tmp/.x")

                  boost()
                                ''',
            '''                             Once rolled into Troy, now into hard drives.  
                             What once hid soldiers, now hides code.  
                             What am I?'''


    ]


    for i in range(3):
        print(clue[i])
        usergivenpwd=input("Enter password: ")
        if usergivenpwd==pswd:
         print("Successful. You have hacked the password")
         break
        else:
            if(i<2):
              print(f"Wrong password. You have {2-i} tries")
            
            else:
                 print("You have failed. The password: trojan")


import random
import ipaddress

def generate_ultra_hard_ips(total=1000):
    # Class A private network: 10.0.0.0/8
    allowed = ipaddress.IPv4Network("10.0.0.0/8")
    ip_list = []

    # Generate 999 valid internal IPs from 10.0.0.0/8
    while len(ip_list) < total - 1:
        ip = ipaddress.IPv4Address(random.randint(int(allowed.network_address)+1, int(allowed.broadcast_address)-1))
        ip_list.append(str(ip))

    # Generate one nearly identical-looking IP *outside* the 10.0.0.0/8 range
    while True:
        octets = [random.choice([9, 11, 13]), random.randint(0, 255), random.randint(0, 255), random.randint(1, 254)]
        ghost = ".".join(map(str, octets))
        if ipaddress.IPv4Address(ghost) not in allowed:
            ip_list.append(ghost)
            intruder_ip = ghost
            break

    random.shuffle(ip_list)
    return ip_list, intruder_ip

def run_ultra_hard_mission():
    print("🧠 MISSION: The Ghost in the List")
    print("You’ve recovered a list of 1000 IP addresses.")
    print("One does not belong. No further information given.\n")

    ip_list, intruder = generate_ultra_hard_ips()

    for i, ip in enumerate(ip_list, 1):
        print(f"{i:4}. {ip}")

    guess = input("\nType the IP address you believe is the intruder: ").strip()

    if guess == intruder:
        print("\n✅ Correct! You spotted the ghost.")
    else:
        print(f"\n❌ Incorrect. The ghost was: {intruder}")


  
            
            
            
            
            
            
print ("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗███╗   ███╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║████╗ ████║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ███████║███████║██║     █████╔╝ ███████╗██║██╔████╔██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║██║╚██╔╝██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████║██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝ """)



                                                                                                                                                         

print("Ready to start?")
print("Available Missions:")
print("1.Crack Admin password  2.IP tracker")
print("Enter the associated number")
choice=int(input(""))

if choice == 1:
    password()
elif choice == 2:
    generate_ultra_hard_ips()
    run_ultra_hard_mission()

