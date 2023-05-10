class leaderboard:
	spieler=[]
	punktzahl=[]
	
	def addToBoard(pSpieler, pPunktzahl):
		spieler+=pSpieler
		punktzahl+=pPunktzahl
	def sortBoardByScore():
		save=0
		for score in punktzahl:
			for x in punktzahl:
				if score == x:
					pass
			