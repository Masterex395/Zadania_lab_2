# # Zad 1
# lista= ["Pływanie", "Tenis stołowy", "Piłka nożna"]
# lista.reverse()
# lista.append("Bieganie")
# print(lista)

# # Zad 2
# slownik = {"pt.": "pod tytułem", "np": "na przykład", "r.": "rok"}
# print(slownik.keys())
# print(slownik.values())

# # Zad 3
# gry= {"GAME 1": "Counter-Strike:Global Offensive", "GAME 2": "Forza Horizon 4",
#        "GAME 3": "World of Tanks", "GAME 4": "Battlefield 3"}
# print(len(gry))

# # Zad 4
# zdanie = input("Podaj dowolne zdanie: ")
# ile_a = 0
# for a in zdanie:
#     if a == "a":
#         ile_a += 1
# print(ile_a)

# # Zad 5
# import sys as system
# system.stdout.write("Podaj 1 liczbę: ")
# a = system.stdin.readline()
# system.stdout.write("Podaj 2 liczbę: ")
# b = system.stdin.readline()
# system.stdout.write("Podaj 3 liczbę: ")
# c = system.stdin.readline()
# a = int(a)
# b = int(b)
# c = int(c)
# wynik = a ** b + c
# system.stdout.write(str(wynik))

# # Zad 6
# print("Podaj 1 liczbę: ")
# a = input()
# print("Podaj 2 liczbę: ")
# b = input()
# print("Podaj 3 liczbę: ")
# c = input()
# if a>b:
#     if c>a:
#         print("3 podana liczba jest największa")
#     else:
#         print("1 podana liczba jest największa")
# elif b>a:
#     if c>b:
#         print("3 podana liczba jest największa")
#     else:
#         print("2 podana liczba jest największa")
# else:
#     if a == c:
#         print("Podane liczby są równe")
#     else:
#         print("3 podana liczba jest największa")

# # Zad 7
# liczby = [2, 4, 5, 3.14, 7.58, 396.99]
# for kwadrat in liczby:
#     print(kwadrat ** 2)

# # Zad 8
# i = 0
# lista = []
# while i < 10:
#     print("Podaj liczbe: ")
#     a = input()
#     parzysta = int(a)%2
#     if parzysta == 0:
#         lista.append(a)
#     i += 1
# print(lista)

# # Zad 9
# lista = [1, 2, 3, 4, 5]
# for liczba in lista:
#     a = int(liczba)%2
#     if a == 0:
#         print("E")
#     else:
#         print("EEEEEE")

# # Zad 10
# import math
# print("Jaka liczbę chcesz spierwiastkowac?")
# a = int(input())
# try:
#     a = (math.sqrt(a))
#     print(a)
# except:
#     print("Nie można pierwiastkowac liczb ujemnych")