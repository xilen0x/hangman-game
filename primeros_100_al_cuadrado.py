#EJERCICIOS
#1 cuadrado de los primeros 100 n°s 
''' def square_100_firts():
    squares = []

    for e in range(1, 101):
        squares.append(e**2)
    print(squares)


square_100_firts() '''
    

#2 cuadrado de los n° que no sean divisibles por 3
''' def square_non_div3():
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)
    

square_non_div3()  '''

#3 crear (con list comprehension) una lista de los n° múltiplos de 4,6, y 9 hasta 5 dígitos.
''' squares = [i for i in range(1, 100000) if i % 36 ==0]
print(squares) '''

#4 diccionario cuya clave son los primeros 100 n°s y su valor su cubo
''' def dict_100():
    dict = {}

    for e in range(1, 101):
        dict[e] = e**3
    print(dict)

dict_100() '''

# 5 diccionario cuya clave son los primeros 100 n°s y su valor su cubo y que ademas no sean divisibles por 3
''' def dict_100():
    dict = {}

    for e in range(1, 101):
        if e % 3 != 0:
            dict[e] = e**3
    print(dict)

dict_100() '''

# 6 Crear diccionario (con dict. comprehension) cuya clave son los primeros 100 n°s y su valor su cubo y que ademas no sean divisibles por 3
''' my_dict = {i:i**3 for i in range(1, 101) if i % 3 != 0}
print(my_dict) '''

# 7 Crear con dict. comprehension, un diccionario cuyas llaves sean los primeros 1000 numeros naturales con sus raices cuadradas como valores.
my_dict = {i:round(i**0.5) for i in range(1, 1001) }
print(my_dict)