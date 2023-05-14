#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3
connection = sqlite3.connect("Speicher.db")
cursor=connection.cursor()

sqlCreateTable="""CREATE TABLE leaderboard (Spieler, Punktzahl)"""
sqlInsertVar="""INSERT INTO leaderboard(Spieler, Punktzahl) VALUES (?, ?)"""
sqlSelectAll="""SELECT * FROM leaderboard"""

def createTable():
    cursor.execute(sqlCreateTable)

def saveOneEntryInLeaderboard(pSpieler, pPunktzahl): 
    cursor.execute(sqlInsertVar, (pSpieler, pPunktzahl))
    connection.commit()
    
def updateEntries():
    pass

def deleteEntries():
    pass
 
def loadEntries():
    cursor.execute(sqlSelectAll)
    print(cursor.fetchone())
    
saveOneEntryInLeaderboard("ssww", 4)
loadEntries()
 
