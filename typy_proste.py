### komentarze


#łąńcuchy znaków i ich łączenie
my_name = "kamila"
my_another_name = my_name
print("my_name id:" + str(id(my_name))) #id zmiennej przed zmiana

my_name='bartosz'
print("my_name id:" + str(id(my_name))) #id zmiennej po zmianie
print("my_another_name id:" + str(id(my_another_name)))

print(f"Witaj {my_name}")

#modyfikacje łańcuchów znaków
print(my_name)
print(my_another_name)
print(my_name.title())
print(my_another_name.title())
print(my_another_name.upper())
print(my_name.lower())

#białe znaki
login = "    kamila123 "
print(f'"{login}"')
print(f'"{login.strip()}"')
print(f'"{login.rstrip()}"')
print(f'"{login.lstrip()}"')

#są to metody tymczasowe, czyli działają tylko w momencie wywołania; nie zmienia zmiennej login, tylko wydruk
#trwale:

login = login.upper()
print(login)

#usuwanie prefiksów i sufiksów

uep_website = "https://ue.poznan.pl"
print(uep_website)
print(uep_website.removeprefix("https://").removeprefix("http://"))    #jeśli przedrostka nie bedzie to nic sie nie stanie
print(uep_website
      .strip()
      .lower()
      .removeprefix("https://")
      .removeprefix("http://")
      .removesuffix("/"))    #usuwamy biale znaki a następnie prefiksy

# LICZBY
#można operować interaktywnie w konsoli na dole
#potęgowanie **4

universe_age = 14_000_000_000_000_000_001
print(universe_age)

x = 0
y = 2
z = 1
#albo:
x, y, z = 0, 2, 1

#zmienne ktore nie ulegają zmianie
MAX_CONNECTIONS = 1000
PORT = 8000