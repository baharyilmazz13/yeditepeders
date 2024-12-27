password = 1234  # Richtig Passwort

while True:
    user_input = int(input("Geben Sie Ihr Passwort ein: "))  # Passwort vom Benutzer abfragen
    
    if user_input == password:  # Wenn das Passwort richtig ist
        print("Ja richtig ! Was möchten Sie tun?")
        break  # Beenden Sie die Schleife
    else:  # Wenn das Passwort falsch ist
        print("Falsches Passwort. Versuchen Sie es noch einmal.")
password = 1234  # Rightig passwort

while True:
    user_input = int(input("Geben Sie Ihr Passwort ein: : "))  # Passwort vom Benutzer abfragen
    
    if user_input == password:  # Wenn das Passwort richtig ist
        print("Ja richtig ! Was möchten Sie tun?")
        break  # Beenden Sie die Schleife
    else:  # Wenn das Passwort falsch ist
        print("Falsches Passwort. Versuchen Sie es noch einmal.")
konto = 1000  # Konto am Anfang

while True:
    menu = int(input("1: Einzahlung, 2: Auszahlung:"))  # Auswahl der Prozesse

    if menu == 1:  # Einlagengeschäft
        geld = int(input("Wie viel wollen Sie einzahlen?:"))
        if geld > 0:
            konto += geld
            print("Ihr neues Konto:"+ str(konto))
        else:
            print("Bitte geben Sie einen gültigen Betrag ein.")
    
    elif menu == 2:  # Abhebung von Geld
        geld = int(input("Wie viel wollen Sie einnehmen?:"))
        if 0 < geld <= konto:
            konto -= geld
            print("Ihr neues Konto:"+ str(konto))
        else:
            print("Bitte geben Sie einen gültigen Betrag ein.")
    
    else:  # Ungültige Transaktion
        print("Ungültige Transaktion. Bitte wählen Sie 1 oder 2:")

    print("Vergessen Sie nicht, Ihre Karte mitzunehmen!")
    break  # Beenden Sie die Schleife
     