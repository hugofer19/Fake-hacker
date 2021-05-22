# Este script não tem qualquer efeito
# O mesmo foi desenvolvido somente para descobrir e testar alguns modulos
import sys
from colorama import Fore, Back, Style
from colorama.ansi import Fore
from colorama import init
import time
import string
import random
import socket as s


def Hacker():
    site = input("Insere o domínio do site que desejas invadir: ")
    try:
        ip = s.gethostbyname(site)
    except ValueError:
        print('O domínio indicado não é válido!')
    print(Fore.BLUE + 'O ip do ' + site + ' é ' +
          Fore.YELLOW + ip + Fore.BLUE + '.')
    time.sleep(1)
    i = int(input(Fore.WHITE + "Insere o número de linhas que desejas codificar: "))
    while i > 1:
        i -= 1
        letras = string.ascii_lowercase
        n = random.randint(14, 61)
        print(Fore.RED + 'Codificando: ' + Fore.GREEN +
              ''.join(random.choice(letras) for i in range(n)))
        time.sleep(0.3)
        if i == 1:
            print(Fore.YELLOW + 'Acesso Garantido Com Sucesso 🔓')


Hacker()
