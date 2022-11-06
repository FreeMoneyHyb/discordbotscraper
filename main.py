import threading, json, base64, os, sys
import requests
 
#Edited By Skid1337#1941 Consept By IHateThisGame#6353

Opt = input('[?] Add Search Option Y/N : ')
if Opt == "n":
  howmany = input('[?] How many do u want daddy?: ')
  request = requests.get(f'https://top.gg/api/client/entities/search?platform=discord&entityType=bot&amount={howmany}&newSortingOrder=RECENTLY_CREATED')  
  
  jsonload = request.json().get('results')
  for loopshit in jsonload:
     imgay = loopshit['id']
     namez = loopshit['name']
     poopsex = loopshit['description']
     print(f'[!] **{namez}** Has Been Added')
     print(f'[!] (About {namez}): {poopsex}')
     with open(f'{"servers.txt"}', 'a+') as f:
       f.write(f'{imgay}\n')
     with open(f'{"serversWinvite.txt"}', 'a+') as f:
       f.write(f'https://discord.com/oauth2/authorize?client_id={imgay}&permissions=0&scope=applications.commands%20bot\n')
else:
  ammount = input('[?] How many do u want daddy?: ')
  search = input('[?] Enter A Bot Topic : ')
  req = requests.get(f'https://top.gg/api/client/entities/search?platform=discord&entityType=bot&amount={ammount}&skip=0&nsfwLevel=1&newSortingOrder=TOP&query={search}&sort=top&isMature=false')  
  
  jsonload = req.json().get('results')
  for popbob in jsonload:
     notgay = popbob['id']
     namex = popbob['name']
     print(f'[!] **{namex}** Has Been Added')
     with open(f'{"servers.txt"}', 'a+') as f:
       f.write(f'{notgay}\n')
     with open(f'{"serversWinvite.txt"}', 'a+') as f:
       f.write(f'https://discord.com/oauth2/authorize?client_id={notgay}&permissions=0&scope=applications.commands%20bot \n')
       
 
