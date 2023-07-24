import sqlite3
from tabulate import tabulate
import settings as st
import os

os.system("cls")

try:
    # Datenbankverbindung herstellen
    connection = sqlite3.connect('bank.db')
    cursor = connection.cursor()

    # password = input("Enter Password: ")

    # cursor.execute(f"PRAGMA key = '{password}';")
    # cursor.execute("PRAGMA cipher_compatibility = 3;")

    # Tabelle "Kunden" erstellen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kunden (
    nr INTEGER PRIMARY KEY,
    name TEXT,
    saldo REAL
    )
    ''')

    # Tabelle "Transaktionen" erstellen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transaktionen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nr INTEGER,
    datum TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaktionstyp TEXT,
    betrag REAL,
    FOREIGN KEY (nr) REFERENCES kunden (nr)
    )
    ''')

    # Änderungen speichern und Verbindung schließen
    connection.commit()
    connection.close()

    def set(kunden_nr: int, betrag: int, show=False):
        try:
            # connection = sqlite3.connect('bank.db')
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Aktuelles Saldo des Kunden abrufen
            cursor.execute(
                'SELECT saldo, name FROM kunden WHERE nr = ?', (kunden_nr,))
            list = cursor.fetchone()
            altes_saldo = list[0]
            name = list[1]

            # Neues Saldo berechnen

            # Saldo des Kunden aktualisieren
            cursor.execute(
                'UPDATE kunden SET saldo = ? WHERE nr = ?', (betrag, kunden_nr))

            # Transaktion zur Tabelle "Transaktionen" hinzufügen
            if show == True:
                cursor.execute('INSERT INTO transaktionen (nr, transaktionstyp, betrag) VALUES (?, ?, ?)',
                               (kunden_nr, 'Einzahlung' if betrag > 0 else 'Auszahlung', betrag))

            print(tabulate([[kunden_nr, name, altes_saldo, betrag, st.gebühr, betrag]], headers=["Nr", "Name", "Altes Konto", "Ammount", "Gebühr", "Neues Konto"], tablefmt="grid"))

            # Änderungen speichern und Verbindung schließen
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print("Fehler beim Aktualisieren des Saldo: ", error)

    def saldo_aktualisieren(kunden_nr, betrag):
        try:

            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Aktuelles Saldo des Kunden abrufen
            cursor.execute(
                'SELECT saldo, name FROM kunden WHERE nr = ?', (kunden_nr,))
            list = cursor.fetchone()
            altes_saldo = list[0]
            name = list[1]

            # Neues Saldo berechnen
            if betrag != 0:
                neues_saldo = altes_saldo + betrag - 1
            else:
                betrag = altes_saldo - 1
                neues_saldo = 0

            # Saldo des Kunden aktualisieren
            cursor.execute(
                'UPDATE kunden SET saldo = ? WHERE nr = ?', (neues_saldo, kunden_nr))

            # Transaktion zur Tabelle "Transaktionen" hinzufügen
            cursor.execute('INSERT INTO transaktionen (nr, transaktionstyp, betrag) VALUES (?, ?, ?)',
                           (kunden_nr, 'Einzahlung' if betrag > 0 else 'Auszahlung', betrag))

            print(tabulate([[kunden_nr, name, altes_saldo, betrag, st.gebühr, neues_saldo]], headers=["Nr", "Name", "Altes Konto", "Ammount", "Gebühr", "Neues Konto"], tablefmt="grid"))

            # Änderungen speichern und Verbindung schließen
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print("Fehler beim Aktualisieren des Saldo: ", error)

    def saldo_überweisen(kaynak_kunden_nr, hedef_kunden_nr, miktar):
        try:
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Kaynak hesaptan para çekme
            cursor.execute(
                'SELECT saldo FROM kunden WHERE nr = ?', (kaynak_kunden_nr,))
            kaynak_saldo = cursor.fetchone()[0]

            yeni_kaynak_saldo = kaynak_saldo - miktar
            cursor.execute('UPDATE kunden SET saldo = ? WHERE nr = ?',
                           (yeni_kaynak_saldo, kaynak_kunden_nr))

            # Hedef hesaba para yatırma
            cursor.execute(
                'SELECT saldo FROM kunden WHERE nr = ?', (hedef_kunden_nr,))
            hedef_saldo = cursor.fetchone()[0]
            yeni_hedef_saldo = hedef_saldo + miktar
            cursor.execute('UPDATE kunden SET saldo = ? WHERE nr = ?',
                           (yeni_hedef_saldo, hedef_kunden_nr))

            # Transaktionen tablosuna kayıt ekleme
            cursor.execute('INSERT INTO transaktionen (nr, transaktionstyp, betrag) VALUES (?, ?, ?)',
                           (kaynak_kunden_nr, 'Überweisung-Ausgang', -miktar))
            cursor.execute('INSERT INTO transaktionen (nr, transaktionstyp, betrag) VALUES (?, ?, ?)',
                           (hedef_kunden_nr, 'Überweisung-Eingang', miktar))

            # Änderungen speichern und Verbindung schließen
            connection.commit()
            connection.close()

            print(tabulate([[kaynak_kunden_nr, hedef_kunden_nr, miktar]], headers=["Quel", "Ziel", "Ammount"], tablefmt="grid"))
            # print(f'Konto {kaynak_kunden_nr} -> Konto {hedef_kunden_nr}: {miktar} Euro überwiesen.')

        except sqlite3.Error as error:
            print("Fehler bei der Überweisung: ", error)

    def transaktion_informion(transaktion_id: int):
        try:
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            if transaktion_id != "":
                # Transaktionen tablosunu sorgula
                cursor.execute(
                    'SELECT * FROM transaktionen WHERE nr = ?', (transaktion_id,))
                transaktion = cursor.fetchall()

                if transaktion:
                    print(tabulate(transaktion, headers=[
                          "ID", "Numer", "Datum", "Type", "Betrag"], tablefmt="grid"))
                    # print(f"Informationen zur Transaktion ID {transaktion_id}:")
                    # print(f"Nummer: {transaktion[1]}")
                    # print(f"Datum: {transaktion[2]}")
                    # print(f"Transaktionstyp: {transaktion[3]}")
                    # print(f"Betrag: {transaktion[4]} Euro")
                else:
                    print(f"Transaktion ID {transaktion_id} nicht gefunden.")

            else:
                cursor.execute(
                    'SELECT * FROM transaktionen ORDER BY id DESC LIMIT 5')
                rows = cursor.fetchall()

                # Sonuçları yazdır
                print(tabulate(rows, headers=[
                      "ID", "Nr", "Datum", "Transaktionstyp", "Betrag"], tablefmt="grid"))

            # Verbindung schließen
            connection.close()
        except sqlite3.Error as error:
            print("Fehler bei der Abfrage der Transaktionsinformationen: ", error)

    def gehatl_anziegen(kunden_nr, hour: int):
        try:
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            ammount = hour * st.lohn
            ammounts = hour * st.lohnS

            # Veritabanını sorgula
            cursor.execute(
                'SELECT saldo,name FROM kunden WHERE nr = ?', (kunden_nr,))
            list = cursor.fetchall()[0]
            altes_saldo = list[0]
            name = list[1]

            # Yeni saldo hesapla
            neues_saldo = altes_saldo + ammounts

            # Kunden tablosunda saldoyu güncelle
            cursor.execute(
                'UPDATE kunden SET saldo = ? WHERE nr = ?', (neues_saldo, kunden_nr))

            # Transaktionen tablosuna kayıt ekle
            cursor.execute('INSERT INTO transaktionen (nr, transaktionstyp, betrag) VALUES (?, ?, ?)',
                           (kunden_nr, f'Lohn ({hour}h)', ammounts))

            # Değişiklikleri kaydet
            connection.commit()

            print(tabulate([(kunden_nr, name, ammount, ammounts-ammount, neues_saldo)],
                  headers=["Konto", "Name", "Ammount", "Steuer", "Jetz"], tablefmt="grid"))
            # print(f'Konto {kunden_nr} - {ammount} Euro Gehalt eingezahlt. Jetz Konto: ')

        except sqlite3.Error as error:
            print("Fehler bei der Gehaltszahlung: ", error)

    # Verbindung schließen
    connection.close()

    def abheben(kunden_nr: int, betrag):
        try:
            saldo_aktualisieren(kunden_nr, -betrag)
            # print(f'Konto {kunden_nr} - {betrag}+{st.gebühr}= Euro abgehoben.')
        except sqlite3.Error as error:
            print("Fehler beim Abheben: ", error)

    def einzahlen(kunden_nr, betrag):
        try:
            saldo_aktualisieren(kunden_nr, betrag)
            # print(f'Konto {kunden_nr} - {betrag}-{st.gebühr}={betrag-st.gebühr} Euro eingezahlt.')
        except sqlite3.Error as error:
            print("Fehler beim Einzahlen: ", error)

    def überweisen(quell_kunden_nr, ziel_kunden_nr, betrag):
        try:
            saldo_überweisen(quell_kunden_nr, ziel_kunden_nr, betrag)

            # print(f'Konto {quell_kunden_nr} -> Konto {ziel_kunden_nr}: {betrag} Euro überwiesen.')
        except sqlite3.Error as error:
            print("Fehler beim Überweisen: ", error)

    def saldo_abfragen(kunden_nr):
        try:
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()
            # Aktuelles Saldo des Kunden abfragen
            cursor.execute(
                'SELECT saldo, name FROM kunden WHERE nr = ?', (kunden_nr,))
            saldo, name = cursor.fetchall()[0]

            # Verbindung schließen
            connection.close()

            print(tabulate([(kunden_nr, name, saldo)], headers=[
                  "Nr", "Name", "Konto"], tablefmt="grid"))
            # print(f'Konto {kunden_nr} ({name}) Saldo: {saldo} Euro')
        except sqlite3.Error as error:
            print("Fehler beim Abfragen des Konto: ", error)

    def konto_erstellen(kunden_nr, name, anfangssaldo):
        try:
            connection = sqlite3.connect('bank.db')
            cursor = connection.cursor()

            # Kunden hinzufügen
            cursor.execute(
                'INSERT INTO kunden (nr, name, saldo) VALUES (?, ?, ?)', (kunden_nr, name, anfangssaldo))

            # Änderungen speichern und Verbindung schließen
            connection.commit()
            connection.close()

            print("Konto erstellt")
            print(tabulate([(kunden_nr, name, anfangssaldo)],
                  headers=["Nr", "Name", "Konto"], tablefmt="grid"))
            # print(f'Konto {kunden_nr} erstellt. Anfangssaldo: {anfangssaldo} Eurao')
        except sqlite3.Error as error:
            print("Fehler beim Erstellen des Kontos: ", error)
    
    def Arbeitplatz():
        connection = sqlite3.connect('bank.db')
        cursor = connection.cursor()

        cursor.execute("SELECT nr, name FROM kunden WHERE Nr > 100;")
        for i in cursor.fetchall():
            print(i)

    while True:
        print("\n")
        print("""
        Bankensystem:
        0. Konto erstellen
        2. Einzahlen
        3. Abheben
        4. Lohn
        5. Konto abfragen
        6. Überweisen
        7. Transaktion informieren
        8. Beenden
        """)
        try:
            choice = input("Wählen Sie (0-7): ")
            choice = choice.split(" ")

        except KeyboardInterrupt:
            exit()

        print("\n\n")
        konto_nummer, betrag, hour, transaktion_id = 0, 0, 0 ,0
        match choice[0]:
            case '1':
                try:
                    print("Konto erstellen\n")
                    konto_nummer = input("Geben Sie die Kontonummer ein: ")
                    name = input("Geben Sie den Namen ein: ")
                    anfangssaldo = float(
                        input("Geben Sie den Anfangssaldo ein: "))
                    konto_erstellen(konto_nummer, name, anfangssaldo)
                except ValueError:
                    print(
                        "Fehlerhafte Eingabe. Kontonummer und Anfangssaldo müssen numerisch sein.")

            case '2':
                try:
                    print("Einzahlen\n")

                    match len(choice):
                        case 1:
                            konto_nummer = input(
                                "Geben Sie die Kontonummer ein: ")
                            betrag = input(
                                "Geben Sie den einzuzahlenden Betrag ein: ")
                        case 2:
                            konto_nummer = choice[1]
                            betrag = input(
                                "Geben Sie den einzuzahlenden Betrag ein: ")
                        case 3:
                            konto_nummer = choice[1]
                            betrag = choice[2]

                    einzahlen(int(konto_nummer), int(betrag))
                except ValueError:
                    print("Fehlerhafte Eingabe. Betrag muss numerisch sein.")

            case '3':
                try:
                    print("Abheben\n")
                    match len(choice):
                        case 1:
                            konto_nummer = input(
                                "Geben Sie die Kontonummer ein: ")
                            betrag = input(
                                "Geben Sie den abzuhebenden Betrag ein: ")
                        case 2:
                            konto_nummer = choice[1]
                            betrag = input(
                                "Geben Sie den abzuhebenden Betrag ein: ")
                        case 3:
                            konto_nummer = choice[1]
                            betrag = choice[2]

                    abheben(int(konto_nummer), int(betrag))
                except ValueError:
                    print("Fehlerhafte Eingabe. Betrag muss numerisch sein.")

            case '4':
                try:
                    print("Lohn\n")
                    match len(choice):
                        case 1:
                            konto_nummer = input("Kontonummer eingeben: ")
                            hour = int(input("Gehaltsbetrag eingeben: "))
                        case 2:
                            konto_nummer = choice[1]
                            hour = int(input("Gehaltsbetrag eingeben: "))
                        case 3:
                            konto_nummer = choice[1]
                            hour = int(choice[2])

                    gehatl_anziegen(konto_nummer, hour)

                except ValueError:
                    print("Fehlerhafte Eingabe. Betrag muss numerisch sein.")

            case '5':
                try:
                    print("Konto abfragen\n")
                    match len(choice):
                        case 1:
                            konto_nummer = input(
                                "Geben Sie die Kontonummer ein: ")
                        case 2:
                            konto_nummer = choice[2]

                    saldo_abfragen(konto_nummer)
                except ValueError:
                    print("Fehlerhafte Eingabe. Kontonummer muss numerisch sein.")

            case '6':
                try:
                    print("Überweisen\n")
                    quell_konto_nummer = input(
                        "Geben Sie die Quell-Kontonummer ein: ")
                    ziel_konto_nummer = input(
                        "Geben Sie die Ziel-Kontonummer ein: ")
                    betrag = int(
                        input("Geben Sie den zu überweisenden Betrag ein: "))
                    überweisen(quell_konto_nummer, ziel_konto_nummer, betrag)
                except ValueError:
                    print("Fehlerhafte Eingabe. Betrag muss numerisch sein.")

            case '7':
                try:
                    print("Transaktion informieren\n")
                    match len(choice):
                        case 1:
                            transaktion_id = input(
                                "Geben Sie die Transaktion ID ein: ")
                        case 2:
                            transaktion_id = choice[1]

                    transaktion_informion(int(transaktion_id))
                except ValueError:
                    print("Fehlerhafte Eingabe. Betrag muss numerisch sein.")

            case '8':
                print("Bankensystem wird beendet...")
                break
            
            case '10':
                Arbeitplatz()

            case _:
                if choice[0].startswith("."):
                    das = ""
                    for i in choice:
                        das = das.join(choice)
                    exec(choice[0].replace(".", ""))
                elif choice[0] == "cls":
                    os.system("cls")
                else:
                    print("Ungültige Auswahl!")

    print("\n\n")
except sqlite3.Error as error:
    print("Fehler bei der Datenbankverbindung: ", error)
