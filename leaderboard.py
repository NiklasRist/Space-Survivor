class leaderboard:
	spieler=["Gerald","Alf","Hans","Ralf","Kai","Harry"]
	punktzahl=[5,7,1,3,4,6]

	def addToBoard(pSpieler, pPunktzahl):
		leaderboard.spieler+=pSpieler
		leaderboard.punktzahl+=pPunktzahl
	def sortBoardByScore():
		for i in range(len(leaderboard.punktzahl)):
			for j in range(len(leaderboard.punktzahl)-1-i):
				if leaderboard.punktzahl[j] > leaderboard.punktzahl[j + 1]:
						leaderboard.punktzahl[j], leaderboard.punktzahl[j+1],leaderboard.spieler[j], leaderboard.spieler[j+1] = leaderboard.punktzahl[j+1], leaderboard.punktzahl[j],leaderboard.spieler[j+1], leaderboard.spieler[j]


			
