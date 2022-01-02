import os

################################################################################

try: # Check if pip is installed
    import pip

except: # Install pip if it isn't already installed
    if (input("You need to install 'pip' to continue. Type 1 if you agree") == "1"):
        os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        os.system("python get-pip.py")
        os.remove("get-pip.py")

################################################################################

while True:

    while True:
        inst = int(input("Do you want to install (1) or uninstall (0) a module?: "))
        if (inst == 1): 
            instType = "install"
            break
        elif (inst == 0): 
            instType = "uninstall"
            break
        else: 
            print("Wrong option!")

    modName = input("Type the module name: ")
    modName = modName.strip()
    
    try:
        os.system("pip "+instType+" "+modName)
    except:
        print("Unable to "+instType+" the module")

    r = int(input("Type 1 if you want to install/uninstall other module"))
    if (r != 1): break