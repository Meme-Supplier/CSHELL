#!/usr/bin/env python3

"""
# 2025 Meme Supplier
memesupplierbusiness@gmail.com
Maintained by Meme Supplier
"""

# System modules
import os
import sys
import subprocess
import platform
import webbrowser
import shutil
from pathlib import Path
from colorama import Fore, init

# CSHELL modules
import cmdList

os.system("clear")
init(autoreset = True)

pythonMajor = sys.version_info.major # Ex: 3.x.x
pythonMinor = sys.version_info.minor # Ex: x.12.x
pythonMicro = sys.version_info.micro # Ex: x.x.3
pythonVersion = str(pythonMajor) + "." + str(pythonMinor) + "." + str(pythonMicro)
pythonVersionShort = str(pythonMajor) + "." + str(pythonMinor)

cshellVer = "v1.4.5"

sufficientPacMan = False

locked = False
passwordSet = False
password = ''

homePath = os.path.expanduser("~")
homeFolder = os.path.basename(homePath)
CSHELLpath = os.path.expanduser("~/CSHELL")

if os.path.exists(CSHELLpath):
    try:
        shutil.rmtree(CSHELLpath)
    except:
        print(Fore.RED + "Error! Unable to remove " + homePath + "/CSHELL! Please delete it manually!")

"""
Define
functions
"""

def processCommand(answer):
    # Goes through and executes commands
    
    match answer:
        case "clear"     : os.system('clear')
        case "help"      : help()
        case "python"    : command("python" + pythonVersionShort)
        case "cmds"      : cmdList.list()
        case "exit"      : sys.exit(0)
        case "shutdown"  : command("shutdown now")
        case "reboot"    : command("reboot")
        case "ping"      : command("ping")
        case "credits"   : credits()
        case "ver"       : ver()
        case "update"    : update()  # updates your system
        case "upgrade"   : upgrade()  # updates CSHELL
        case "lock"      : lock()
        case "xray"      : edit()
        case "reload"    : reload()
        case "in"        : input()
        case "uptime"    : command("uptime")
        case "uninstall" : uninstall()
        case "quit"      : quit()
        case "clean"     : clean()
        case "ip"        : command("hostname -I")

        # Commands that require syntax (show usage)
        case "echo"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "echo <message>")
        case "web"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "web <site>")
        case "expr"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "expr <equation>")
        case "bash"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "bash <command>")
        case "wait"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "wait <time (seconds)>")
        case "pwd"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pwd <password>")
        case "edit"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "edit <path to text file>")
        case "script"  : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "script <script path>")
        case "pscript" : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pscript <script path>")
        case "ls"      : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "ls <directory>")
        case "del"     : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "del <path to file/directory>")
        case "newdir"  : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "newdir <path to directory>")
        case "pm"      : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "pm <apt/dnf/pacman> <rest of the command>")
        case "copy"    : print(Fore.CYAN + "Usage: " +
                               Fore.BLUE + "copy <path to file> <path to destination>")
        case ''        : None

        case _ :

            # Handle multiple commands separated by "&&"
            if " && " in answer:
                for cmd in answer.split(" && "):
                    processCommand(cmd.strip())

                return  # Exit after handling multiple commands

            # Multi-syntax commands
            if   answer.startswith ("echo ")    : print  (answer.replace("echo " , "" , 1))
            elif answer.startswith ("expr ")    : print  (eval(answer.replace("expr " , "" , 1)))
            elif answer.startswith ("bash ")    : command(answer.replace("bash " , "" , 1))
            elif answer.startswith ("web ")     : web    (answer.replace("web " , "" , 1))
            elif answer.startswith ("wait ")    : wait   (answer.replace("wait " , "" , 1))
            elif answer.startswith ("pwd ")     : setPwd (answer.replace("pwd " , "" , 1))
            elif answer.startswith ("script ")  : script (answer.replace("script " , "" , 1))
            elif answer.startswith ("pscript ") : command("python3 " + answer.replace("pscript " , "" , 1))
            elif answer.startswith ("in ")      : input  (answer.replace("in " , "" , 1) + '\n')
            elif answer.startswith ("ls ")      : command("\nls " + answer.replace("ls " , "" , 1))
            elif answer.startswith ("flatpak")  : command(answer)
            elif answer.startswith ("git")      : git    ()
            elif answer.startswith ("create ")  : command("touch " + answer.replace("create " ,"" , 1))
            elif answer.startswith ("del ")     : delete (answer.replace("del " , "" , 1))
            elif answer.startswith ("pm ")      : pm     (answer.replace("pm " , "" , 1))
            elif answer.startswith ("python")   : command(answer)
            elif answer.startswith ("copy ")    : command("cp " + answer.replace("copy " , "" , 1))
            elif answer.startswith ("ping ")    : command(answer)
            elif answer.startswith ("edit ")    : command("nano " + answer.replace("edit " , "" , 1))

            # If nothing checks out
            else: 
                print(Fore.RED + answer + ": invalid command.")

"""
Scripting
Commands
"""

def web(page):
    if page.startswith("https://www.") or page.startswith("http://www."):
        webbrowser.open_new(page)
    else:
        webbrowser.open_new("https://www." + page)

def pm(cmd):
    if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):
        command(cmd)
    else:
        print(Fore.RED + "Unable to remove packages: Unsupported package manager!")

def newdir(dir):
    Path(dir).mkdir(parents = True,
                    exist_ok = True)
    
    # Verifies of the directory exists
    if os.path.exists(dir):
        print(Fore.GREEN + "Directory successfully created!")
    else:
        print("Error! File/Directory doesn't exist!\nTry again and remember to use the full path!")

def clean():
    if shutil.which("apt"):   
        command("sudo apt autoremove")

    elif shutil.which("dnf"):   
        command("sudo dnf autoremove")

    elif shutil.which("pacman"):
        command("sudo pacman -Rns $(pacman -Qdtq)")
    else:
        print(Fore.RED + "Unable to remove packages: Unsupported package manager!")

def delete(file):
    if os.path.exists(file):
        command("rm -rf " + file)
    else:
        print(Fore.RED + "Error! File/Directory doesn't exist! Remember to use the full path!")

def git():
    if gitInstalled():
        command(answer)
    else:
        print(Fore.RED + "Git is not installed. Please install Git.")

def uninstall():
    global uninstalled
    uninstalled = True

    choice = input(Fore.RED + "Are you sure you want to uninstall CSHELL?\n" +
                   Fore.WHITE)

    if choice == 'Y' or choice == 'y':
        command("bash ~/cshell/uninstall.sh")
        sys.exit(0)
    else:
        print(Fore.GREEN + "\nAborted.")

def wait(value):
    command("sleep " + str(value))

def command(command):
    subprocess.run([command],
                    shell = True)
    
def setPwd(pwd):
    global password
    global passwordSet

    if len(pwd) < 5:
        print(Fore.RED  + "Password must be at least " +
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

        attemptsLeft = 5

        while locked:
            
            if attemptsLeft != 0:
                print(Fore.CYAN + "Enter password to unlock CSHELL.")
                pwdAttempt = input()

                if pwdAttempt == password:
                    locked = False
                else:
                    print(Fore.RED + "\nIncorrect password!\n")
                    attemptsLeft -= 1
            else:
                os.system("clear")
                print(Fore.RED + "You are out of attempts! Wait 5 seconds to try again!")
                wait(5)
                attemptsLeft = 5
    else:
        print(Fore.RED  + "You need to set a password first in order to use this command.")
        print(Fore.RED  + "Use the command " +
              Fore.BLUE + "\"pwd <password>\" " + 
              Fore.RED  + "to set your password")

def update():
    if shutil.which("apt"):   
        command("sudo apt update && sudo apt upgrade")

    elif shutil.which("dnf"):   
        command("sudo dnf update")

    elif shutil.which("pacman"):
        command("sudo pacman -Syu")
    else:
        print(Fore.RED + "Unable to update: Unsupported package manager!")

def upgrade():
    print(Fore.CYAN + "Do you want to update CSHELL?\n" +
          Fore.BLUE + "(Y/N)\n")

    print(Fore.RED + "Note: This will uninstall then reinstall CSHELL.")

    choice = input()

    if choice == 'Y' or choice == 'y': 
        command("bash ~/cshell/upgrade.sh")
        sys.exit(0)
    else:
        print(Fore.RED + "Aborted.")

def edit():
    command("nano ~/cshell/cshell.py")
    print(Fore.BLUE + "\nChanges applied.")
    reload()

def reload():
    
    print(Fore.CYAN + "\nWould you like to reload CSHELL?")
    choice = input()

    if choice == 'Y' or choice == 'y': 
        print("Reloading script...")
        
        os.execv(sys.executable,
                ["python" + pythonVersion] +
                sys.argv)
    else:
        print(Fore.RED + "Aborted.")    

def script(scriptPath):
    if scriptPath.startswith("~/"):
        print(Fore.RED + "The path to the script must be the full path. " +
              Fore.CYAN + "\nEx: " +
              Fore.BLUE + "/home/(your username)/file.cshell")
    else:
        if answer.endswith(".cshell"):
            try:
                with open(scriptPath, "r") as file:
                        for line in file:
                            processCommand(line.strip())
            except:
                print(Fore.RED + "Error: File/directory not found!")
        
        else:
            print(Fore.RED  + "Unsupported file extension! CSHELL only supports files ending with \"" +
                  Fore.BLUE + ".cshell" +
                  Fore.RED  + "\"!")

def credits():
    print(Fore.CYAN   + "Meme Supplier" +
          Fore.BLUE   + ": owner, programmer, maintainer\n" +
          Fore.YELLOW + "Contact: " +
          Fore.BLUE   + "memesupplierbusiness@gmail.com\n" +
          Fore.GREEN  + "2025 Meme Supplier")

def help():
    if sufficientPacMan and isLinux:
        print(Fore.CYAN   + "Welcome to " +
              Fore.GREEN  + "CSHELL " +
              Fore.YELLOW + cshellVer)
        print(Fore.CYAN   + "Type " +
              Fore.BLUE   + "\"cmds\"" +
              Fore.CYAN   + " for some commands!\n")

def ver():
#   CSHELL version
    print(Fore.CYAN  + "\nCSHELL" +
          Fore.BLUE  + " version: " +
          Fore.GREEN + cshellVer)
    print(Fore.CYAN  + platform.system() ,
          Fore.BLUE  + platform.release())

#   Python version
    print(Fore.CYAN + "Python " +
          Fore.BLUE + pythonVersion +
          '\n')

def gitInstalled(): # Is git installed?
    try:
        subprocess.run(["git", "--version"],
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE,
                       check  = True)
        return True
    except (subprocess.CalledProcessError,
            FileNotFoundError):
        return False
    
def isLinux(): # Are you using Linux?
    if platform.system() == "Linux":
        return True
    else:
        return False

# Do you have a supported package manager?
if shutil.which("apt") or shutil.which("dnf") or shutil.which("pacman"):   
    sufficientPacMan = True
else:
    sufficientPacMan = False

    print(Fore.RED  + "Unsupported package manager! Please use " +
          Fore.BLUE + "Apt" +
          Fore.RED  + ", " +
          Fore.BLUE + "Dnf" +
          Fore.RED  + ", or " +
          Fore.BLUE + "Pacman" +
          Fore.RED  + ".")
    
if not isLinux():
    print(Fore.CYAN + "This script is for " +
          Fore.BLUE + "Linux " +
          Fore.RED  + "only! " +
          Fore.CYAN + "Either install Linux for edit the code " +
          Fore.RED  + "(it may not work as expected or break if you edit the code).\n"  )

    sys.exit(1)

"""
Program
"""

help()

while True and isLinux() and not locked and sufficientPacMan:

    answer = input(Fore.BLUE   + "CSHELL" +
                   Fore.GREEN  + '$' +
                   Fore.CYAN   + '~' +
                   Fore.WHITE  + ': ')

    processCommand(answer)
