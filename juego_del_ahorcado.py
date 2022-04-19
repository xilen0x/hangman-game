import random


def read():
    list_of_words = []
    new_word = []
    
    # lectura archivo
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line)
    # seleccion de una palabra
    word_choice = random.choice(list_of_words)
    print(word_choice)  # comentar esta linea al final
    word_long = len(word_choice)
    spaces = []
    # imprime __ segun longitud de la palabra
    for e in range(1, word_long):
        spaces.append("__")
    print(spaces)
    
    status = 1
    while status != 0:

        chosen_letter = input("\n Adivina la palabra. Ingresa una letra: ")

        if chosen_letter == "x":
            status = 0
        else:
            for i in word_choice:
                if i == chosen_letter:
                    new_word.append(chosen_letter)

                else:
                    new_word.append("__")
        
        new_word.pop()
        
        print("\n", new_word, "\n")





#def contains_letter(word_choice):
    

def main():
    print("""  
************************* JUEGO DEL AHORCADO *************************
            
            Para salir del programa presiona x

**********************************************************************
            """)
    read()


''' if chosen_letter in word_choice:
    print("Sí está")
else:
    print("No está") '''


if __name__ == '__main__':

    main()
