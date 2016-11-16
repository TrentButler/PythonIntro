import os
import urllib2

getWebpage = urllib2.urlopen('https://www.youtube.com/watch?v=cd_YsXGYsbo')
page = getWebpage.read()

outPut = open('output.txt', 'w+')
outPut.write(page)

result = open("result.txt", "w+")

for line in outPut:
	if 'import' in line:
		result.write("Found: ")
		result.write(line)
	if 'jazz' in line:
		result.write("Found: ")
		result.write(line)
	if 'youtube' in line:
		result.write("Found: ")
		result.write(line)

		
endFile = True
while endFile is True:
	
	work = outPut.readline
	
	if 'jazz' in work:
		result.write(work)
		print work
		endFile = False
		
	if 'youtube' in work:
		result.write(work)
		print work
		endFile = False
		
		
	
outPut.close()
result.close()	


# Its a start...
# Research on how to loop over txt files more