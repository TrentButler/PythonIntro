import html
import requests
import os

os.system("color 0a")

print("\n \n")
print("Grand Theft Auto V cheat searcher \n")
print("\n \n")

iNput = raw_input("Search ~>> ")

pullPage = requests.get("http://www.cheatcc.com/ps4/grandtheftauto5cheatscodes.html")

pushPage = html.fromstring(pullPage.content)


cheatName = tree.xpath('//b/text()')
cheatCode = tree.xpath('//p/text()')




print 'CHEAT NAME: ' , cheatName
print 'CHEAT CODE: ' , cheatCode


raw_input()