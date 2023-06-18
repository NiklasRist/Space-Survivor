#Hilfestellung
#https://docs.python.org/3/library/sqlite3.html#   !!!!besser!!!!
import sqlite3

#leaderboard id<10 und in leaderboard soll das leaderboard gespeichert werden



class speicher:
    
    sql_create_table="""CREATE TABLE IF NOT EXISTS leaderboard (
                            spieler TEXT,
                            Punktzahl INTEGER,
                            id INTEGER PRIMARY KEY
                        )""" 
    sql_insert_var="""INSERT INTO leaderboard(spieler, Punktzahl) VALUES (?, ?)"""
    sql_select_all="""SELECT spieler, Punktzahl FROM leaderboard"""
    sql_order_by_punktzahl="SELECT id FROM leaderboard ORDER BY Punktzahl ASC"
    sql_delete_entry_by_id="DELETE FROM leaderboard WHERE id = ?"
    def __init__(self):
        self.connection = sqlite3.connect(".\speicher\leaderboard.db")
        self.cursor = self.connection.cursor()
        self.create_table()
        #self.create_trigger()

    def create_table(self):
        self.cursor.execute(speicher.sql_create_table)
        self.connection.commit()

    def save_one_entry_in_leaderboard(self, p_spieler, p_punktzahl): 
        self.cursor.execute(speicher.sql_insert_var, (p_spieler, p_punktzahl))#, speicher.row_id))
        self.connection.commit()
        
    def load_entries(self):
        self.cursor.execute(speicher.sql_select_all)
        only_for_debugging= self.cursor.fetchall() #3-dimensionaler Array [(spieler, punktzahl),(spieler, punktzahl),...]
        return only_for_debugging
    
        
    def sort_and_limit_table(self):
        self.cursor.execute("SELECT * FROM leaderboard ORDER BY Punktzahl ASC")
        sorted_entries = self.cursor.fetchall()

        # Temporäre Tabelle erstellen, um die sortierte Reihenfolge beizubehalten
        self.cursor.execute("DROP TABLE IF EXISTS temp_sorted_table")
        self.cursor.execute("CREATE TABLE temp_sorted_table AS SELECT * FROM leaderboard WHERE 0")

        # Sortierte Einträge in die temporäre Tabelle einfügen
        for entry in sorted_entries:
            self.cursor.execute("INSERT INTO temp_sorted_table VALUES (?, ?, ?)", entry)

        # Alte Tabelle löschen
        self.cursor.execute("DROP TABLE leaderboard")

        # Temporäre Tabelle in die ursprüngliche Tabelle umbenennen
        self.cursor.execute("ALTER TABLE temp_sorted_table RENAME TO leaderboard")
        self.connection.commit()
        self.cursor.execute("SELECT * FROM leaderboard ORDER BY Punktzahl ASC")
        self.connection.commit()
        # Einträge über 10 löschen, um die Tabelle auf 10 Einträge zu begrenzen
        self.cursor.execute("SELECT COUNT(*) FROM leaderboard")
        count = self.cursor.fetchone()[0]

        while count > 10:
            self.cursor.execute("DELETE FROM leaderboard WHERE rowid = (SELECT MIN(rowid) FROM leaderboard)")
            self.connection.commit()
            self.cursor.execute("SELECT COUNT(*) FROM leaderboard")
            count = self.cursor.fetchone()[0]

