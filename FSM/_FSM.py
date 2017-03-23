class _FSM:
	

	def __init__(self):
		self.data = []
		self.states = {}
		self.transitions = {}
		self.currentstate = None
		self.stopstate = None
		self.startstate = None

	def AddState(self,addState):
		stateKey = str(addState)
		if stateKey not in self.states:
			self.states[stateKey] = addState

	def AddTransition(self, stateFrom, stateTo):
		transitionKey = str(stateFrom) + "->" + str(stateTo)
		Transition = (stateFrom,stateTo)
		if transitionKey not in self.transitions:
			self.transitions[transitionKey] = Transition

	def ChangeState(self, stateTo):
		transitionKey = str(self.currentstate) + "->" + str(stateTo)
		stateKey = str(stateTo)
		if transitionKey in self.transitions:
			self.currentstate = self.states[stateKey]

	def StartMachine(self,startState):
		stateKey = str(startState)
		if stateKey in self.states:
			self.currentstate = startState

	def _getcurrent(self):
		return self.currentstate