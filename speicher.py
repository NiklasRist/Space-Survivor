#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3
class Speicher:
    connection = sqlite3.connect("Speicher.db")
    cursor=connection.cursor()
    
    sqlCreateTable="""CREATE TABLE leaderboard (Spieler, Punktzahl, id)"""
    sqlInsertVar="""INSERT INTO leaderboard(Spieler, Punktzahl, id) VALUES (?, ?, ?)"""
    sqlSelectAll="""SELECT Spieler, Punktzahl FROM leaderboard"""
    sqlUpdateOneEntry="""UPDATE leaderboard SET Spieler=?, Punktzahl=? WHERE id=?"""
    
    row_id=0

    def createTable():
        Speicher.cursor.execute(Speicher.sqlCreateTable)

    def saveOneEntryInLeaderboard(pSpieler, pPunktzahl): 
        Speicher.cursor.execute(Speicher.sqlInsertVar, (pSpieler, pPunktzahl, Speicher.row_id))
        Speicher.connection.commit()
        row_id+=1
        
    def updateEntry(pSpieler, pPunktzahl, pZeile):
        Speicher.cursor.execute(Speicher.sqlUpdateOneEntry,(pSpieler, pPunktzahl, pZeile))
        
    def updateEntries():
        pass

    def deleteEntries():
        pass

    def deleteAllEntries():
        pass

    def loadEntries():
        Speicher.cursor.execute(Speicher.sqlSelectAll)
        return Speicher.cursor.fetchall() #2-dimensionaler Array [(spieler, punktzahl),(spieler, punktzahl),...]

Speicher.createTable
Speicher.saveOneEntryInLeaderboard("Nur", 7)
Speicher.saveOneEntryInLeaderboard("Nur", 7)
Speicher.updateEntry("HArald", 24, 0)
print(Speicher.loadEntries)
 
