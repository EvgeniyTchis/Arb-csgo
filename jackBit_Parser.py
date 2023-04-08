import json
import ast




def findTeamByID(id, tList):

    for t in tList:
        if t[0] == id:
            return t[1]
        
    return "Null Team"








data = ""

with open('jackBit_testData.txt', 'r') as file:
    data = file.read()

data = json.loads(data)

teamData = data["teams"]
teamData = json.loads(teamData)
teamList = []
for td in teamData:
    team = []
    team.append(td["ID"])
    team.append(td["Name"])
    teamList.append(team)

gameData = data["game"]
gameData = gameData[:-2] + "]"
gameData = json.loads(gameData)

gameList = []
for gd in gameData:
    try:
        game = []
        game.append(gd["t1"])
        game.append(gd["t2"])
        for id in gd["ev"]["3764"]:
            game.append(gd["ev"]["3764"][id]["coef"])
        gameList.append(game)
    except:
        print("json error")


newGame = []
for g in gameList:
    ng = []
    ng.append(findTeamByID(g[0], teamList))
    ng.append(findTeamByID(g[1], teamList))
    ng.append(g[2])
    ng.append(g[3])
    newGame.append(ng)

print(newGame)
##print(json.dumps(gameData, indent=4))

