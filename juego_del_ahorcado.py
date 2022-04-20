import random


def read():
    list_of_words = []
    
    # lectura archivo
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line)
    # seleccion de una palabra
    word_choice = random.choice(list_of_words)
    print(word_choice)  # comentar esta linea al final
    return word_choice

    

def main():
    new_word = []
    print("""  
************************* JUEGO DEL AHORCADO *************************
            
            Para salir del programa presiona la letra x

**********************************************************************""")

    try:
        word_choice = read()
        word_long = len(word_choice)
    
        # imprime __ segun longitud de la palabra
        print(len(word_choice)*"__ ")
        
        #word_choice = list(word_choice)
        #print(word_choice)

        status = 1
        while status != 0:

            chosen_letter = input("\n Adivina la palabra. Ingresa una letra: ")

            if chosen_letter == "x":
                status = 0
            else:
                for i, x in enumerate(word_choice):
                    if x == chosen_letter:
                        new_word[i] = chosen_letter


                print(len(word_choice)*"__ ")
            
            #new_word.pop()
            
            print(new_word)
    except ValueError:
        print("Debes ingresar una letra y nada más!")


if __name__ == '__main__':

    main()
