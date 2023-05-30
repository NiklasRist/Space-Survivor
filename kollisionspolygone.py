class spieler_polygon:
    def __init__(self) -> None:
        self.collision_polygon_complex=[(22,16),(22,21),(21,22),(19,22),(19,25)(18,26),(16,26),(15,25),(15,22),(13,22),(13,31),(12,32),(10,32),(9,31),(9,29),(6,29),(6,41),(15,41),(16,42),(16,44),(21,44),(21,42),(22,41),(25,41),(26,42),(26,44),(31,44),(31,42),(32,41),(41,41),(41,29),(38,29),(38,31),(37,32),(35,32),(34,31),(34,22),(32,22),(32,25),(31,26),(29,26), (29,25), (28,22), (26,22), (25,21), (25,16)]
        self.collision_polygon=[(22,15),(6,31),(6,45),(41,45),(41,31),(25,15)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/48*object_size
            eckpunkt[1]=eckpunkt[1]/48*object_size

class projektil_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(3,0),(0,3),(0,6),(3,9),(6,9),(9,6),(9,3),(6,0)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/10*object_size
            eckpunkt[1]=eckpunkt[1]/10*object_size

class asteroid_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(26,9),(7,28),(7,40),(22,55),(43,55),(59,39),(59,27),(41,29)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/67*object_size
            eckpunkt[1]=eckpunkt[1]/63*object_size