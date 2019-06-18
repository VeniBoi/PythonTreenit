import random

while True:
    print("Miltä väliltä haluat arvata numeron?")
    numero1 = input("Anna ensimmäinen numero: ")
    numero2 = input("Anna toinen numero: ")

    randomNumero = random.randrange(int(numero1), int(numero2) + 1)

    print("Kone on arponut numeron")
    vastaus = int(input("Minkä numeron kone on arponut? Vastauksesi: "))

    if randomNumero == vastaus:
        print("Oikein!")
    else:
        print("Väärin! HA!")
        print("Oikea vastaus oli: " + str(randomNumero))
    jatketaanko = input("Aloitetaanko alusta? K/E: ")

    if jatketaanko == "E":
        break
