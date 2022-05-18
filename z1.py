"""Zadanie 1.
Liczbami półpierwszymi nazywamy liczby naturalne, które są iloczynem dwóch liczb pierwszych.
Przykładowo liczbami taki są: 34, bo 34 = 2 ∙ 17, a także 699 = 2 ∙ 17, 841 = 29 ∙ 29 itd.
W pliku liczby.txt znajduje się 500 liczb naturalnych, z których każda ma co najwyżej 6 cyfr.
Napisz program, który wyodrębni wszystkie liczby półpierwsze z pliku liczby.txt.
Program powinien zapisać wyodrębnione liczby do pliku liczby_wynik.txt.
"""


liczby_wynik = open("liczby.txt", "r")


def prime_number(num: int) -> bool:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


def semiprime_number(num: int) -> int:
    result_count = 0
    mult = 1
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if prime_number(i) and i != 1:
                result_count += 1
                mult = mult * i
                print(num, i)
    if result_count == 2 and mult == num:
        result = num
    else:
        result = 0
    return result


print(semiprime_number(937))
wyniki = open("wyniki_c1.txt", "w")
for k in liczby_wynik:
    if semiprime_number(int(k.rstrip())) != 0:
        wyniki.write(k)

input()
