import os
import argparse

VERSION = "1.0"

BANNER = r"""
 ██████╗ ████████╗
██╔════╝ ╚══██╔══╝
██║  ███╗   ██║
██║   ██║   ██║
╚██████╔╝   ██║
 ╚═════╝    ╚═╝

GTConsole Framework
"""

COMANDOS = {
    "help": "Mostra esta ajuda",
    "version": "Mostra a versão",
    "about": "Informações do projeto",
    "banner": "Mostra o banner",
    "info-system": "Mostra informações do sistema",
    "clear": "Limpa a tela",
    "exit": "Sai do console",
}


def executar(comando):
    if comando == "help":
        print("\nComandos disponíveis:")
        for nome, desc in COMANDOS.items():
            print(f"  {nome:<12} - {desc}")

    elif comando == "version":
        print(f"GTConsole v{VERSION}")

    elif comando == "about":
        print("GTConsole Framework")
        print("Projeto experimental de console em Python.")

    elif comando == "banner":
        print(BANNER)

    elif comando == "info-system":
        os.system("neofetch")

    elif comando == "clear":
        os.system("clear")

    elif comando in ("exit", "sair"):
        return False

    elif comando.strip() == "":
        pass

    else:
        print(f"Comando não encontrado: {comando}")

    return True


parser = argparse.ArgumentParser(description="GTConsole Framework")

parser.add_argument(
    "-c",
    "--command",
    help="Executa um comando e encerra"
)

parser.add_argument(
    "--version",
    action="store_true",
    help="Mostra a versão"
)

parser.add_argument(
    "--banner",
    action="store_true",
    help="Mostra o banner"
)

parser.add_argument(
    "--about",
    action="store_true",
    help="Informações do projeto"
)

parser.add_argument(
    "--list-commands",
    action="store_true",
    help="Lista todos os comandos"
)

args = parser.parse_args()

if args.version:
    print(f"GTConsole v{VERSION}")
    exit()

if args.banner:
    print(BANNER)
    exit()

if args.about:
    print("GTConsole Framework")
    print("Projeto experimental de console em Python.")
    exit()

if args.list_commands:
    for cmd in COMANDOS:
        print(cmd)
    exit()

if args.command:
    executar(args.command)
    exit()

print(BANNER)
print("Digite 'help' para ajuda.\n")

while True:
    comando = input("GTConsole:~$ ")

    if not executar(comando):
        print("Encerrando GTConsole...")
        break