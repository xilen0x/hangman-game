import random
import os
import unidecode

def read():
    list_of_words = []
    
    # lectura archivo
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line.strip('\n'))
    # select of a word
    word_choice = random.choice(list_of_words).upper()
    #eliminate accents
    word_choice = unidecode.unidecode(word_choice)
    #print(word_choice)  # comentar esta linea al final
    return word_choice

    
def hangman(lives):
    #word = read()
    if lives == 6:
        print("""
             |   |
             O   |
            /|\  |
            / \  |
                 |
                """)
    elif lives == 5:
        print("""
             |   |
             O   |
            /|\  |
              \  |
                 |
                """)
    elif lives == 4:
        print("""
             |   |
             O   |
            /|\  |
                 |
                 |
                """)
    elif lives == 3:
        print("""
             |   |
             O   |
            /|   |
                 |
                 |
                """)
    elif lives == 2:
        print("""
             |   |
             O   |
             |   |
                 |
                 |
                """)
    elif lives == 1:
        print("""
             |   |
             O   |
                 |
                 |
                 |
                """)
    elif lives == 0:
        print("""
             |   |
                 |
                 |
                 |
                 |
                """)
    return lives

def main():

    print("""  
    ************************* JUEGO DEL AHORCADO *************************
                                    |   |
                                    O   |
                                   /|\  |
                                   / \  |
                                        |


                   Para salir del programa escribe: exit

    **********************************************************************\n""")

    try:
        word_original = read()
    
        word = list(word_original)
        #print(word)
        p2 = ' __ ' * len(word)
        p2 = p2.split()
        print(p2)
        lives = 6

        while word != p2:

            letter = input("\n Ingrese una letra: ").upper()
            os.system("clear")

            if letter == 'EXIT':
                break
            elif letter in word and letter not in p2:
                locations = [i for i, x in enumerate(word) if x == letter ]
                #print("locations: ",locations)
                for location in locations:
                    p2[location] = letter
                print(p2)
                hangman(lives)
                print("Te restan {} vidas".format(lives))

            else:
                lives -= 1
                print(p2)
                hangman(lives)
                print("Te restan {} vidas".format(lives))
                if lives == 0:
                    break
                    
        if letter == 'exit':
            print("Bye!")
        else:
            print('\nGAME OVER, HAS PERDIDO!\n' if lives == 0 else '\FELICITACIONES, GANASTE EL JUEGO!!!\n')
            print("La palabra era {} \n".format(word_original))

    except ValueError:
        print("You must enter just a letter!")


if __name__ == '__main__':

    main()
