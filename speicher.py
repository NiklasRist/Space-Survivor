#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3

#leaderboard id<10 und in leaderboard soll das leaderboard gespeichert werden



class Speicher:
    connection = sqlite3.connect(".\speicher\leaderboard.db")
    cursor=connection.cursor()
    
    sqlCreateTable="""CREATE TABLE leaderboard (Spieler, Punktzahl, id)""" #id automatisch zugewiesen, beginnt bei 0
    sqlInsertVar="""INSERT INTO leaderboard(Spieler, Punktzahl) VALUES (?, ?)"""
    sqlSelectAll="""SELECT Spieler, Punktzahl FROM leaderboard"""
    sqlUpdateOneEntry="""UPDATE leaderboard SET Spieler=?, Punktzahl=? WHERE id=?"""
    def __init__(self):
        pass

    def createTable(self):
        Speicher.cursor.execute(Speicher.sqlCreateTable)

    def saveOneEntryInLeaderboard(self, pSpieler, pPunktzahl): 
        Speicher.cursor.execute(Speicher.sqlInsertVar, (pSpieler, pPunktzahl))#, Speicher.row_id))
        Speicher.connection.commit()
        #Speicher.row_id+=1
        
    def updateEntry(self, pSpieler, pPunktzahl, pZeile):
        Speicher.cursor.execute(Speicher.sqlUpdateOneEntry,(pSpieler, pPunktzahl, pZeile))
        
    def updateEntries(self):
        pass

    def deleteEntries(self):
        pass

    def deleteAllEntries(self):
        pass

    def loadEntries(self):
        Speicher.cursor.execute(Speicher.sqlSelectAll)
        return Speicher.cursor.fetchall() #2-dimensionaler Array [(spieler, punktzahl),(spieler, punktzahl),...]

#Speicher.createTable
#Speicher.saveOneEntryInLeaderboard("Nur", 7)
#Speicher.saveOneEntryInLeaderboard("Nur", 7)
#Speicher.updateEntry("HArald", 24, 0)
#print(Speicher.loadEntries())
 
