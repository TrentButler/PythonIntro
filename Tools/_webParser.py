# NEEDS WORK
from _htmlParser import _HTML_Parser
import urllib2
import os

os.chdir("C:\\Users\\trent.butler\\Documents\\GitHub\\PythonIntro\\Tools")  # CHANGE THE CURRENT DIRECTORY TO '_DUMP'

def writeToFile(fileName, text, data):
    
    _file = open(fileName + ".txt", "a")
    _file.write(text + " (" + str(data) + ")" + "\n")
    _file.close()


# user input
iNput = raw_input("Input Webpage ~>> ")
# get webpage from user input
page = urllib2.urlopen(iNput)

parse = _HTML_Parser()
parse.set_up("test", writeToFile)
parse.feed(page.read())
print "SUCCESS"
