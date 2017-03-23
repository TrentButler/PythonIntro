from trello import TrelloApi
import urllib2 as URL
import os
import json
os.system("cls")

work = open('_DUMP.txt', 'w+')
_APIKEY = '1008880605d2b13135423f60b7239e65'
_APITOKEN = 'fd3966d052d60370943ec0bddb6cf5f709522c10981f8fad667b4bca60118df4'

_TRELLOAPI = TrelloApi(_APIKEY, token=_APITOKEN)
# print _TRELLOAPI.get_token_url('ClockHours', expires='30days', write_access=True)

processThis = _TRELLOAPI.cards.get_action('57b47a1d722df06b05a38f7e')

def stripString(s):
    # NEEDS WORK
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '-', '\n']
    returnString = ''
    for c in s:
        for CHARACTER in charList:
            if c == CHARACTER:
                returnString += c
    if len(returnString) < 11:
        return ""
    return returnString    
    


for _dict in processThis:
    # work.write(str(thing) + " " +  str(processThis[thing]) +"\n")
    if _dict.has_key('data'):
        _dataDICT = _dict['data']
        if _dataDICT.has_key('text'):
            # NEEDS WORK
            work.write(stripString(str(_dataDICT['text'])) + "\n")
            # work.write(_dataDICT['text'] + "\n")

work.close()
print "SUCCESS"
os.system("start _DUMP.txt")
