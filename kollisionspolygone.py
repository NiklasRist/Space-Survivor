import math
class spieler_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(22,15),(6,31),(6,45),(41,45),(41,31),(25,15)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/48*object_size
            eckpunkt[1]=eckpunkt[1]/48*object_size
    def is_in_side(self,polygon_side, x,y) -> bool: #geht das wenn der Bildschirm vergrößert/verkleinert wird
        r=0
        differenz=(self.collision_polygon[polygon_side][0]-self.collision_polygon[polygon_side-1][0], self.collision_polygon[polygon_side][1]-self.collision_polygon[polygon_side-1][1])
        abstand=math.sqrt(differenz[0]**2,differenz[1]**2)
        einheitsvektor=(differenz[0]/abstand,differenz[1]/abstand)
        while (x,y) != (self.collision_polygon[polygon_side-1][0]+r*einheitsvektor[0],self.collision_polygon[polygon_side-1][1]+r*einheitsvektor[1]):
            r+=1
            if r==abstand+1:
                return False
        return True
    
        
        

class projektil_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(3,0),(0,3),(0,6),(3,9),(6,9),(9,6),(9,3),(6,0)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/10*object_size
            eckpunkt[1]=eckpunkt[1]/10*object_size
    def is_in_side(self,polygon_side, x,y) -> bool: #geht das wenn der Bildschirm vergrößert/verkleinert wird
        r=0
        differenz=(self.collision_polygon[polygon_side][0]-self.collision_polygon[polygon_side-1][0], self.collision_polygon[polygon_side][1]-self.collision_polygon[polygon_side-1][1])
        abstand=math.sqrt(differenz[0]**2,differenz[1]**2)
        einheitsvektor=(differenz[0]/abstand,differenz[1]/abstand)
        while (x,y) != (self.collision_polygon[polygon_side-1][0]+r*einheitsvektor[0],self.collision_polygon[polygon_side-1][1]+r*einheitsvektor[1]):
            r+=1
            if r==abstand+1:
                return False
        return True

class asteroid_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(26,9),(7,28),(7,40),(22,55),(43,55),(59,39),(59,27),(41,29)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/67*object_size
            eckpunkt[1]=eckpunkt[1]/63*object_size
    def is_in_side(self,polygon_side, x,y) -> bool: #geht das wenn der Bildschirm vergrößert/verkleinert wird
        r=0
        differenz=(self.collision_polygon[polygon_side][0]-self.collision_polygon[polygon_side-1][0], self.collision_polygon[polygon_side][1]-self.collision_polygon[polygon_side-1][1])
        abstand=math.sqrt(differenz[0]**2,differenz[1]**2)
        einheitsvektor=(differenz[0]/abstand,differenz[1]/abstand)
        while (x,y) != (self.collision_polygon[polygon_side-1][0]+r*einheitsvektor[0],self.collision_polygon[polygon_side-1][1]+r*einheitsvektor[1]):
            r+=1
            if r==abstand+1:
                return False
        return True
            
class enemy_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(26,23),(15,34),(15,52),(24,61),(38,61),(49,50),(49,35),(37,23)]
    def rescale_polygon(self, object_size, polygon):
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/64*object_size
            eckpunkt[1]=eckpunkt[1]/64*object_size
    def is_in_side(self,polygon_side, x,y) -> bool: #geht das wenn der Bildschirm vergrößert/verkleinert wird
        r=0
        differenz=(self.collision_polygon[polygon_side][0]-self.collision_polygon[polygon_side-1][0], self.collision_polygon[polygon_side][1]-self.collision_polygon[polygon_side-1][1])
        abstand=math.sqrt(differenz[0]**2,differenz[1]**2)
        einheitsvektor=(differenz[0]/abstand,differenz[1]/abstand)
        while (x,y) != (self.collision_polygon[polygon_side-1][0]+r*einheitsvektor[0],self.collision_polygon[polygon_side-1][1]+r*einheitsvektor[1]):
            r+=1
            if r==abstand+1:
                return False
        return True