zajecia = ["bazy danych", "programowanie",  "mikroekomnomia"]
print(zajecia) #wyświetlenie całej listy

print(zajecia[0]) #indeksy zaczynaja sie od 0; wyswietlenie pierwszego elementu
print(zajecia[0].title()) #indeksy zaczynaja sie od 0; wyswietlenie pierwszego elementu z wielka pierwsza lit

print(f"Nie mogę się doczekać nauki na egzamin z przedmiotu {zajecia[2]}")

print(zajecia[2])
print(zajecia[-1]) #wyświetlanie pierwszego od konca elementu

zajecia[0]='cyberbezpieczenstwo'
print(zajecia)

zajecia.append('makroekonomia') #dodawanie na koniec listy
print(zajecia)

zajecia.insert(1,'bazy danych') #dodanie elementu na konkretne miejsce
print(zajecia)

##USUWANIE Z LISTY
del zajecia[-1] #usuwanie z listy po indeksie
print(zajecia)

print(f"Zaliczono na 5 przedmiot: {zajecia.pop(-1).title()}") #usuwanie popem usuwa element ale nam go wyświetla przy usuwaniu
print(zajecia)

zajecia.insert(0, 'programowanie')
zajecia.remove('programowanie') #usuwanie elementu po nazwie ALE pierwszego wystapienia tego
print(zajecia)

##SORTOWANIE LISTY
print(sorted(zajecia))   #sortowanie w printoowaniu
print(zajecia)

zajecia.sort()  #sortowanie na stałe
print(zajecia)

zajecia.sort(reverse=True) #odwrotnie niz alfanbetycznie
print(zajecia)

zajecia.reverse()   #zamiana miejscami (odwrotnosc listy)- trwala metoda
print(zajecia)

print(len(zajecia)) #ile elementow w liscie

for przedmiot in zajecia:
    print("Lubię przedmiot "+przedmiot.title())