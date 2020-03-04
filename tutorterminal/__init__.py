#!/usr/bin/python3
import os
import re
import shlex
import subprocess
import argparse

try:
    from ansimarkup import ansiprint
except ImportError:
    import platform 
    plt = platform.system()

    colors = {
        'yellow_bold': '\033[33;1m',
        'white': '\033[37m',
        'yellow': '\033[33m',
        'green': '\033[32m',
        'reset': '\033[0;0m'
    }
    
    if plt == "Windows":
        for k in colors:
            colors[k] = ""
    

    warn = (
        f"{colors['yellow_bold']}Oh no!\n"
        f"It looks you don't have {colors['white']}ansimarkup{colors['yellow']} installed.\n"
        f"This will not prevent the execution of the {colors['white']}tutorterminal{colors['yellow']}, but its installation is recommended.\n"
        f"To install it, just run the following command: \n"
        f"{colors['green']}pip install ansimarkup {colors['reset']} \n"
    )

    print(warn)
    ansiprint = lambda x, end="\n": print(re.sub("<.*?>", "", x), end=end)


def checkfile(content, exists=True):
    if exists ^ os.path.exists(content):
        ansiprint(
            "<fg red> Arquivo/diretório "
            + ("inexistente" if exists else "existente")
            + ": "
            + content
            + ". Procure por ajuda."
        )
        return False
    return True


def prompt():
    ansiprint(
        "<bold><green>[In]</green></bold> <light-blue>"
        + os.path.abspath(".")
        + "</light-blue>$ ",
        end="",
    )


def query_user(content):
    fancy_input = lambda: prompt() or input()

    user_input = fancy_input()
    while not user_input:
        ansiprint("Comando nao pode ser vazio.")
        user_input = fancy_input()
    while not re.match(content, user_input):
        ansiprint(
            "<fg red>Certeza que deseja continuar? A entrada parece ser diferente do indicado.</fg red> <bold>[s/N]</bold> ",
            end="",
        )
        user_test = input()
        if user_test == "n" or not user_test:
            user_input = fancy_input()
        else:
            break
    return user_input


def enter():
    ansiprint("<bold><white>Aperte ENTER para continuar...</white></bold>")
    input()


def run_command(content, free=False, auto=False):
    user_input = content
    if auto:
        prompt()
        ansiprint(content)
    else:
        user_input = shlex.split(query_user(content))
    output = "<bold><red>[Out]</red></bold> "
    err = "<bold><red>[ERR]</red></bold> "
    with subprocess.Popen(user_input,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                        ) as process:
        for line in process.stdout.readlines():
            ansiprint(output + line.decode("utf-8"), end="")
        for line in process.stderr.readlines():
            ansiprint(err + line.decode("utf-8"), end="")
        process.wait()
        if process.returncode != 0:
            ansiprint(
                "Algo parece ter dado errado... procure por ajuda ou verifique os comandos executados."
            )
            return False
        return True


def process(script):

    processing = ""
    tmp_processing = ""

    for line in script:
        if processing:
            if line.strip() == "###":
                f_open = open(processing, "w")
                f_open.write(tmp_processing)
                f_open.close()
                processing = ""
                tmp_processing = []
            tmp_processing += line
            continue

        if not line.strip():
            continue

        line = line.strip()

        if " " not in line:
            line += " "

        command, content = line.split(" ", 1)
        content = content.strip()

        if command == "!checkfile":  # checkfile not exists
            if not checkfile(content, False):
                exit(1)
        if command == "checkfile":  # checkfile
            if not checkfile(content):
                exit(1)
        if command == "##":
            ansiprint(content)
        if command == "#":
            ansiprint(content)
        if command == "enter":
            enter()
        if command == "run_free":
            if not run_command(content, free=True):
                exit(1)
        if command == "run":
            if not run_command(content):
                exit(1)
        if command == "run_auto":
            if not run_command(content, auto=True):
                exit(1)
        if command == "###":
            processing = content


def main():
    parser = argparse.ArgumentParser(description="Run Tutorterminal application.")

    parser.add_argument(
        "files", metavar="files", type=str, nargs="+", help="the script files to run"
    )

    args = parser.parse_args()
    files = args.files

    invalid_files = list(
        filter(lambda x: x[0], map(lambda x: (not os.path.isfile(x), x), files))
    )

    if invalid_files:
        for _, fname in invalid_files:
            files.remove(fname)
            ansiprint(
                "<red>Warning - '{}' not found!</red>".format(fname)
            )

    num_scripts = len(files)

    for index in range(num_scripts):
        f_name = files[index]
        ansiprint(
            "<bold><light-blue>Running script [{}/{}] - <yellow>'{}'</yellow></light-blue>".format(
                index + 1, num_scripts, f_name
            )
        )
        with open(f_name) as f:
            process(f.readlines())


if __name__ == "__main__":
    main()
