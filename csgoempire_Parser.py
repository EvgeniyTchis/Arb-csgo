import json


data = ""

with open('csgoempire_testData.txt', 'r') as file:
    data = file.read()

data = json.loads(data)

result = []
for p in data:
    curpage = p

    teamList = []
    teamj = curpage["data"]["teams"]
    for td in teamj:
        team = []
        team.append(teamj[td]["id"])
        team.append(teamj[td]["name"])
        teamList.append(team)


    matchList = []
    matchj = curpage["data"]["matches"]
    for md in matchj:
        if matchj[md]["game"] == "cs-go":
            match = []
            match.append(matchj[md]["id"])
            match.append(matchj[md]["team1_id"])
            match.append(matchj[md]["team2_id"])
            matchList.append(match)


    selectionList = []
    selectionj = curpage["data"]["selections"]
    for sd in selectionj:
        selection = []
        selection.append(selectionj[sd]["match_id"])
        selection.append(selectionj[sd]["position"])
        selection.append(selectionj[sd]["odds"])
        selectionList.append(selection)


    fullSelectionList = []
    for s1 in selectionList:
        selection2 = []
        if s1[1] == 0:
            for s2 in selectionList:
                if s1[0] == s2[0] and s2[1] == 1:
                    selection2.append(s1[0])
                    selection2.append(float(s1[2]))
                    selection2.append(float(s2[2]))
                    fullSelectionList.append(selection2)

    entryList = []
    for m in matchList:
        entry = [None] * 4
        for t in teamList:
            if t[0] == m[1]:
                entry[0] = t[1]
            elif t[0] == m[2]:
                entry[1] = t[1]
        
        for s in fullSelectionList:
            if m[0] == s[0]:
                entry[2] = s[1]
                entry[3] = s[2]
        entryList.append(entry)

    result = result + entryList

print(result)




