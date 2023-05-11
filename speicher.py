#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3
connection = sqlite3.connect("Speicher.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE leaderboard (Spieler, Punktzahl)""")

def saveLeaderboard(pSpieler, pPunktzahl): #wie kombiniert man sql_command mit variablen vom typ array???
    cursor.execute("""INSERT INTO leaderboard()""")