def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: deljenje z 0 ni dovoljeno!"
    return a / b

# Seznam za zgodovino zadnjih 3 izračunov
zgodovina = []

print("Pozdrav! Mini kalkulator")
print("1 = seštevanje")
print("2 = odštevanje")
print("3 = množenje")
print("4 = deljenje")
print("0 = izhod")

izbira = input("Kaj želiš narediti? (0,1,2,3 ali 4): ")

rezultat = None

if izbira == "1":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = sestej(x, y)
    print(f"{x} + {y} = {rezultat:.2f}")

elif izbira == "2":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = odstej(x, y)
    print(f"{x} - {y} = {rezultat:.2f}")

elif izbira == "3":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = pomnozi(x, y)
    print(f"{x} * {y} = {rezultat:.2f}")

elif izbira == "4":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    rezultat = deli(x, y)
    if isinstance(rezultat, str):
        print(rezultat)
    else:
        print(f"{x} / {y} = {rezultat:.2f}")

elif izbira == "0":
    print("Program se zapira. Nasvidenje!")
else:
    print("Neveljavna izbira!")

# Dodamo izračun v zgodovino, če je veljaven
if rezultat is not None and not isinstance(rezultat, str):
    zgodovina.append(f"{izbira}: {x} ? {y} = {rezultat:.2f}")
    # ohranimo samo zadnje 3 izračune
    if len(zgodovina) > 3:
        zgodovina.pop(0)

# Izpišemo zgodovino
if zgodovina:
    print("\nZgodovina zadnjih izračunov:")
    for item in zgodovina:
        print(item)
