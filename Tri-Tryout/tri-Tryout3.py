# Tri-Tryout 3

def Naam():
    naam = input('Wat is je naam? ').lower()
    nieuwNaam = naam[0].upper()
    for i in range(1, len(naam)):
        nieuwNaam += naam[i]
    return nieuwNaam

def Leeftijd():
    leeftijd = input('Hoe oud ben je? ').lower()
    if leeftijd != 'stop':
        int(leeftijd)
    return leeftijd

def program():
    repeat = True
    while repeat:
        naam = Naam()
        if naam == 'Stop':
            print('Het programma is gestopt.')
            repeat = False
            break
        leeftijd = Leeftijd()
        if leeftijd == 'stop':
            print('Het programma is gestopt.')
            repeat = False
            break
        print(f'Hallo {naam}, je leeftijd is {leeftijd}.')

program()