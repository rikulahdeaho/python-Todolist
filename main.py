tasks = []
suoritetut_tehtavat = set()
# Tämän avulla voidaan lisätä tehtäviä.
def lisaa_tehtava():
    while True:
        tehtava = input("Syötä tehtävä (lopeta lopettaaksesi): ")
        if tehtava == "lopeta":
            break
        tasks.append(tehtava)
        print("Tehtävä lisätty!")
        print("Nykyiset tehtävät:")
        nayta_tehtavat(suoritetut_tehtavat)
        suoritetaanko = input("Merkitäänkö tehtävä suoritetuksi (kyllä/ei)? ")
        if suoritetaanko == "kyllä":
            suoritetut_tehtavat.add(len(tasks))
            print("Tehtävä merkitty suoritetuksi!")

# Tämän avulla voidaan näyttää tehtäväviä.
def nayta_tehtavat(suoritetut_tehtavat):
    if not tasks:
        print("Ei tehtäviä.")
    else:
        print("Tässä on lista tehtävistäsi:")
        for i, tehtava in enumerate(tasks):
            if i+1 in suoritetut_tehtavat:
                yliviivattu_tehtava = "\u0336" + tehtava
                print(f"{i+1}. {yliviivattu_tehtava}")
            else:
                print(f"{i+1}. {tehtava}")

# Tämän avulla voidaan muokata tehtäviä.
def muokkaa_tehtavaa():
    nayta_tehtavat()
    indeksi = int(input("Syötä muokattavan tehtävän indeksi: ")) - 1
    if indeksi >= 0 and indeksi < len(tasks):
        uusi_tehtava = input("Syötä uusi tehtävä: ")
        tasks[indeksi] = uusi_tehtava
        print("Tehtävä muokattu!")
    else:
        print("Virheellinen indeksi!")

# Tämän avulla voidaan poistaa tehtävät. 
def poista_tehtava():
    nayta_tehtavat()
    indeksi = int(input("Syötä poistettavan tehtävän indeksi: ")) - 1
    if indeksi >= 0 and indeksi < len(tasks):
        poistettu_tehtava = tasks.pop(indeksi)
        print(f"Tehtävä '{poistettu_tehtava}' poistettu!")
    else:
        print("Virheellinen indeksi!")

# Tämän suorittaa to-do listan. 
def suorita_to_do_lista():
    while True:
        valinta = input("Valitse toiminto (lisää/näytä/muokkaa/poista/lopeta): ")
        if valinta == "lisää":
            lisaa_tehtava()
        elif valinta == "näytä":
            nayta_tehtavat()
        elif valinta == "muokkaa":
            muokkaa_tehtavaa()
        elif valinta == "poista":
            poista_tehtava()
        elif valinta == "lopeta":
            break
        else:
            print("Virheellinen valinta!")

# Suoritetaan to-do-listan päälooppi
suorita_to_do_lista()
