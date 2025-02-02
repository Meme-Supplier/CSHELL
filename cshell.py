
"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

def CShell():

    import os, sys, subprocess, platform, webbrowser, shutil
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    
    os.system('clear')

    cshellVer = "v0.5.5"

    locked = False
    password = ()
    passwordSet = False

    """
    Define
    functions
    """

    def commands():
        print('\n' +
    #       Color        Output          
            Fore.YELLOW + "Available commands:\n")
        
        """
        Command list
        """

    #   Exit
        print(Fore.CYAN + "exit " +
            Fore.GREEN + "Exits CShell")
    #   Clear
        print(Fore.CYAN + "clear" +
            Fore.GREEN + " Clears the screen")
    #   Help
        print(Fore.CYAN + "help" +
            Fore.GREEN + " Some info")
    #   Cmds
        print(Fore.CYAN + "cmds" +
            Fore.GREEN + " Lists available commands")
    #   Python
        print(Fore.CYAN + "python" +
            Fore.GREEN + " Opens python")
    #   Ver
        print(Fore.CYAN + "ver" +
            Fore.GREEN + " Shows CShell's version")
    #   Lock
        print(Fore.CYAN + "lock" +
            Fore.GREEN + " Locks the terminal")
    #   Edit
        print(Fore.CYAN + "edit" +
            Fore.GREEN + " Allows you to easily edit CShell")
    #   Edit
        print(Fore.CYAN + "reload" +
            Fore.GREEN + " Reloads CShell")
    #   Shutdown
        print(Fore.CYAN + "shutdown" +
            Fore.GREEN+ " Shuts down your system")
    #   Wait
        print(Fore.CYAN + "wait"     +
            Fore.BLUE + " <time (seconds)>" +
            Fore.GREEN + " Waits your desired time")
    #   Echo
        print(Fore.CYAN + "echo"     +
            Fore.BLUE + " <text>" +
            Fore.GREEN + " Prints text")
    #   Command
        print(Fore.CYAN + "command " +
            Fore.BLUE +"<app>" +
            Fore.GREEN + " Runs normal shell commands " +
            Fore.RED + "Notice: commands like \"cd\" and \"dir\" won't work.")
    #   Expr
        print(Fore.CYAN + "expr "    +
            Fore.BLUE + "<equation>" +
            Fore.GREEN + " Solves a math equation")
    #   Web
        print(Fore.CYAN + "web "     +
            Fore.BLUE + "<website>" +
            Fore.GREEN + " Opens your desired website")
    #   Pwd
        print(Fore.CYAN + "pwd "     +
            Fore.BLUE + "<password>" +
            Fore.GREEN + " Sets a password " +
            Fore.RED + "Notice: Password has to be at least 5 characters long.")
    #   Update
        print(Fore.CYAN + "update "     +
            Fore.GREEN + " Updates your device " +
            Fore.RED + "Notice: Only supports Fedora, Arch, and Debian based distros.")
        print()

    """
    Info
    """

    def credits():
        print(Fore.CYAN  + "Meme Supplier" +
            Fore.BLUE  + ": owner, programmer, maintainer\n" +
            Fore.GREEN + "2025 Meme Supplier")

    def help():
        #         Color        Output
        print(Fore.CYAN   + "Welcome to " +
            Fore.GREEN  + "CShell " +
            Fore.YELLOW + cshellVer)
        print(Fore.CYAN   + "Type " +
            Fore.BLUE   + "\"cmds\"" +
            Fore.CYAN   + " for some commands!\n")
    
    def ver():
    #         Color        Output
        print(Fore.CYAN  + '\nCSHELL' +
            Fore.BLUE  + ' version: ' +
            Fore.GREEN + cshellVer)
        print(Fore.CYAN  + platform.system() ,
            Fore.BLUE  + platform.release() , '\n')
    
    """
    Scripting
    Commands
    """

    def wait(value):
        command("sleep " + value)

    def command(command):
        subprocess.run([command],
                    shell = True)
    def setPwd(pwd):
        global password
        global passwordSet
        if len(pwd) <= 4: print(Fore.RED  + "Password must be at least " +
                                Fore.BLUE + "5 " +
                                Fore.RED  + "characters long!")
        else:
            password = pwd
            passwordSet = True
            print(Fore.CYAN + "Password has been set to " +
                Fore.BLUE + password)

    def lock():
        if passwordSet:
            os.system("clear")
            global locked
            locked = True

            while locked:
                print(Fore.CYAN + "Enter password to unlock CShell.")
                pwdAttempt = input()
                if pwdAttempt == password : locked = False
                else: print(Fore.RED + "Incorrect password!\n")
        else:
            print(Fore.RED + "You need to set a password first in order to use this command.")
            print(Fore.RED + "Use the command " +
                Fore.BLUE + "\"pwd <password>\" " + 
                Fore.RED + "to set your password")
        

    def update():
        if shutil.which("apt"):
            command("sudo apt update && sudo apt upgrade")
        elif shutil.which("dnf"):
            command("sudo dnf update")
        elif shutil.which("pacman"):
            command("sudo pacman -Syu")
        else:
            print(Fore.RED + "Unsupported package manager!")

    def edit():
        try:    
            command("cd " + currentDirectory + " && sudo nano cshell.py")
        except:
            print(Fore.RED + "Unable to use command: Nano is not installed!")
        
        print(Fore.BLUE + "\nChanges applied.")
        
        reload()

    def reload():
        
        print(Fore.CYAN + "Would you like to reload CShell?")
        choice = input()
        
        if choice == 'Y' or choice == 'y': 
            print(Fore.CYAN + "\nReloading CShell...")
            command("cd " + currentDirectory + " && bash reload.sh")
            sys.exit(0)
        else:
            print(Fore.RED + "Aborted.")

    def processCommand(answer):
#       Goes through and executes commands
        match answer:
#                Input        Response  
            case "clear"    : os.system(answer)
            case "help"     : print() , help()
            case "cmds"     : commands()
            case "exit"     : sys.exit(0)
            case "python"   : command("python3")
            case "shutdown" : command("shutdown now")
            case "credits"  : credits()
            case "ver"      : ver()
            case "update"   : update()
            case "lock"     : lock()
            case "edit"     : edit()
            case "reload"   : reload()
    
            #Commands that require syntax
            #(Show usage)

            case "echo"    : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "echo <message>")
            case "expr"    : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "expr <equation>")
            case "command" : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "command <command>")
            case "web"     : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "web <website>")
            case "wait"    : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "wait <time (seconds)>")
            case "pwd"     : print(Fore.CYAN + "Usage: " +
                                Fore.BLUE + "pwd <password>")
                
            case ''        : () # Does nothing

            case _ :

    #           Multi-syntax
                if   answer.startswith ("echo ")    : command(answer)
                elif answer.startswith ("expr ")    : command(answer)
                elif answer.startswith ("command ") : command(answer.replace("app ","",1))
                elif answer.startswith ("web ")     : webbrowser.open_new(answer.replace("web ","",1))
                elif answer.startswith ("wait ")    : wait(answer.replace("wait ","",1))
                elif answer.startswith ("pwd ")     : setPwd(answer.replace("pwd ","",1))
    #           If nothing checks out
                else: print(Fore.RED +
                        answer +
                        ": command or program not found")

    """
    Program
    """

    if platform.system() == 'Linux':
        isLinux = True
    else:
        isLinux = False

    if not isLinux:
    #         Color       Output
        print(Fore.CYAN + "This script is for " +
            Fore.BLUE + "Linux" +
            Fore.RED  + " only!" +
            Fore.CYAN + " Either install Linux for edit the code " +
            Fore.RED  + "(it may not work as expected or break if you edit the code).\n"  )
        sys.exit(1)

    # Attempts to confirm Colorama's existence
    try:
        coloramaInstalled = True 
        from colorama import Fore, init
        init(autoreset=True)

    # If not installed, you will be prompted to install Colorama.
    except:
        coloramaInstalled = False
        
        print(Fore.RED + "Colorama doesn't appear to be installed!" +
            Fore.RED + "\nWould you like to install it?\n(Y or N)\n")
        
        choice = input("\n")
        
        if choice == 'Y' or choice == 'y':
            # Opens the download page for Colorama
            webbrowser.open_new("https://pypi.org/project/colorama/")
        else:
            # Cancels the action, and exits CShell
            print("\nAborted.\nPlease install Colorama to continue.")

    if isLinux : help()

    while True and coloramaInstalled and isLinux and not locked:
    #                  Color        Output
        answer = input(Fore.BLUE  + 'CShell' +
                    Fore.GREEN + '$' +
                    Fore.YELLOW + '~' +
                    Fore.WHITE + ': ')
        
        processCommand(answer)
    
CShell()

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""
