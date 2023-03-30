import requests
import json

url = "https://csgoempire.com/api/v2/match-betting/flattened?page=1&per_page=100&provider_id=1"

headers = {"Host": "csgoempire.com",
"Cookie" : '__cf_bm=Ro.oBXuzbPE7zGLk.DnuU0LqnFGXhxmuEOf7MuBxunk-1680069217-0-AdAPV6ryQKCPCTsSQSLgc5eZOdcf4AA4BWnC7bG/RNfdQ8BQRNJw+Xvh4ZASlBAl/eBwi48Rnw1Q9TcIDc9Kjq80sM7MKhsxoyVlo70gdCZx4EeIiW+xOLeN3KY/FV61fKj/dOs1tC+cj2D3QF9WquawVEDaanWU2SGCMdkAYsvB; csgoempire=Qp9eOzcNEZcQ6uxKxRR0JFjR6g5DoPTVa7TLV1pJ; _ga=GA1.1.1618484810.1680069225; _ga_DHPQBHR4YL=GS1.1.1680069224.1.1.1680069290.0.0.0',
"Sec-Ch-Ua" : 'Not A(Brand";v="24", "Chromium";v="110"',
"Accept" : 'application/json, text/plain, */*',
"X-Empire-Device-Identifier": 'dd65b997-8543-4719-8ef3-769652ae58fc',
'Sec-Ch-Ua-Mobile' : '?0',
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
'Sec-Ch-Ua-Platform' : "Windows",
'Sec-Fetch-Site' : 'same-origin',
'Sec-Fetch-Mode' : 'cors',
'Sec-Fetch-Dest' : 'empty',
'Referer' : 'https://csgoempire.com/match-betting',
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'en-US,en;q=0.9'}

matchList = requests.get(url, headers=headers)
matchList = json.dumps(matchList.json())
matchList = json.loads(matchList)

lastPage = matchList["last_page"]
print(lastPage)
matchPages = []

matchPages.append(matchList)
print(matchPages)
for i in range(2, lastPage):
    url = "https://csgoempire.com/api/v2/match-betting/flattened?page=" + str(i) + "&per_page=100&provider_id=1"
    matchList = requests.get(url, headers=headers)
    matchList = json.dumps(matchList.json())
    matchList = json.loads(matchList)
    matchPages.append(matchList)



print(matchPages)

