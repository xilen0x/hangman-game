def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


''' def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo") '''


def run():
    while True:
        num = input('Ingresa un número: ')
        assert num.isnumeric() and int(num) > 0, "Debes ingresar solo un entero positivo"

        print(divisors(int(num)))
        break

if __name__ == '__main__':
    run()
