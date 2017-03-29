import os
class Application():
	def __init__(self):
		self.chrome = 'start chrome.exe'
		self.firefox = 'start firefox.exe'
		self.iExplorer = 'start iexplore.exe'
	
	def Open(self, arg):		
		if(arg == 1):
			os.system(self.chrome)
		elif(arg == 2):
			os.system(self.firefox)



b = Application()
b.Open(1)
