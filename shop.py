from event import schwartzesloch, verwirrung

class shop():
    def __init__(self):
        self.verwirrung_obj = verwirrung()
        self.schwartzesloch_obj = schwartzesloch(1)
        self.ausgabe = None

    def pruefen_ob_genug_punkte(self, spieler, event_nummer, steuerung_obj):

        if event_nummer == 1 or event_nummer == 2:
            genug_punkte = spieler.punkte >= self.verwirrung_obj.get_kosten()
            if genug_punkte:
                steuerung_obj.event[event_nummer - 1] = True
                self.ausgabe = "Event gekauft!"
                return self.ausgabe
                
            else:
                return "Nicht genügend Punkte!"
        if event_nummer == 3 or event_nummer == 4:
            genug_punkte = spieler.punkte >= self.schwartzesloch_obj.get_kosten()
            if genug_punkte:
                steuerung_obj.event[event_nummer - 1] = True
                self.ausgabe = "Event gekauft!"
                return self.ausgabe
                
            else:
                self.ausgabe = "Nicht genügend Punkte!"
                return self.ausgabe
