from Spieler import Spieler
from GegnerSpawnen import GegnerSpawnen
event1 = GegnerSpawnen()
event2 = 
event3 =
Event = [event1, event2, event3]

class Shop():
    
    def __init__(self):
        pass
    
    def pruefenObGenugPunkte(spieler, eventNummer, SpielerObjekt):
        genugPunkte = Spieler.spielerPunkte >= Event[eventNummer].getKosten()
        if genugPunkte:
            Shop.eventAusführen(eventNummer)
            return "Event gekauft!"
            Spieler.spielerPunkte = Spieler.spielerPunkte - Event[eventNummer].getKosten()
        else:
            return "Nicht genügend Punkte!"
    
    def eventAusführen(spieler, eventNummer, SpielerObjekt):
        Event[eventNummer].ausfuehren()
