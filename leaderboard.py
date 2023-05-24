class leaderboard:
	spieler=[]
	punktzahl=[]

	def addToBoard(pSpieler, pPunktzahl):
		leaderboard.spieler+=pSpieler
		leaderboard.punktzahl+=pPunktzahl
  
	def sortBoardByScoreDesc():
		for i in range(len(leaderboard.punktzahl)):
			for j in range(len(leaderboard.punktzahl)-1-i):
				if leaderboard.punktzahl[j] > leaderboard.punktzahl[j + 1]:
						leaderboard.punktzahl[j], leaderboard.punktzahl[j+1],leaderboard.spieler[j], leaderboard.spieler[j+1] = leaderboard.punktzahl[j+1], leaderboard.punktzahl[j],leaderboard.spieler[j+1], leaderboard.spieler[j]
      
	def deleteUnnecessaryEntries():
		while len(leaderboard.punktzahl)>10:
			leaderboard.punktzahl, leaderboard.spieler=leaderboard.punktzahl[1:], leaderboard.spieler[1:]

	def updateBoard(pSpieler, pPunktzahl):
		leaderboard.addToBoard(pSpieler, pPunktzahl)
		leaderboard.sortBoardByScoreDesc()
		leaderboard.deleteUnnecessaryEntries()