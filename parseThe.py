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
	line.replace("<a >", "")
	line.replace("<p>", "")
	line.replace("<header>", "")
	line.replace("<head>", "")
	line.replace("<br>","")
	line.replace("<body>", "")
	line.replace("<script>", "")
	line.replace("<title>", "")
	
	line.replace("</a>", "")
	line.replace("</p>", "")
	line.replace("</header>", "")
	line.replace("</head>", "")
	line.replace("</br>","")
	line.replace("</body>", "")
	line.replace("</script>", "")
	line.replace("</title>", "")
	
	#line.replace("  ", "")
	
	if ' the ' in line:
		cOunt +=1
		#substring?
		#result.write("count: " cOunt)
		result.write("\nstring found was: \n" + line)
		result.write("\n")
		#I need a more specific if statement?
	
	if ' Redtrent ' in line:
		cOunt +=1
		result.write("string found was: \n" + line)
		result.write("\n")
		#USED WHEN PARSING MY FACEBOOK PAGE....
		
	if 'Step ' in line:
		cOunt +=1
		result.write("string found was: \n" + line)
		result.write("\n")
	
	if 'step ' in line:
		cOunt +=1
		result.write("string found was: \n" + line)
		result.write("\n")
	
	if 'step' in line:
		cOunt +=1
		result.write("string found was: \n" + line)
		result.write("\n")
	
	if 'Step' in line:
		cOunt +=1
		result.write("string found was: \n" + line)
		result.write("\n")


result.close() #DO NOT FORGET TO CLOSE THE TEXT FILES.....
os.startfile('result.txt')
print('count:' , cOunt)


#help = [{'count:' cOunt, 'string found:' line}]
#parsed_json = json.loads(help)
#result.write(json.dumps(parsed_json)






#export what was found to 'result.txt'

#os.startfile(result.txt) something like that.....
#os.startfile('C:\\Users\\trent.butler\\Desktop\\Python Intro\\result.txt')