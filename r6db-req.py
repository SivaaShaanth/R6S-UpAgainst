import requests
import json
from nested_lookup import nested_lookup
from bs4 import BeautifulSoup
from os import makedirs
from os.path import join, basename
from lib2to3.fixes.fix_execfile import FixExecfile
soup=BeautifulSoup(open("/Users/sivaashaanth/R6DB/a0b69c84ebc00c54c94d/SivaaShaanth.github.io/index.html"),"html.parser")
#print(soup.prettify())
def modifyhtml(datatxt,i,name):
    #print(datatxt)
    rankidname="r"+str(i)
    playeridname="p"+str(i)
    div=soup.find(id=rankidname)
    for img in div.findAll('img'):
        imgname= "new_ranks/"+str(datatxt)+".png"
        img['src'] = imgname
    div=soup.find(id=playeridname)
    div.string=name
    #print(soup)
RESULTS_DIR = 'UserRanks'
IMG_TEXT_DIR= 'playernames/players.txt'
makedirs(RESULTS_DIR, exist_ok=True)
with open(IMG_TEXT_DIR,'r') as playerFile:
    playerString=playerFile.read()
    playerList=playerString.split("\n")
    i=1
    for name in playerList:
        print(name)
        r = requests.get('https://r6db.com/api/v2/players?name='+name+'&platform=pc&exact=false',headers={"x-app-id":"d951c9f8-c6d6-4277-b9cc-1b5de2fbda81"})
        if r.status_code==200 :
            res=json.loads(r.text)
            #print(res)
            if res:
                pid=res[0]['id']
                print(pid)
                x = requests.get('https://r6db.com/api/v2/players/'+pid,headers={"x-app-id":"d951c9f8-c6d6-4277-b9cc-1b5de2fbda81"})
                finalres=json.loads(x.text)
                max_rank=max(nested_lookup('max_rank', finalres))
                tempFileName=str(i)+".txt"
                jpath = join(RESULTS_DIR,tempFileName)
                
                with open(jpath, 'w+') as f:
                    #datatxt = finalres['rank']['apac']['max_rank']
                    #print(datatxt)
                    if(len(str(max_rank))>0):
                        print("Wrote", len(str(max_rank)), "bytes to", jpath)
                        f.write(str(max_rank))
                        if(i<6):
                            modifyhtml(max_rank,i,name)
                        #print(soup)
                    else:
                        f.write("0")
                i=i+1
    with open("/Users/sivaashaanth/R6DB/a0b69c84ebc00c54c94d/SivaaShaanth.github.io/index.html", "w") as file:
        file.write(str(soup))
        #exec(open("./SFileUploader.py").read())