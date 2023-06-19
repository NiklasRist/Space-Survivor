from spieler import spieler
from event import verwirrung, schwartzesloch
event1 = None
event2 = event1
event3 = event1

class shop():
    """
    Represents a shop in the game.
    """
    def __init__(self):
        self.verwirrung_obj=verwirrung()    #kosten=10
        self.schwartzesloch_obj=schwartzesloch() #kosten=10
    
    def pruefen_ob_genug_punkte(self, spieler, event_nummer):
        """
        Checks if the player has enough points to purchase the event.

        Args:
            spieler (Spieler): The player object.
            event_nummer (int): The number of the event to be purchased.

        Returns:
            str: A message indicating whether the event was purchased or not.
        """
        genug_punkte = spieler.spieler_punkte >= event[event_nummer].get_kosten()
        if genug_punkte:
            self.event_ausführen(spieler, event_nummer)
            spieler.spieler_punkte = spieler.spieler_punkte - event[event_nummer].get_kosten()
            return "Event gekauft!"
            
        else:
            return "Nicht genügend Punkte!"
    

