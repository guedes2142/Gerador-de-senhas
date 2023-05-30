#Rafael Guedes
#Linux Ubundo
#2023/05/30

import os
import random
import platform
import string
from colorama import Fore, Style
from datetime import datetime as dt
from time import sleep as sl
import sqlite3

class PasswordGenerator():
    def __init__(self):
        self.date = dt.now()
        self.system = platform.system()
        self.words = string.ascii_letters
        self.num = string.digits
        self.spec = string.punctuation

    def clear_console(self):
        if self.system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def date_base(self):
        ...
        #TODO banco de dados para amarzenar as senhas ja criada e para comparar com um nova que sera gerada para nao repetir senhas

    def generate_password(self):
        password_length = int(input(Fore.GREEN + 'Digite o comprimento da sua senha mínimo 12: ' + Style.RESET_ALL))
        if password_length < 12:
            print(Fore.RED + 'A senha não pode conter menos que 12 caracteres!!'+ Style.RESET_ALL)
            
        else:
            self.date = str(self.date).split('-')
            password = ''.join(random.choice(self.words + self.num + self.spec) for _ in range(password_length))
            password += random.choice(self.date)

        return password

    def save_password(self, password):
        save_in_txt = input(Fore.GREEN + 'Gostaria de salvar sua senha em um arquivo de texto?\n'
                            'Um arquivo chamado senhas.txt sera salvo na mesma pasta que está este aplicativo! \n'
                            'Recomendado S/n : ' + Style.RESET_ALL).lower()
        if save_in_txt.startswith('s'):
            with open('passwords.txt', 'a+') as save:
                save.write(f'{password}\n')
                print(Fore.YELLOW +'Senha salva com sucesso!!\n'
                      'Salve a em um pendrive ou nunca use softwares piratas em seu PC\n'
                      'para manter sua senha segura mais alguns caracteres foram incluso, deixando a mesma maior!'+ Style.RESET_ALL)
                sl(3)
        else:
            print(Fore.RED + 'Erro ao salvar a senha, Desculoe tente novamente'+ Style.RESET_ALL)

    def print_header(self):

        print(Fore.LIGHTMAGENTA_EX + '██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░')
        print(Fore.YELLOW + '██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗')
        print(Fore.BLUE + '██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║')
        print(Fore.GREEN + '██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║')
        print(Fore.CYAN + '██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝')
        print(Fore.MAGENTA + '╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░')

        print(Fore.LIGHTMAGENTA_EX + '░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░')
        print(Fore.MAGENTA + '██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
        print(Fore.LIGHTBLUE_EX + '██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝')
        print(Fore.BLUE + '██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗')
        print(Fore.LIGHTGREEN_EX + '╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
        print(Fore.GREEN + '░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')
        print(Fore.LIGHTRED_EX + '************ by.Rafael Guedes ************' + Style.RESET_ALL)
        print(Fore.BLUE + """ Security password generator CLI """ + Style.RESET_ALL)

    def run(self):
        while True:
            self.clear_console()
            self.print_header()
            user_input = input(Fore.MAGENTA + '1: gerar nova senha\n'
                '2: sair\n'
                '>>> ' + Style.RESET_ALL)

            if user_input.isdigit():
                user_input =int(user_input)
                if user_input == 1:
                    password = self.generate_password()
                    self.clear_console()
                    print(f'Sua senha nova\n'
                        f'{password}')
                    self.save_password(password)
                    new_password = input(Fore.LIGHTMAGENTA_EX + 'Gostaria de gerar uma nova senha ? S/n : '+ Style.RESET_ALL).lower()
                    if new_password.startswith('s'):
                        continue
                    else:
                        break
                elif user_input == 2:
                    print('Saindo........')
                    sl(2)
                    break
            elif user_input == 2:
                    print('Saindo........')
                    sl(2)
                    break
            else:
                print(Fore.LIGHTRED_EX + 'Digitou letras ou opcao invalida tente novamente'+ Style.RESET_ALL)
                print(Fore.BLUE + 'Saindoo .......'+ Style.RESET_ALL)
                sl(2)
                break

password_generator = PasswordGenerator()
password_generator.run()
                



       
           

        


