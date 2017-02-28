import Python-Intro.classFSM

fsm = FiniteStateMachine()
fsm.AddState("INIT")
fsm.AddState("IDLE")
fsm.AddState("EXIT")
fsm.AddTransition("INIT", "IDLE")
fsm.AddTransition("IDLE", "EXIT")
fsm.StartMachine("INIT")
print(str(fsm.currentstate))
raw_input()