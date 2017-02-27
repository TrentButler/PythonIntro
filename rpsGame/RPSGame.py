from playerChoice import PlayerChoice
from dealerChoice import DealerChoice

class RPSGame:
	player = PlayerChoice()
	def __init__(self):
		self.data = []
	def RunGame(self, rpsInput):
		print("1.) Rock, 2.) Paper, 3.) Scissors")
		gameInput = rpsInput
		if gameInput is '1':
			self.player.pFSM.ChangeState('ROCK')
			self.player.Switch
		if gameInput is '2':
			self.player.pFSM.ChangeState('PAPER')
			self.player.Switch
		if gameInput is '3':
			self.player.pFSM.ChangeState('SCISSORS')
			self.player.Switch
		if gameInput is 'q':
			exit()

run = RPSGame()

while True:
	rpsGameInput = raw_input()
	run.RunGame(rpsGameInput)
	#print(str(run.player.pFSM.currentstate))
#print(str(run.player.pFSM.currentstate))
