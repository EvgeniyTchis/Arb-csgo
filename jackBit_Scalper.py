import requests
import json



## gets all matches from the bookie
matchList = requests.get("https://sportservice.inplaynet.tech/api/sport/getheader/en")

## parses all current matches for csgo
## sport number for csgo is 63 on jackbit
matchList = json.loads(matchList.json())
matchList = matchList["EN"]["Sports"]["63"]["Regions"]["820"]["Champs"]

## get all match ids to query
matchString = ""
for champ in matchList:
    for match in matchList[champ]["GameSmallItems"]:
        matchString = matchString + "," + str(match)

##print(matchString)

## query for odds info
link = "https://sportservice.inplaynet.tech/api/prematch/getprematchgameall/en/94/?games=" + matchString
matchList = requests.get(link)
print(matchList.json())


