import sqlite3

class Speicher:
    '''
    Eine Klasse, die die Speicherfunktionen für das Leaderboard implementiert.

    Attributes:
        connection: Eine Verbindung zur SQLite-Datenbank.
        cursor: Ein Cursor-Objekt zum Ausführen von SQL-Abfragen.

    Methods:
        __init__(): Initialisiert den Speicher und stellt eine Verbindung zur Datenbank her.
        create_table(): Erstellt die Tabelle leaderboard in der Datenbank, falls sie noch nicht existiert.
        save_one_entry_in_leaderboard(p_spieler, p_punktzahl): Speichert einen Eintrag im Leaderboard in der Datenbank.
        load_entries(): Lädt alle Einträge aus der Datenbank.
        sort_and_limit_table(): Sortiert die Einträge in der Datenbank nach der Punktzahl und begrenzt die Anzahl auf 10.
    '''

    sql_create_table = """CREATE TABLE IF NOT EXISTS leaderboard (
                            spieler TEXT,
                            Punktzahl INTEGER,
                            id INTEGER PRIMARY KEY
                        )"""

    sql_insert_var = """INSERT INTO leaderboard(spieler, Punktzahl) VALUES (?, ?)"""
    sql_select_all = """SELECT spieler, Punktzahl FROM leaderboard"""
    sql_order_by_punktzahl = "SELECT id FROM leaderboard ORDER BY Punktzahl ASC"
    sql_delete_entry_by_id = "DELETE FROM leaderboard WHERE id = ?"

    def __init__(self):
        '''
        Initialisiert den Speicher und stellt eine Verbindung zur Datenbank her.

        Args:
            None

        Returns:
            None

        Raises:
            None
        '''
        self.connection = sqlite3.connect(".\speicher\leaderboard.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        '''
        Erstellt die Tabelle leaderboard in der Datenbank, falls sie noch nicht existiert.

        Args:
            None

        Returns:
            None

        Raises:
            None
        '''
        self.cursor.execute(Speicher.sql_create_table)
        self.connection.commit()

    def save_one_entry_in_leaderboard(self, p_spieler, p_punktzahl):
        '''
        Speichert einen Eintrag im Leaderboard in der Datenbank.

        Args:
            p_spieler (str): Der Name des Spielers.
            p_punktzahl (int): Die Punktzahl des Spielers.

        Returns:
            None

        Raises:
            None
        '''
        self.cursor.execute(Speicher.sql_insert_var, (p_spieler, p_punktzahl))
        self.connection.commit()

    def load_entries(self):
        '''
        Lädt alle Einträge aus der Datenbank.

        Args:
            None

        Returns:
            only_for_debugging (list): Eine Liste der geladenen Einträge. Jeder Eintrag ist ein Tupel (spieler, punktzahl).

        Raises:
            None
        '''
        self.cursor.execute(Speicher.sql_select_all)
        only_for_debugging = self.cursor.fetchall()
        return only_for_debugging

    def sort_and_limit_table(self):
        '''
        Sortiert die Einträge in der Datenbank nach der Punktzahl und begrenzt die Anzahl auf 10.

        Args:
            None

        Returns:
            None

        Raises:
            None
        '''
        self.cursor.execute("SELECT * FROM leaderboard ORDER BY Punktzahl ASC")
        sorted_entries = self.cursor.fetchall()

        # Temporäre Tabelle erstellen, um die sortierte Reihenfolge beizubehalten
       
