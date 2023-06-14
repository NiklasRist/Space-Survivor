from spieler import spieler
from gegner_spawnen import gegner_spawnen
event1 = gegner_spawnen()
event2 = event1
event3 = event1
event = [event1, event2, event3]

class shop():
    
    def __init__(self):
        pass
    
    def pruefen_ob_genug_punkte(self, spieler, event_nummer, spieler_objekt):
        genug_punkte = spieler.spieler_punkte >= event[event_nummer].get_kosten()
        if genug_punkte:
            self.event_ausführen(spieler, event_nummer, spieler_objekt)
            spieler.spieler_punkte = spieler.spieler_punkte - event[event_nummer].get_kosten()
            return "Event gekauft!"
            
        else:
            return "Nicht genügend Punkte!"
    
    def event_ausführen(self, spieler, event_nummer, spieler_objekt):
        event[event_nummer].ausfuehren()
