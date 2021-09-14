#ew kaas

geel = input("Is de kaas geel?:")
if (geel.lower() == "ja"):
    gaten = input("Zitten er gaten in?:")

    if (gaten.lower() == "ja"):
        duur = input("Is de kaas belachelijk duur?: ")
        
        if (duur.lower() == "ja"):
            print("Emmenthaler")
        else:
            print("Leerdammer")
    
    else:
        steen = input("Is de kaas hard als steen?: ")

        if (steen.lower() == "ja"):
            print("Pamigiano Reggiano")
        else:
            print("Goudse kaas")

else:
    blauw = input("Heeft de kaas blauwe schimmel?: ")

    if (blauw.lower() == "ja"):
        korstja = input("Heeft de kaas een korst?: ")

        if (korstja.lower() == "ja"):
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")

    else:
        korstnee = input("Heeft de kaas een korst?:")

    
        if (korstnee.lower() == "ja"):
            print("Camembert")
        else:
            print("Mozzarella")

