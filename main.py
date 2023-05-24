tasks = []

def lisaa_tehtava():
    tehtava = input("Syötä tehtävä: ")
    tasks.append(tehtava)
    print("Tehtävä lisätty!")

def nayta_tehtavat():
    print("Tässä on lista tehtävistäsi:")
    for i, tehtava in enumerate(tasks):
        print(f"{i+1}. {tehtava}")

def poista_tehtava():
    nayta_tehtavat()
    indeksi = int(input("Syötä poistettavan tehtävän indeksi: ")) - 1
    if indeksi >= 0 and indeksi < len(tasks):
        poistettu_tehtava = tasks.pop(indeksi)
        print(f"Tehtävä '{poistettu_tehtava}' poistettu!")
    else:
        print("Virheellinen indeksi!")

def suorita_to_do_lista():
    while True:
        valinta = input("Valitse toiminto (lisää/näytä/poista/lopeta): ")
        if valinta == "lisää":
            lisaa_tehtava()
        elif valinta == "näytä":
            nayta_tehtavat()
        elif valinta == "poista":
            poista_tehtava()
        elif valinta == "lopeta":
            break
        else:
            print("Virheellinen valinta!")

# Suoritetaan to-do-listan päälooppi
suorita_to_do_lista()

