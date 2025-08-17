ukoly = {}
pocet_keys = 0

def pridat_ukol():
    nazev_ukolu = input("Zadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")
    if nazev_ukolu != "" and  popis_ukolu != "":
        ukoly[nazev_ukolu] = popis_ukolu
        print()
        print(f"Úkol '{nazev_ukolu}' byl přidán.")
    else:
        print("Chybné údaje, zkuste to znovu.")
    return pridat_ukol


def zobrazit_ukoly():
    print("Seznam úkolů:")
    for index, (klic, hodnota) in enumerate(ukoly.items(), 1):
        print(f"{index}. {klic} - {hodnota}")
    return zobrazit_ukoly

def odstranit_ukol():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
        hlavni_menu
    else:
        while True:
            try:
                zobrazit_ukoly()
                mazany_index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
                indexy = list(ukoly.keys())
                mazeme = indexy[mazany_index - 1]
                if mazeme in ukoly:
                    print(f"Úkol '{mazeme}' byl odstraněn.")
                    del ukoly[mazeme]
                else:
                    print(f"Úkol '{mazeme}' není na seznamu.")
                    hlavni_menu()
                break
            except IndexError:
                print()
                print("Úkol není na seznamu.")
                print()
                hlavni_menu ()
                break

    return odstranit_ukol

def hlavni_menu():
    while True:
        try:
            print("Správce úkolů - hlavní menu")
            print("1. Přidat nový úkol")
            print("2. Zobrazit všechny úkoly")
            print("3. Odstranit úkol")
            print("4. Konec programu")
            vyber = int(input("Vyberte možnost (1 - 4): "))
            print()
            if vyber == 1:
                pridat_ukol()
                print()
                hlavni_menu ()
            elif vyber == 2:
                zobrazit_ukoly()
                print()
                hlavni_menu()
            elif vyber == 3:
                odstranit_ukol()
                print()
                hlavni_menu()
            elif vyber == 4:
                return print("Konec programu.")
            else:
                print()
                print("Chybná volba, vyberte znovu.")
                print()
                hlavni_menu ()
            break
        except ValueError:
            print()
            print("Chybná volba, vyberte znovu.")
            print()
            hlavni_menu ()
            break

    return hlavni_menu
    
hlavni_menu()