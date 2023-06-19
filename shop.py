from event import schwartzesloch, verwirrung

class shop():
    def __init__(self):
        self.event_aktiv = [False, False, False, False]
        self.verwirrung_obj = verwirrung()
        self.schwartzesloch_obj = schwartzesloch(1)

    def pruefen_ob_genug_punkte(self, spieler, event_nummer):

        if event_nummer == 1 | event_nummer == 2:
            genug_punkte = spieler.spieler_punkte >= self.verwirrung_obj.get_kosten()
            if genug_punkte:
                self.event_aktiv[event_nummer - 1] = True
                return "Event gekauft!"
                
            else:
                return "nicht genügend punkte"
        if event_nummer == 3 | event_nummer == 4:
            genug_punkte = spieler.spieler_punkte >= self.schwartzesloch_obj.get_kosten()
            if genug_punkte:
                self.event_aktiv[event_nummer - 1] = True
                return "Event gekauft!"
                
            else:
                return "Nicht genügend Punkte!"
