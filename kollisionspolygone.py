import math

class polygon:
    def __init__(self) -> None:
        self.collision_polygon=[]
        self.mittelpunkt=[]
        self.sides=0
    def rescale_polygon(self, object_size):
        add_all=[0,0]
        for eckpunkt in self.collision_polygon:
            eckpunkt[0]=eckpunkt[0]/1*object_size
            eckpunkt[1]=eckpunkt[1]/1*object_size
            add_all[0]+=eckpunkt[0]
            add_all[1]+=eckpunkt[1]
        self.mittelpunkt=[int(add_all[0]/6),int(add_all[1]/6)]
      
    def move_polygon(self, vektor):
        for eckpunkt in self.collision_polygon: 
            eckpunkt[0]+=vektor[0]
            eckpunkt[1]+=vektor[1]  
            self.mittelpunkt[0]+=vektor
            self.mittelpunkt[1]+=vektor   
    
    def give_schnittpunkt(self, polygon_side, polygon_object) -> list: 
        '''
            Jedes Kollisionspolygon hat viele Seiten.
            Die Seitennummerierung beginnt bei den Strecke zwischen den ersten beiden Punkten mit Seite 1.
            Diese Funktion berechnet den Schnittpunkt zweier Liniensegmente:
            a:x=self.mittelpunkt+r*(polygon_object.mittelpunkt-self.mittelpunkt)) (Teil der Abstandsgerade)
            s:x=self.collison_polygon[polygon_side-1]+r*(self.collison_polygon[polygon_side]-self.collision_polygon[polygon_side-1]))) (Teil der Polygonseitengerade)
            schittpunkt(x,y,lines_are_identical)
        '''
        parametergleichungsvariable=(((self.mittelpunkt[0]-self.collision_polygon[polygon_side-1][0])*(self.collision_polygon[polygon_side-1][1]-self.collision_polygon[polygon_side][1]))-((self.mittelpunkt[1]-self.collision_polygon[polygon_side-1][1])*(self.collision_polygon[polygon_side-1][0]-self.collision_polygon[polygon_side][0])))/(((self.mittelpunkt[0]-polygon_object.mittelpunkt[0])*(self.collision_polygon[polygon_side-1][1]-self.collision_polygon[polygon_side][1]))-((self.mittelpunkt[1]-polygon_object.mittelpunkt[1])*(self.collision_polygon[polygon_side-1][0]-self.collision_polygon[polygon_side][0])),False)
        schnittpunkt=[(self.mittelpunkt[0]+parametergleichungsvariable*(polygon_object.mittelpunkt[0]-self.mittelpunkt[0])),(self.mittelpunkt[1]+parametergleichungsvariable*(polygon_object.mittelpunkt[1]-self.mittelpunkt[1]))]
        if 0<=parametergleichungsvariable<=1: #Schnitttpunkt?
            return schnittpunkt
        elif self.mittelpunkt==self.collision_polygon[polygon_side-1] and polygon_object.mittelpunkt==self.collision_polygon[polygon_side]: #identisch?
            schnittpunkt[2]=True
            return schnittpunkt
        else: return None #parallel?
        
    def collision(self, polygon_object):
        '''
            Prüft ob der Schnittpunkt eines anderen Polygons auf oder zwischen dem Mittelpunkt oder dem Schnittpunkt dieses Polygons ist.
        '''
        schnittpunkt_1=[]
        schnittpunkt_2=[]
        for side in range(self.sides):
            
            zw=self.give_schnittpunkt(side+1, polygon_object)
            if type(zw)==list and math.sqrt((polygon_object.mittelpunkt[0]-zw[0])**2 + (polygon_object.mittelpunkt[1]-zw[1])**2)<= math.sqrt((polygon_object.mittelpunkt[0]-self.mittelpunkt[0])**2+(polygon_object.mittelpunkt[1]-self.mittelpunkt[1])**2): #nicht parallel und mittelpunkt_1<=Schnittpunkt<=mittelpunkt_2
                schnittpunkt_1=zw
                schnittpunkt_2=schnittpunkt_1
                if zw[2]==False:
                    for p_side in range(polygon_object.sides):
                        zw=polygon_object.give_schnittpunkt(p_side+1, self)
                        if type(zw)==list and math.sqrt((self.mittelpunkt[0]-zw[0])**2 + (self.mittelpunkt[1]-zw[1])**2)<= math.sqrt((polygon_object.mittelpunkt[0]-self.mittelpunkt[0])**2+(polygon_object.mittelpunkt[1]-self.mittelpunkt[1])**2): #nicht parallel und mittelpunkt_1<=Schnittpunkt<=mittelpunkt_2
                            schnittpunkt_2=zw
        if polygon_object.mittelpunkt<=schnittpunkt_1<=schnittpunkt_2 or polygon_object.mittelpunkt>=schnittpunkt_1>=schnittpunkt_2 : #zwischen mittelpunkt und schnitt punkt von polygon_object?
            return True
        else:
            return False
 
    
class spieler_polygon(polygon):
    def __init__(self) -> None:
        self.collision_polygon=[(22,15),(6,31),(6,45),(41,45),(41,31),(25,15)]
        self.mittelpunkt=[24, 30]
        self.sides=6
    def rescale_polygon(self, object_size):
        add_all=[0,0]
        for eckpunkt in self.collision_polygon:
            eckpunkt[0]=eckpunkt[0]/48*object_size
            eckpunkt[1]=eckpunkt[1]/48*object_size
            add_all[0]+=eckpunkt[0]
            add_all[1]+=eckpunkt[1]
        self.mittelpunkt=[int(add_all[0]/6),int(add_all[1]/6)]
      

        '''
            Prüft ob der Schnittpunkt eines anderen Polygons auf oder zwischen dem Mittelpunkt oder dem Schnittpunkt dieses Polygons ist.
        '''
        schnittpunkt_1=[]
        schnittpunkt_2=[]
        for side in range(self.sides):
            
            zw=self.give_schnittpunkt(side+1, polygon_object)
            if type(zw)==list and math.sqrt((polygon_object.mittelpunkt[0]-zw[0])**2 + (polygon_object.mittelpunkt[1]-zw[1])**2)<= math.sqrt((polygon_object.mittelpunkt[0]-self.mittelpunkt[0])**2+(polygon_object.mittelpunkt[1]-self.mittelpunkt[1])**2): #nicht parallel und mittelpunkt_1<=Schnittpunkt<=mittelpunkt_2
                schnittpunkt_1=zw
                schnittpunkt_2=schnittpunkt_1
                if zw[2]==False:
                    for p_side in range(polygon_object.sides):
                        zw=polygon_object.give_schnittpunkt(p_side+1, self)
                        if type(zw)==list and math.sqrt((self.mittelpunkt[0]-zw[0])**2 + (self.mittelpunkt[1]-zw[1])**2)<= math.sqrt((polygon_object.mittelpunkt[0]-self.mittelpunkt[0])**2+(polygon_object.mittelpunkt[1]-self.mittelpunkt[1])**2): #nicht parallel und mittelpunkt_1<=Schnittpunkt<=mittelpunkt_2
                            schnittpunkt_2=zw
        if polygon_object.mittelpunkt<=schnittpunkt_1<=schnittpunkt_2 or polygon_object.mittelpunkt>=schnittpunkt_1>=schnittpunkt_2 : #zwischen mittelpunkt und schnitt punkt von polygon_object?
            return True
        else:
            return False
 

class projektil_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(3,0),(0,3),(0,6),(3,9),(6,9),(9,6),(9,3),(6,0)]
        self.mittelpunkt=[]
        sides=8
    def rescale_polygon(self, object_size, polygon):
        add_all=[0,0]
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/10*object_size
            eckpunkt[1]=eckpunkt[1]/10*object_size
            add_all[0]+=eckpunkt[0]
            add_all[1]+=eckpunkt[1]
        self.mittelpunkt=[int(add_all[0]/6),int(add_all[1]/6)]

class asteroid_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(26,9),(7,28),(7,40),(22,55),(43,55),(59,39),(59,27),(41,29)]
        sides=8
    def rescale_polygon(self, object_size, polygon):
        add_all=[0,0]
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/67*object_size
            eckpunkt[1]=eckpunkt[1]/63*object_size
            add_all[0]+=eckpunkt[0]
            add_all[1]+=eckpunkt[1]
        self.mittelpunkt=[int(add_all[0]/6),int(add_all[1]/6)]
         
class enemy_polygon:
    def __init__(self) -> None:
        self.collision_polygon=[(26,23),(15,34),(15,52),(24,61),(38,61),(49,50),(49,35),(37,23)]
        sides=8
    def rescale_polygon(self, object_size, polygon):
        add_all=[0,0]
        for eckpunkt in polygon:
            eckpunkt[0]=eckpunkt[0]/64*object_size
            eckpunkt[1]=eckpunkt[1]/64*object_size
            add_all[0]+=eckpunkt[0]
            add_all[1]+=eckpunkt[1]
        self.mittelpunkt=[int(add_all[0]/6),int(add_all[1]/6)]

        '''
            Jedes Kollisionspolygon hat viele Seiten.
            Die Seitennummerierung beginnt bei den Strecke zwischen den ersten beiden Punkten mit Seite 1.
            Diese Funktion berechnet den Schnittpunkt zweier Liniensegmente:
            a:x=self.mittelpunkt+r*(polygon_object.mittelpunkt-self.mittelpunkt)) (Teil der Abstandsgerade)
            s:x=self.collison_polygon[polygon_side-1]+r*(self.collison_polygon[polygon_side]-self.collision_polygon[polygon_side-1]))) (Teil der Polygonseitengerade)
            schittpunkt(x,y,lines_are_identical)
        '''
        parametergleichungsvariable=(((self.mittelpunkt[0]-self.collision_polygon[polygon_side-1][0])*(self.collision_polygon[polygon_side-1][1]-self.collision_polygon[polygon_side][1]))-((self.mittelpunkt[1]-self.collision_polygon[polygon_side-1][1])*(self.collision_polygon[polygon_side-1][0]-self.collision_polygon[polygon_side][0])))/(((self.mittelpunkt[0]-polygon_object.mittelpunkt[0])*(self.collision_polygon[polygon_side-1][1]-self.collision_polygon[polygon_side][1]))-((self.mittelpunkt[1]-polygon_object.mittelpunkt[1])*(self.collision_polygon[polygon_side-1][0]-self.collision_polygon[polygon_side][0])),False)
        schnittpunkt=[(self.mittelpunkt[0]+parametergleichungsvariable*(polygon_object.mittelpunkt[0]-self.mittelpunkt[0])),(self.mittelpunkt[1]+parametergleichungsvariable*(polygon_object.mittelpunkt[1]-self.mittelpunkt[1]))]
        if 0<=parametergleichungsvariable<=1:
            return schnittpunkt
        elif self.mittelpunkt==self.collision_polygon[polygon_side-1] and polygon_object.mittelpunkt==self.collision_polygon[polygon_side]:
            schnittpunkt[2]=True
            return schnittpunkt
        else: return None