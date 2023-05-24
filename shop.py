from spieler import Spieler
from gegner_spawnen import GegnerSpawnen
event1 = GegnerSpawnen()
event2 = event1
event3 = event1
Event = [event1, event2, event3]

class Shop():
    
    def __init__(self):
        pass
    
    def pruefenObGenugPunkte(self, spieler, eventNummer, SpielerObjekt):
        genugPunkte = Spieler.spielerPunkte >= Event[eventNummer].getKosten()
        if genugPunkte:
            self.eventAusführen(spieler, eventNummer, SpielerObjekt)
            Spieler.spielerPunkte = Spieler.spielerPunkte - Event[eventNummer].getKosten()
            return "Event gekauft!"
            
        else:
            return "Nicht genügend Punkte!"
    
    def eventAusführen(self, spieler, eventNummer, SpielerObjekt):
        Event[eventNummer].ausfuehren()
