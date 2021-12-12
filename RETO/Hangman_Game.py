# Import libraries
import random
import os
import time
from Recursos import init, images, win, lost


# Read the file: It's necessary that the words don't have symbols and show in a list
with open("./Archivos/data.txt", "r", encoding="utf-8") as file:
    data = [(line.translate(line.maketrans('áéíóú', 'aeiou')).replace('\n', ''))
            for line in file]
time.sleep(2)


def cortos():
    time.sleep(1)
    os.system("clear")


def run():

    # numbers of incorrects
    incorrec = 0

    print(init)

    # Numbers of lifes
    vidas = 3

    # choisen word
    word = random.choice(data)
    print(images[incorrec], "\n"*2, " _"*len(word))

    guessed_letters = list()

    while True:
        while True:
            letter = input("Ingresa una letra: ").lower()
            try:
                if str.isdigit(letter) == True:
                    raise ValueError("Debe ingresar una letra")
                elif len(letter) == 0:
                    raise ValueError("Debe ingresar una letra")
                elif len(letter) > 1:
                    raise ValueError("Debe ingresar solo una letra")
            except ValueError as ve:
                print(ve)
                break

            if letter in guessed_letters:
                print("Ya habías intentado con esa letra")
                os.system("clear")
            else:
                guessed_letters.append(letter)
                if letter in word:
                    print("Adivinaste una letra")
                    cortos()
                    break
                else:
                    vidas = vidas - 1
                    incorrec = incorrec+1
                    print('Te equivocaste, intentalo nuevamente',
                          '\n', 'Te quedan ', vidas, ' vidas')
                    cortos()
                    break

        if vidas == 0:
            print(init, "\n", images[incorrec], "\n", lost)
            print(f'''
    Palabras acertadas: {len(guessed_letters)}
    La palabra era: {word}
    ¿Desea jugar otra vez? si/no
            ''')
            print('¿Quiere jugar de nuevo? (sí o no)')
            desc = input()
            if "s" in desc:
                os.system("clear")
                run()
            else:
                break

        estatus = ""
        missing_letters = 0

        for x in word:
            if x in guessed_letters:
                estatus = estatus+x
            else:
                estatus = estatus+' _'
                missing_letters = missing_letters+1

        print(init)
        print(images[incorrec])
        print(estatus)

        if missing_letters == 0:
            print(init, "\n", images[incorrec], "\n", win)
            print(f'''
    Palabras acertadas: {len(guessed_letters)}
    La palabra era: {word}
    ¿Desea jugar otra vez? si/no
            ''')
            print('¿Quiere jugar de nuevo? (sí o no)')
            desc = input()
            if "s" in desc:
                os.system("clear")
                run()
            else:
                break


if __name__ == "__main__":
    run()

    # for i, let in enumerate(word):
    #     conjunto = dict()
    #     conjunto[i] = let
    #     if letter == let:
    #         print("si existe")
