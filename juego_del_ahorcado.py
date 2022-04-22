import random
import os

def read():
    list_of_words = []
    
    # lectura archivo
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line.strip('\n'))
    # seleccion de una palabra
    word_choice = random.choice(list_of_words).upper()
    print(word_choice)  # comentar esta linea al final
    return word_choice

    

def main():

    print("""  
    ************************* JUEGO DEL AHORCADO *************************
            Para comenzar presiona: enter
            Para salir del programa escribe: exit

    **********************************************************************""")

    try:
        word = read()
    
        word = list(word)
        print(word)
        p2 = ' __ ' * len(word)
        p2 = p2.split()
        print(p2)
        lives = len(word)
        print("lives: ", lives)

        while word != p2:

            letter = input("enter a letter: ").upper()
            os.system("clear")

            if letter == 'exit':
                break
            elif letter in word and letter not in p2:
                locations = [i for i, x in enumerate(word) if x == letter ]
                #print("locations: ",locations)
                for location in locations:
                    p2[location] = letter
                print(p2)
            else:
                lives -= 1
                print("You have {} lives left".format(lives))
                if lives == 0:
                    break
                    
        if letter == 'exit':
            print("Bye!")
        else:
            print('You LOST' if lives == 0 else 'You WON')

    except ValueError:
        print("Debes ingresar una letra y nada más!")


if __name__ == '__main__':

    main()
