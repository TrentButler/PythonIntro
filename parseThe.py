import os
import urllib2
import fileinput
import json
os.system('color 0a') #app color

eXport = open('export.txt', 'w+')
result = open('result.txt', 'w+')
cOunt = 0



# Display
print("This program looks for: \n")
print("- How many times 'the' is used in a webpage")
print("- What line it was used in")
print("\n \n")

#user input
iNput = raw_input("Input Webpage ~>> ")


#get webpage from user input
page = urllib2.urlopen(iNput)

#pull info from webpage/ export to text file
eXport.write(page.read()) 


#look for 'the' in the file
for line in fileinput.input('export.txt'):
	if ' the ' in line:
		cOunt + 1
		
		#result.write("count: " count)
		result.write("string found was: " + line)
		

os.startfile('C:\\Users\\trent.butler\\Desktop\\Python Intro\\result.txt')
raw_input()

#help = [{'count:' cOunt, 'string found:' line}]
#parsed_json = json.loads(help)
#result.write(json.dumps(parsed_json)






#export what was found to 'result.txt'

#os.startfile(result.txt) something like that.....
#os.startfile('C:\\Users\\trent.butler\\Desktop\\Python Intro\\result.txt')