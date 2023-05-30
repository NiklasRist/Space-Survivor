class leaderboard:
	spieler=[]
	punktzahl=[]
	
	def __init__(self):
		self.spieler = []
		self.punktzahl = []
	
	def addToBoard(self, pSpieler, pPunktzahl):
		leaderboard.spieler+=pSpieler
		leaderboard.punktzahl+=pPunktzahl
  
	def sortBoardByScoreDesc(self):
		for i in range(len(leaderboard.punktzahl)):
			for j in range(len(leaderboard.punktzahl)-1-i):
				if leaderboard.punktzahl[j] > leaderboard.punktzahl[j + 1]:
						leaderboard.punktzahl[j], leaderboard.punktzahl[j+1],leaderboard.spieler[j], leaderboard.spieler[j+1] = leaderboard.punktzahl[j+1], leaderboard.punktzahl[j],leaderboard.spieler[j+1], leaderboard.spieler[j]
      
	def deleteUnnecessaryEntries(self):
		while len(leaderboard.punktzahl)>10:
			leaderboard.punktzahl, leaderboard.spieler=leaderboard.punktzahl[1:], leaderboard.spieler[1:]

	def updateBoard(self, pSpieler, pPunktzahl):
		self.addToBoard(pSpieler, pPunktzahl)
		self.sortBoardByScoreDesc()
		self.deleteUnnecessaryEntries()
