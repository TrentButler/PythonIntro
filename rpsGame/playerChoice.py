from classFSM.FSM import FiniteStateMachine

class PlayerChoice:
	pFSM = FiniteStateMachine()
	def __init__(self):
		self.pFSM.AddState('INIT')
		self.pFSM.AddState('ROCK')
		self.pFSM.AddState('PAPER')
		self.pFSM.AddState('SCISSORS')
		self.pFSM.AddTransition('INIT', 'ROCK')
		self.pFSM.AddTransition('INIT', 'PAPER')
		self.pFSM.AddTransition('INIT', 'SCISSORS')
		self.pFSM.AddTransition('ROCK', 'INIT')
		self.pFSM.AddTransition('PAPER', 'INIT')
		self.pFSM.AddTransition('SCISSORS', 'INIT')
		self.pFSM.StartMachine('INIT')
	def Switch():
		if self.pFSM.currentstate is 'ROCK':
			print(str(self) + "ROCK")
			self.pFSM.ChangeState('INIT')
		if self.pFSM.currentstate is 'PAPER': 
			print(str(self) + "PAPER")
			self.pFSM.ChangeState('INIT')
		if self.pFSM.currentstate is 'SCISSORS':
			print(str(self) + "SCISSORS")
			self.pFSM.ChangeState('INIT')