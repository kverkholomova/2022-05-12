"""Zadanie 2.
W pliku dane.txt znajduje się 200 wierszy. Każdy wiersz zawiera 320 liczb naturalnych z przedziału
od 0 do 255, oddzielonych znakami pojedynczego odstępu (spacjami). Przedstawiają one jasności kolejnych pikseli czarno-białego obrazu o wymiarach 320 x 200 pikseli (0 – czarny, 255 – biały). Napisz
program, który:
1. Podaje jasność najjaśniejszego i najciemniejszego piksela.
2. Podaje, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś
symetrii. Obraz ma pionową oś symetrii, jeśli w każdym wierszu 𝑖 − 𝑡𝑦 piksel od lewej strony przyjmuje tę samą wartość, co 𝑖 − 𝑡𝑦 piksel od prawej strony, dla dowolnego 1 ≤ 𝑖 ≤ 320.
3. Podaje liczbę wszystkich pikseli kontrastujących. Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się więcej niż 128, zaś sąsiednimi nazywamy takie piksele, które leżą
obok siebie w tym samym wierszu lub w tej samej kolumnie.
4. Zapisuje wyniki z punktów od 1 do 3 w pliku dane_wyniki.txt.
"""

dane_matrix = []
dane = open("dane.txt", "r")
wyniki = open("dane_wyniki.txt", "w")
for k in dane:
    dane_row_str = k.split()
    dane_row_int = list(map(int, dane_row_str))
    dane_matrix.append(dane_row_int)
    # print(len(dane_row_int))
    # print(dane_matrix)
    # print("Column")

# print(dane_matrix)

minimum = dane_matrix[0][0]
maximum = dane_matrix[0][0]
for row in dane_matrix:
    for element in row:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element


wyniki.write("Minimum pixel is:")
wyniki.write(str(minimum))
wyniki.write("\n")
wyniki.write("Maximum pixel is:")
wyniki.write(str(maximum))
print(minimum)
print(maximum)

wyniki.write("\n")



dane_matrix = []
dane = open("dane.txt", "r")
for k in dane:
    dane_row_str = k.split()
    dane_row_int = list(map(int, dane_row_str))
    dane_matrix.append(dane_row_int)

# print(dane_matrix)


def is_row_symmetric(row: list[int]) -> bool:
    return row == row[::-1]


not_symmetric_count = 0
for row in dane_matrix:
    if not is_row_symmetric(row):
        not_symmetric_count += 1


for row in dane_matrix:
    if is_row_symmetric(row):
        r = ' '.join(str(x) for x in row)
        wyniki.write(r)
        wyniki.write('\n')
print(not_symmetric_count)


def is_contrast(a: int, b: int) -> bool:
    return abs(a - b) > 128


def has_contrast_neighbour(matrix: list[list[int]], i: int, j: int) -> bool:
    # indexes are [0..199][0..319]
    result = False
    if 0 <= i-1 <= 199:
        result |= is_contrast(matrix[i][j], matrix[i-1][j])
    if 0 <= i+1 <= 199:
        result |= is_contrast(matrix[i][j], matrix[i+1][j])

    if 0 <= j-1 <= 319:
        result |= is_contrast(matrix[i][j], matrix[i][j-1])
    if 0 <= j+1 <= 319:
        result |= is_contrast(matrix[i][j], matrix[i][j+1])

    return result


contrast_count = 0
for i in range(0, 200):
    for j in range(0, 320):
        if has_contrast_neighbour(dane_matrix, i, j):
            contrast_count += 1
            # print(dane_matrix[i][j])

wyniki.write("The number of contrast pixels is: ")
wyniki.write(str(contrast_count))
wyniki.write("\n")
print(contrast_count)

input()

