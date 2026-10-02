# Loop while

'''funciona mas ta feio.
import os
os.system('cls')

while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")

    if x == '1':
        print('\nVai comer')
        input('Tecle [Enter] para continuar.')

    elif x == '2':
        print('\nBeba água')
        input('Tecle [Enter] para continuar.')

    elif x == '3':
        print('\nGrite: MAMÃE!!!')
        input('Tecle [Enter] para continuar.')                   

    elif x == '0':
        print('\nAcabou')
        break

    else:
        print('\nNão entendi!')
        input('Tecle [Enter] para continuar.') '''

       # Loop while

import os
os.system('cls')

while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")

    match x:
        case '0':
            print('\nAcabou')

            # Esse break interrompe o 'while'
            break

        case '1':
            print('\nVai comer')
            

        case '2':
            print('\nBeba água')
            

        case '3':
            print('\nGrite: MAMÃE!!!')
                          

        # Nenhuma das opções acima é válida
        case _:
            print('\nNão entendi!')

    input('Tecle [Enter] para continuar.')                