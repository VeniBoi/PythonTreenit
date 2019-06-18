import random
import time

while True:
    lottorivienMaara = int(input("Kuinka monta lottoriviä haluat luoda? Määrä: "))
    lottorivit = []
    voittorivi = []
    osumat = []
    voitto = 0

    # Tehdään niin monta riviä kuin käyttäjä haluaa
    for x in range(lottorivienMaara):
        rivi = []
        kaytetytNumerot = []

        # Jokaiselle riville arvotaan 7 numeroa
        # ja tarkistetaan ettei yksi numero tule kuin kerran
        for y in range(7):
            i = random.randrange(1, 41)
            while i in kaytetytNumerot:
                i = random.randrange(1, 41)
            kaytetytNumerot.append(i)
            rivi.append(i)
        lottorivit.append(rivi)

    # Kerrotaan oma lottorivi
    print("Omat lottorivisi ovat:")
    print(*lottorivit, sep='\n')

    time.sleep(2)

    print("Seuraavaksi luodaan voittorivi...")
    time.sleep(1)
    print("Voittorivi on:")
    time.sleep(1)

    #Luodaan voittorivi
    kNumerot = []
    for y in range(7):
        i = random.randrange(1, 41)
        while i in kNumerot:
            i = random.randrange(1, 41)
        kNumerot.append(i)
        voittorivi.append(i)

    print(voittorivi)

    #Seuraavaksi näytetään kuinka monta osumaa käyttäjällä oli,
    #sekä kuinka paljon hän on voittanut ja paljonko lottorivit maksoivat

    input("Paina enter, nähdäksesi tulokset... \n")

    tmpOsumat = 0
    #Jos voittorivissä esiintyy tarkastettava numero niin siitä lisätään merkintä
    for rivi in lottorivit:
        for numero in rivi:
            if numero in voittorivi:
                tmpOsumat = tmpOsumat + 1
        osumat.append(tmpOsumat)
        tmpOsumat = 0

    #Kerrotaan osumien määrä
    print("Osumia oli:")
    ind = 1
    for osuma in osumat:
        print("Lottorivissä #" + str(ind) + " " + str(osuma) + " kpl")
        ind = ind + 1

    time.sleep(1.5)

    #Kerrotaan paljonko pelaaja voitti
    summa = 0
    for osuma in osumat:
        if osuma == 3:
            summa = summa + 2
        elif osuma == 4:
            summa = summa + 10
        elif osuma == 5:
            summa = summa + 50
        elif osuma == 6:
            summa = summa + 50000
        elif osuma == 7:
            summa = summa + "Päävoitto, eli vaiks miljoona"
    print("\nOlet voittanut " + str(summa) + " euroa")

    time.sleep(1)

    #Kerrotaan paljonko pelaaja kulutti kuponkeihin rahaa
    print("\nKäytit lottoriveihin " + str(len(lottorivit)) + "€ rahaa")
    time.sleep(1)
    if voitto > len(lottorivit):
        print("Se kannatti, jäit voitolle!")
    else:
        print("\nOlisi ehkä kannattanut käyttää ne rahat fiksummin... Ei voittoja.")
    time.sleep(1)

    #Kysytään yritetäänkö uudestaan
    jatketaanko = input("\nKoitetaanko uudestaan?? K/E: ")

    if jatketaanko == "E":
        break





