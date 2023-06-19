class leaderboard:
    '''
    Eine Klasse, die ein Leaderboard verwaltet.

    Attributes:
        spieler (list): Eine Liste der Spieler auf dem Leaderboard.
        punktzahl (list): Eine Liste der Punktzahlen der Spieler.

    Methods:
        __init__(): Initialisiert das Leaderboard.
        addToBoard(p_spieler, p_punktzahl): Fügt einen Spieler und seine Punktzahl dem Leaderboard hinzu.
        sortBoardByScoreDesc(): Sortiert das Leaderboard in absteigender Reihenfolge der Punktzahlen.
        deleteUnnecessaryEntries(speicher_obj): Löscht überflüssige Einträge aus dem Leaderboard.
        updateBoard(p_spieler, p_punktzahl, speicher_obj): Aktualisiert das Leaderboard mit einem neuen Spieler und einer Punktzahl.
    '''

    def __init__(self):
        '''
        Initialisiert das Leaderboard.

        Args:
            None

        Returns:
            None

        Raises:
            None
        '''
        self.spieler = []
        self.punktzahl = []

    def addToBoard(self, p_spieler, p_punktzahl):
        '''
        Fügt einen Spieler und seine Punktzahl dem Leaderboard hinzu.

        Args:
            p_spieler (str): Der Name des Spielers.
            p_punktzahl (int): Die Punktzahl des Spielers.

        Returns:
            None

        Raises:
            None
        '''
        self.spieler.append(p_spieler)
        self.punktzahl.append(p_punktzahl)

    def sortBoardByScoreDesc(self):
        '''
        Sortiert das Leaderboard in absteigender Reihenfolge der Punktzahlen.

        Args:
            None

        Returns:
            None

        Raises:
            None
        '''
        for i in range(len(self.punktzahl)):
            for j in range(len(self.punktzahl) - 1 - i):
                if self.punktzahl[j] > self.punktzahl[j + 1]:
                    self.punktzahl[j], self.punktzahl[j + 1], self.spieler[j], self.spieler[j + 1] = \
                        self.punktzahl[j + 1], self.punktzahl[j], self.spieler[j + 1], self.spieler[j]

    def deleteUnnecessaryEntries(self, speicher_obj):
        '''
        Löscht überflüssige Einträge aus dem Leaderboard.

        Args:
            speicher_obj: Das Objekt, das zum Speichern der Leaderboard-Daten verwendet wird.

        Returns:
            None

        Raises:
            None
        '''
        while len(self.punktzahl) > 10:
            self.punktzahl, self.spieler = self.punktzahl[1:], self.spieler[1:]

    def updateBoard(self, p_spieler, p_punktzahl, speicher_obj):
        '''
        Aktualisiert das Leaderboard mit einem neuen Spieler und einer Punktzahl.

        Args:
            p_spieler (str): Der Name des Spielers.
            p_punktzahl (int): Die Punktzahl des Spielers.
            speicher_obj: Das Objekt, das zum Speichern der Leaderboard-Daten verwendet wird.

        Returns:
            None

        Raises:
            None
        '''
        self.addToBoard(p_spieler, p_punktzahl)
        self.sortBoardByScoreDesc()
        self.deleteUnnecessaryEntries(speicher_obj)
