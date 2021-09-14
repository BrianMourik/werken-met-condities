#this is going to be tedious isnt it

haar = 0
ervaring = 0
rijbewijs = 0
stylish = 0
lengte = 0
zwaarte = 0
overleven = 0
diploma = 0

sex = input("Bent u een man of een vrouw?: ")
if (sex.lower() == "man"):
    haar1 = input("Heeft u een snor?: ")
    if (haar1.lower() == "ja"):
        haar2 = int(input("Hoe breed is uw snor in cm?: "))
        if (haar2 >= 10):
            haar = 1

else:
    haar1 = input("Krult uw haar?: ")
    if (haar1.lower() == "ja"):
        kleur = input("Welke kleur is uw haar?: ")
        if (kleur.lower() == "rood"):
            haar2 = int(input("Hoe lang is uw haar in cm?: "))
            if (haar2 >= 20):
                haar = 1

ervaring1 = int(input("Hoeveel jaar ervaring met dieren-dressuur?: "))
if (ervaring1 >= 4):
    ervaring = 1

shit = input("Leeft u nog?: ")

rijbewijs1 = input("Wat voor rijbewijs heeft u?: ")
if (rijbewijs1.lower() == "vrachtwagen" ):
    rijbewijs = 1

shit = input("Heeft u ooit een bril laten vallen?: ")

stylish1 = input("Wat voor hoed draagt u vaak?: ")
if (stylish1.lower() == "hoge hoed"):
    stylish = 1

lengte1 = int(input("Hoe lang bent u in cm?: "))
if (lengte1 >= 150):
    lengte = 1

shit = input("Waarom doet u deze test?: ")

shit = input("Wat is het antwoord van het leven en alles?: ")

zwaarte1 = int(input("Hoeveel weegt u in kg?: "))
if (zwaarte1 >= 90):
    zwaarte = 1

overleven1 = input("Heeft u enige speciaale certificaten?: ")
if (overleven1.lower() == "overleven met gevaarlijk personeel"):
    overleven = 1

diploma1 = input("Heeft u een mbo opleiding gevolgd?: ")
if (diploma1.lower() == "ja"):
    mbo = input("Wat voor mbo opleiding?: ")
    if (mbo.lower() == "ondernemen"):
        diploma = 1

uitkomst = int((((haar+ervaring)+(rijbewijs+stylish))+((lengte+zwaarte)+(overleven+diploma))))

if (uitkomst == 8):
    print("U BENT AANGENOMEN!")
    
else:
    print("U voldoet niet aan alle criteria.")