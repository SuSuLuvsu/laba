from random import randint


def proc1():
    slova = []
    while (one_word := str(input())) !="stop":
        slova.append(one_word)

    print(" ".join(slova))
proc1()


k = 0
def proc2():
 word = input("введите слово:")
 for i in range(len(word)):
    if word[i]=="Ф" or word[i]=="ф":
        print("Ого! Это редкое слово")
        break
    else:
        print("Эч , это не очень редкое слово")
        break
proc2()

def proc4():
    k = 0
    print("Для завершения игры введите stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        if res == "stop":
            break
        res = int(res)
        if a+b == res:
            print("Правильно!")
        else:
            print("Ответ неправильный :(")
            k += 1
        if k == 3:
           print('игра окончена')
           break
proc4()



