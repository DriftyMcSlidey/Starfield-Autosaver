#zu erst prüfen wir ob alle Pakete da sind. Wenn nicht istallieren wir die nach
import subprocess
import sys

def installiere_paket(paket):
    subprocess.check_call([sys.executable, "-m", "pip", "install", paket])

def pruefe_und_installiere_pakete(pakete):
    for paket in pakete:
        try:
            __import__(paket)
        except ImportError:
            print(f"Das Paket '{paket}' ist nicht installiert. Installiere es jetzt...")
            installiere_paket(paket)

# Liste der zu prüfenden Pakete
zu_pruefende_pakete = ['pygetwindow', 'pyautogui']

# Prüfe und installiere die Pakete falls notwendig
pruefe_und_installiere_pakete(zu_pruefende_pakete)

#ab hier beginnt das Autosave Script
import pygetwindow as gw
import pyautogui
import datetime
import time
print(f"Starfield Autosaver ist gestartet.")
print(f"Bitte schließe dieses Fenster nicht!")
print(f"Zum Beenden einfach das Fenster schließen.\n")
print(f"Du kannst jetzt das Spiel starten und spielen.")
print(f"Du hast 10 Minuten Zeit das alte Quicksave zu laden.")
print(f"Viel Spaß.\n")
while True:
    # Zeit um 10 Minuten erhöhen
    aktuelle_zeit = datetime.datetime.now()
    naechstes_quicksave = aktuelle_zeit + datetime.timedelta(minutes=10)
    print(f"Save geplant: {naechstes_quicksave}")
    # Warte 600 Sekunden
    time.sleep(600)
    # Finde Fenster mit dem Titel "starfield"
    fenster_liste = gw.getWindowsWithTitle('Starfield')
    # Die For Schleife muss sein, wir wollen ja nicht ein Browser oder anderes Fenster
    for fenster in fenster_liste:
        # Überprüfe, ob das Fenster gefunden wurde
        if fenster.title == "Starfield":
            #fenster.activate()  # Aktiviere das Fenster (optional)
            #Finde das aktive Fenster
            aktiv_fenster = gw.getActiveWindow()
            aktiv_fenster_titel = aktiv_fenster.title
            if aktiv_fenster_titel == "Starfield":
                aktuelles_datum = datetime.datetime.now()
                print(f"Save erstellt: {aktuelles_datum}")
                # Halte die F5-Taste für X Sekunden
                pyautogui.keyDown('f5')
                time.sleep(2)
                pyautogui.keyUp('f5')