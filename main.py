# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def Addizione(num1, num2):
    return num1 + num2

def Moltiplicazione(num1, num2):
    return num1 * num2

def Sottrazione(num1, num2):
    if num1 > num2 :
        return num1 - num2
    else : return num2 - num1

def Divisione(num1, num2):
    if num1 > num2:
        return num1 / num2
    else : return num2 / num1

if __name__ == '__main__':
    print("###########################################")
    print("################ CALCULATOR ###############")
    print("###########################################")
    print("###   1   ###   2   ###   3   ###   +   ###")
    print("###   4   ###   5   ###   6   ###   -   ###")
    print("###   7   ###   8   ###   9   ###   *   ###")
    print("###  DEL  ###   0   ###   =   ###   /   ###")
    print("###########################################")
    print("Menu : \n1 Addizione\n2 Sottrazione\n3 Moltiplicazione\n4 Divisione\n5 Uscita\n")
    num1 = int(input('Dammi numero 1 : '))
    num2 = int(input('Dammi numero 2 : '))
    scelta = int(input('Dammi scelta tra 1 e 5 : '))
    if scelta == 1:
         print('Hai scelto : Addizione.')
         ris = Addizione(num1, num2)
         print(f'Risultato Addizione : {ris}')
    elif scelta == 2:
         print('Hai scelto : Sottrazione.')
         ris2 = Sottrazione(num1, num2)
         print(f'Risultato Sottrazione : {ris2}')
    elif scelta == 3:
         print('Hai scelto : Moltiplicazione.')
         prod = Moltiplicazione(num1, num2)
         print(f'Risultato Moltiplicazione : {prod}')
    elif scelta == 4:
         print('Hai scelto : Divisione.')
         div = Divisione(num1, num2)
         print(f'Risultato Divisione : {div}')
    else : print('Uscita')