import random as rd
import os

############
mode = "bark" #edit this for default mode. modes: bark (default) / system (bash)
############

user = os.environ.get("USER") or 'NOUSER' #Export user of actual shell
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLOCKRED = "\033[41m"
BLOCKGREEN = "\033[42m"
BLOCKYELLOW = "\033[43m"
BLOCKBLUE = "\033[44m"
BLOCKMAGENTA = "\033[45m"
BLOCKCYAN = "\033[46m"
RESET = "\033[0m"
PATHCOLOR1 = BLUE + BOLD
PATHCOLOR2 = MAGENTA + ITALIC
USERCOLOR1 = GREEN + BOLD           # change default prompt colors
USERCOLOR2 = BLUE                   # when you start the shell.
INPUTCOLOR1 = RESET
INPUTCOLOR2 = RESET

helptxt = { ### Alphabetical commands
    "backdir": "change directory to the back one.",
    "cat": "show the content of a file.",
    "cd": "change the current directory.",
    "clear": "clear the screen.",
    "credits": "show the credits of this shell.",
    "date": "show the actual date and time.",
    "echo": "write something in the console in upper case.",
    "exe": "run a binary file.",
    "exit/^C+enter": "bye bye!",
    "fetch": "show system information.",
    "g++": "compile a C++ file into a binary file.",
    "gcc": "compile a C file into a binary file.",
    "help": "show this help.",
    "hi": "a greeting with your name!.",
    "ls": "list the files in the current directory.",
    "matrix": "show a matrix rain effect.",
    "mkdir": "create a new directory.",
    "mod": "modify a file with the nano editor.",
    "neovim": "Open a file with neovim.",
    "pwd": "get the path of where you are",
    "reload": "reload and apply the currents settings.",
    "rm": "remove a file.",
    "rmdir": "remove a directory.",
    "rnum": "bring you a random number.",
    "runpy": "run a python file.",
    "setcolors": "personalize your prompt.",
    "setmode": "set shell mode.",
    "settings": "change default settings.",
    "setuser": "set your username.",
    "showinfo": "show the barkell version.",
    "syscommand": "run a system command.",
    "time": "show the current time.",
    "whoami": "show your username.",
}

def help():
    print("The available commands are:\n")
    for first, second in helptxt.items():
        print(f" {GREEN}{first}{RESET}  --  {second}")
    print("")

def settings():
    global mode
    global PATHCOLOR1
    global PATHCOLOR2
    global USERCOLOR1
    global USERCOLOR2
    global INPUTCOLOR1
    global INPUTCOLOR2
    colors = {"YELLOW","BLUE","RED","MAGENTA","GREEN","CYAN","BOLD"}
    src = "~/BarkellPreview/barkell.py"

    while True:
        def sel():
            option = input(f"{YELLOW}Settings{RESET}:\n 1.- {GREEN}Mode{RESET}.\n 2.- {GREEN}System prompt{RESET}.\n 3.- {GREEN}Barkell prompt{RESET}.\n{YELLOW}Option{RESET}: ")
            return option.strip()
        option = sel()
        while option != "1" and option != "2" and option != "3":
            print(f"{BLOCKRED}Error{RESET}: Invalid option, try again.")
            option = sel()

        if option == "1":
            def selmode():
                select = input(f"{YELLOW}Modes{RESET}:\n 1.- {BLUE}Barkell{RESET}.\n 2.- {MAGENTA}System{RESET}.\n{YELLOW}Option{RESET}: ")
                return select.strip()
            select = selmode()
            while select != "1" and select != "2":
                print(f"{BLOCKRED}Error{RESET}: Invalid option, try again.")
                select = selmode()
            if select == "1":
                mode = "bark"
            if select == "2":
                mode = "system"
            os.system(f"sed -i 's|^mode = .*|mode = \"{mode}\" #edit this for default mode. modes: bark (default) / system (bash)|' {src}")
            print(f"{GREEN}Done{RESET}, type {YELLOW}'reload'{RESET} to apply changes.")

        elif option == "2":
            usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
            while usercolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
            USERCOLOR2 = globals()[usercolor]
            os.system(f"sed -i 's|^USERCOLOR2 = .*|USERCOLOR2 = {usercolor}|' {src}")

            pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
            while pathcolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
            PATHCOLOR2 = globals()[pathcolor]
            os.system(f"sed -i 's|^PATHCOLOR2 = .*|PATHCOLOR2 = {pathcolor}|' {src}")

            inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
            while inputcolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
            INPUTCOLOR2 = globals()[inputcolor]
            os.system(f"sed -i 's|^INPUTCOLOR2 = .*|INPUTCOLOR2 = {inputcolor}|' {src}")
            print(f"{GREEN}Done{RESET}, type {YELLOW}''{RESET} to apply changes.")

        elif option == "3":
            usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
            while usercolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
            USERCOLOR1 = globals()[usercolor]
            os.system(f"sed -i 's|^USERCOLOR1 = .*|USERCOLOR1 = {usercolor}|' {src}")

            pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
            while pathcolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
            PATHCOLOR1 = globals()[pathcolor]
            os.system(f"sed -i 's|^PATHCOLOR1 = .*|PATHCOLOR1 = {pathcolor}|' {src}")

            inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
            while inputcolor not in colors:
                print(f"{RED}Error{RESET}: Invalid color or color not found.")
                inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
            INPUTCOLOR1 = globals()[inputcolor]
            os.system(f"sed -i 's|^INPUTCOLOR1 = .*|INPUTCOLOR1 = {inputcolor}|' {src}")
            print(f"{GREEN}Done{RESET}, type {YELLOW}'reload'{RESET} to apply changes.")

        again = input(f"{YELLOW}Quit{RESET} settings? y|n: ").strip().lower()
        if again != "n":
            break

def sysconsole():
    directory = os.getcwd().replace(os.getenv("HOME", ""), "~", 1) # abreviate directory

    if user == 'NOUSER':
        command = input(f"{PATHCOLOR2}{directory}{RESET} {INPUTCOLOR2}ʎ{RESET} ").strip()
    else:
        command = input(f"{USERCOLOR2}{user}{RESET} {PATHCOLOR2}{directory}{RESET} {INPUTCOLOR2}ʎ {RESET}").strip()

    if command == "setmode":
        pass
    elif command == "reload":
        os.system("python ~/BarkellPreview/barkell.py")
        exit()
    elif command == "settings":
        settings()
    elif command == "setcolors":
        setcolor()
        pass
    else:
        os.system(f"{command}")
        print(RESET,end="")

    return command.lower()

def barkconsole():
    directory = os.getcwd().replace(os.getenv("HOME", ""), "~", 1)

    if user == 'NOUSER':
        line = input(f"{BOLD}{BLUE}{directory}{RESET} $ ")
    else:
        line = input(f"{USERCOLOR1}{user} {RESET}{PATHCOLOR1}{directory}{RESET}{INPUTCOLOR1} ${RESET} ")
    return line.strip().lower()

def setcolor():
    global PATHCOLOR1
    global PATHCOLOR2
    global USERCOLOR1
    global USERCOLOR2
    global INPUTCOLOR1
    global INPUTCOLOR2
    colors = {"YELLOW","BLUE","RED","MAGENTA","GREEN","CYAN","BOLD"}

    tochange = input(f"{GREEN}Prompts{RESET}:\n 1.- {BLUE}Barkell{RESET} prompt.\n 2.- {MAGENTA}System{RESET} prompt.\n{YELLOW}To change{RESET} 1 | 2: ")
    while tochange != "1" and tochange != "2":
        print(f"{BLOCKRED}Error{RESET}: Invalid option, try again.")
        tochange = input(f"{GREEN}Prompts{RESET}:\n 1.- {BLUE}Barkell{RESET} prompt.\n 2.- {MAGENTA}System{RESET} prompt.\n{YELLOW}To change{RESET} 1 | 2: ")

    if tochange == "1":
        usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
        while usercolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
        USERCOLOR1 = globals()[usercolor]

        pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        while pathcolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        PATHCOLOR1 = globals()[pathcolor]

        inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
        while inputcolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            inputcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        INPUTCOLOR1 = globals()[inputcolor]
        print(f"{GREEN}Applied{RESET}!")

    elif tochange == "2":
        usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
        while usercolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            usercolor = input(f"{YELLOW}User{RESET} color: ").strip().upper()
        USERCOLOR2 = globals()[usercolor]

        pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        while pathcolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            pathcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        PATHCOLOR2 = globals()[pathcolor]

        inputcolor = input(f"{YELLOW}Input{RESET} color: ").strip().upper()
        while inputcolor not in colors:
            print(f"{RED}Error{RESET}: Invalid color or color not found.")
            inputcolor = input(f"{YELLOW}Path{RESET} color: ").strip().upper()
        INPUTCOLOR2 = globals()[inputcolor]
        print(f"{GREEN}Applied{RESET}!")


def funciones():
    global user
    global mode

    if mode == "system":
        comando = sysconsole()

    elif mode == "bark":
        comando = barkconsole()

    if comando == "setmode":
        def sel():
            select = input(f"{YELLOW}Modes{RESET}:\n 1.- {BLUE}Bark{RESET}: Default mode, default commands.\n 2.- {MAGENTA}System{RESET}: The linux bash default commands.\n{YELLOW}Mode{RESET}: ")
            return select.strip()
        select = sel()
        while select != "1" and select != "2":
            print(f"{BLOCKRED}Error{RESET}: Invalid option, try again.")
            select = sel()
        if select == "1":
            mode = "bark"
        if select == "2":
            mode = "system"

    if mode == "bark":
        if comando == " " or comando == "":
            print(f"{BLOCKYELLOW}VoidCommand{RESET}: Type 'help' to see available commands.")

        elif comando == "backdir":  ##### Alphabetical commands
            try:
                os.chdir("..")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "cat" or comando == "showfile" or comando == "showall" or comando == "show":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                with open(ruta, "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"{BLOCKRED}FileNotFoundError{RESET}:Path {BLUE}{ruta}{RESET} not found.")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "cd":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.chdir(ruta)
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "clear":
            os.system("clear")

        elif comando == "dt" or comando == "date":
            os.system("date")

        elif comando == "echo":
            entrada = input(f"{YELLOW}Message{RESET}: ").upper()
            print(entrada)

        elif comando == "exe" or comando == "execute" or comando == "runbin" or comando == "./" or comando == "runbinfile" or comando == "bin":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.system(f"chmod +x {ruta}")
                os.system(f"./{ruta}")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "exit" or comando == "quit":
            pass

        elif comando == "fetch" or comando == "fastfetch" or comando == "neofetch":
            print("")
            os.system("fastfetch")
            print("")

        elif comando == "g++" or comando == "clang++" or comando == "compilecpp":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.system(f"g++ {ruta} -o {ruta}.out")
            except FileNotFoundError:
                print(f"{BLOCKRED}FileNotFoundError{RESET}:Path {BLUE}{ruta}{RESET} not found.")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "gcc" or comando == "clang" or comando == "compilec" or comando == "compilecfile":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.system(f"gcc {ruta} -o {ruta}.out")
            except FileNotFoundError:
                print(f"{BLOCKRED}FileNotFoundError{RESET}:Path {BLUE}{ruta}{RESET} not found.")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "help":
            help()

        elif comando == "hi":
            if 'NOUSER' in user:
                print(f'{YELLOW}Note: Set your user with {RESET}{BLOCKYELLOW}"setuser"{YELLOW}.{RESET}')

            else:
                print(f"Hello from {BLOCKMAGENTA}Barkell{RESET} {BLUE}{user}{RESET}!")

        elif comando == "ls":
            try:
                print(f"- - - - - - - - - - - - - - - - - - - - - - - - -{BOLD}")
                os.system("ls -v")
                print(f"{RESET}- - - - - - - - - - - - - - - - - - - - - - - - -")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "matrix" or comando == "cmatrix" or comando == "matrixrain":
            os.system("cmatrix")

        elif comando == "mkdir":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.mkdir(ruta)
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "mod" or comando == "edit" or comando == "nano" or comando == "open":
            ruta = input(f"{YELLOW}File:{RESET} ")
            try:
                os.system(f"nano {ruta}")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "nvim" or comando == "neovim" or comando == "vim":
            file = input(f"{YELLOW}File{RESET}: ")
            os.system(f"nvim {file}")

        elif comando == "pwd" or comando == "whereami":
            allpath = os.getcwd()
            print(f"{GREEN}Path{RESET}: {allpath}")

        elif comando == "reload":
            os.system("python ~/Barkell/barkell0_0_9.py")
            exit()

        elif comando == "rm" or comando == "remove" or comando == "delete" or comando == "dl":
            ruta = input(f"{YELLOW}File: {RESET}")
            try:
                os.remove(ruta)
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "rmdir" or comando == "removedir" or comando == "rmdirectory":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.system(f"rm -rf {ruta}")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "rnum":
            try:
                minimo = int(input(f"{YELLOW}Minimum: {RESET}"))
                maximo = int(input(f"{YELLOW}Maximum: {RESET}"))
                rnum = rd.randint(minimo,maximo)
                print(f"The random number is: {BLUE}{rnum}{RESET}")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "runpy" or comando == "runpython" or comando == "python":
            ruta = input(f"{YELLOW}Path: {RESET}")
            try:
                os.system(f"python3 {ruta}")
            except Exception as err:
                print(f"{BLOCKRED}Error:{RESET} {YELLOW}{err}{RESET}.")

        elif comando == "setcolors":
            setcolor()

        elif comando == "settings":
            settings()

        elif comando == "setmode":
            pass

        elif comando == "setuser":
            user = input(f"{YELLOW}User: {RESET}")

        elif comando == "showinfo":
            print(f"{GREEN}.:Barkell:.{RESET}\t{BLUE}v:{RESET} 0.1.0")
            print(f"{YELLOW}Type {RESET}{BLOCKYELLOW}help{RESET}{YELLOW} to see the available commands.{RESET}")

        elif comando == "time" or comando == "whattimeisit" or comando == "whattimeis":
            os.system("date +%T")

        elif "whoami" in comando:
            print(user)

        else:
            print(f"{RED}\033[5mCommandNotFound{RESET}: {comando} is not a command.\n{YELLOW}Type {RESET}{BLOCKYELLOW}help{RESET}{YELLOW} to see the available local commands.{RESET}")
    return comando

'''
    MAIN BUCLE
'''

try:
    comando = funciones()
    while comando != "exit" and comando != "quit":
        try:
            comando = funciones()

        except KeyboardInterrupt:
            if user == 'NOUSER':
                print("Goodbye!")

            else:
                clrs = ("GREEN","BLUE","MAGENTA","YELLOW","CYAN","RED")
                pos = rd.randint(0,5)
                color = clrs[pos]
                cl = globals().get(color)
                print(f"Goodbye {cl}{user}{RESET}!")
                exit()
    if user == 'NOUSER':
        print("Goodbye!")
    else:
        clrs = ("GREEN","BLUE","MAGENTA","YELLOW","CYAN","RED")
        pos = rd.randint(0,5)
        color = clrs[pos]
        cl = globals().get(color)
        print(f"Goodbye {cl}{user}{RESET}!")

except KeyboardInterrupt:
    if user == 'NOUSER':
        print("Goodbye!")
    else:
        clrs = ("GREEN","BLUE","MAGENTA","YELLOW","CYAN","RED")
        pos = rd.randint(0,5)
        color = clrs[pos]
        cl = globals().get(color)
        print(f"Goodbye {cl}{user}{RESET}")
