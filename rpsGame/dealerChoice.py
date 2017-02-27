from classFSM.FSM import FiniteStateMachine

class DealerChoice:
	dFSM = FiniteStateMachine()
	def __init__(self):
		self.dFSM.AddState('INIT')
		self.dFSM.AddState('ROCK')
		self.dFSM.AddState('PAPER')
		self.dFSM.AddState('SCISSORS')
		self.dFSM.AddTransition('INIT', 'ROCK')
		self.dFSM.AddTransition('INIT', 'PAPER')
		self.dFSM.AddTransition('INIT', 'SCISSORS')
		self.dFSM.AddTransition('ROCK', 'INIT')
		self.dFSM.AddTransition('PAPER', 'INIT')
		self.dFSM.AddTransition('SCISSORS', 'INIT')
		self.dFSM.StartMachine('INIT')
	def Switch(CurrentState):
		if self.eFSM.currentstate is 'ROCK':
			print(str(self) + "ROCK")
			self.eFSM.ChangeState('INIT')
		if self.eFSM.currentstate is 'PAPER': 
			print(str(self) + "PAPER")
			self.eFSM.ChangeState('INIT')
		if self.eFSM.currentstate is 'SCISSORS':
			print(str(self) + "SCISSORS")
			self.eFSM.ChangeState('INIT')