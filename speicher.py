#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3

#leaderboard id<10 und in leaderboard soll das leaderboard gespeichert werden



class speicher:
    connection = sqlite3.connect(".\speicher\leaderboard.db")
    cursor=connection.cursor()
    
    sql_create_table="""CREATE TABLE leaderboard (spieler, Punktzahl, id)""" #id automatisch zugewiesen, beginnt bei 0
    sql_insert_var="""INSERT INTO leaderboard(spieler, Punktzahl) VALUES (?, ?)"""
    sql_select_all="""SELECT spieler, Punktzahl FROM leaderboard"""
    sql_update_one_entry="""UPDATE leaderboard SET spieler=?, Punktzahl=? WHERE id=?"""
    def __init__(self):
        pass

    def create_table(self):
        speicher.cursor.execute(speicher.sql_create_table)

    def save_one_entry_in_leaderboard(self, p_spieler, p_punktzahl): 
        speicher.cursor.execute(speicher.sql_insert_var, (p_spieler, p_punktzahl))#, speicher.row_id))
        speicher.connection.commit()
        #speicher.row_id+=1
        
    def update_entry(self, p_spieler, p_punktzahl, p_zeile):
        speicher.cursor.execute(speicher.sql_update_one_entry,(p_spieler, p_punktzahl, p_zeile))
        
    def update_entries(self):
        pass

    def delete_entries(self):
        pass

    def delete_all_entries(self):
        pass

    def load_entries(self):
        speicher.cursor.execute(speicher.sql_select_all)
        return speicher.cursor.fetchall() #2-dimensionaler Array [(spieler, punktzahl),(spieler, punktzahl),...]


 
