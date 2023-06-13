class leaderboard:
	spieler=[]
	punktzahl=[]
	
	def __init__(self):
		self.spieler = []
		self.punktzahl = []
	
	def addToBoard(self, pSpieler, pPunktzahl):
		self.spieler.append(pSpieler)
		self.punktzahl.append(pPunktzahl)
  
	def sortBoardByScoreDesc(self):
		for i in range(len(self.punktzahl)):
			for j in range(len(self.punktzahl)-1-i):
				if self.punktzahl[j] > self.punktzahl[j + 1]:
						self.punktzahl[j], self.punktzahl[j+1],self.spieler[j], self.spieler[j+1] = self.punktzahl[j+1], self.punktzahl[j],self.spieler[j+1], self.spieler[j]
      
	def deleteUnnecessaryEntries(self):
		while len(self.punktzahl)>10:
			self.punktzahl, self.spieler=self.punktzahl[1:], self.spieler[1:]

	def updateBoard(self, pSpieler, pPunktzahl):
		self.addToBoard(pSpieler, pPunktzahl)
		self.sortBoardByScoreDesc()
		self.deleteUnnecessaryEntries()
