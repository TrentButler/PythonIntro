from trello import TrelloApi
import urllib2
import os
import json 
os.system("cls")

work = open('_DUMP.txt', 'w+')
_APIKEY = '1008880605d2b13135423f60b7239e65'
_APITOKEN = 'fd3966d052d60370943ec0bddb6cf5f709522c10981f8fad667b4bca60118df4'

_TRELLOAPI = TrelloApi(_APIKEY, token=_APITOKEN)
# print _TRELLOAPI.get_token_url('ClockHours', expires='30days', write_access=True)

# processThis = _TRELLOAPI.cards.get_action('57b47a1d722df06b05a38f7e')
processThis = _TRELLOAPI.cards.get('C1dvnzSR', actions='commentCard', fields=None)

def stripString(s):
    # NEEDS WORK
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '\n']
    returnString = ''
    for c in s:
        for CHARACTER in charList:
            if c == CHARACTER:
                returnString += c
    if len(returnString) < 9:
        return ""
    return returnString

def getdate(s):
    returnString = ''
    incrementor = 0
    for c in s:
        if incrementor >= 10:
            break
        returnString += c
        incrementor += 1
    if len(returnString) < 10:
        return ""
    return returnString



# mycard = urllib2.urlopen('https://api.trello.com/c/C1dvnzSR/69-trent-butler.json')
# work.write(mycard.read())

_from = '2017-04-01'
_to = '2017-04-19'



actiondict = {} # NEEDS WORK
for thing in processThis:
    if processThis.has_key('actions'):
        actiondict = processThis['actions']

clock_hours = []  # NEEDS WORK
for thing in actiondict:
    if thing.has_key('date'):
        hold_date = thing['date']
        _date = getdate(hold_date)
        if _date != _from:
            continue
        

        

    
processThis = {}
for _dict in processThis:
    # work.write(str(thing) + " " +  str(processThis[thing]) +"\n")
    if _dict.has_key('actions'):
        _dataDICT = _dict['actions']
        if _dataDICT.has_key('text'):
            # NEEDS WORK
            work.write(stripString(str(_dataDICT['text'])) + "\n")
            # work.write(_dataDICT['text'] + "\n")

work.close()
print "SUCCESS"
os.system("start _DUMP.txt")
