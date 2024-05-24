import random
def gissningsspel():
    slumpat_nummer = random.randint(1, 100)
    gissningar = 0

    while True:
        gissning = int(input("Gissa ett nummer (mellan 1 och 100): "))
        gissningar += 1

        if gissning < slumpat_nummer:
            print("För lågt. Gissa högre.")
        elif gissning > slumpat_nummer:
            print("För högt. Gissa lägre.")
        else:
            print(f"Grattis! Du gissade rätt, det var {slumpat_nummer}. Det tog dig {gissningar} gissningar.")
            break

if __name__ == "__main__":
    gissningsspel()
