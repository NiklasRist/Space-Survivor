#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3
connection = sqlite3.connect("Speicher.db")
cursor=connection.cursor()

sqlCreateTable="""CREATE TABLE leaderboard (Spieler, Punktzahl)"""
sqlInsertVar="""INSERT INTO leaderboard(Spieler, Punktzahl) VALUES (?, ?)"""

def createTable():
    cursor.execute(sqlCreateTable)

def saveLeaderboard(pSpieler, pPunktzahl): 
    cursor.execute(sqlInsertVar, (pSpieler, pPunktzahl))
    

saveLeaderboard("Wolf", 3)