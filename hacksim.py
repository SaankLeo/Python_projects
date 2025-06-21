

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


    
            
            
            
            
            
            
print ("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗███╗   ███╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║████╗ ████║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ███████║███████║██║     █████╔╝ ███████╗██║██╔████╔██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║██║╚██╔╝██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████║██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝ """)



                                                                                                                                                         

print("Ready to start?")
print("Available Missions:")
print("1.Crack Admin password")
print("Enter the associated number")
choice=int(input(""))

if choice == 1:
    password()

