#install BeautifulSoup
#install urllib.request
#before running

#delete word none, delete space
#sed -i 's/None//g' nameoftxtfile.txt
#sed -ri '/^\s*$/d' nameoftxtfile.txt

from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open('whiteroom.txt', 'a')
a = 2

for i in range(3):
    websiteCode = urlopen("https://www.shutterstock.com/search/white+rooms?kw=shutterstock&c3apidt=p11277540745&ds_rl=1243391&gclid=EAIaIQobChMIjrbl_aX57AIVkobACh2WfgHgEAAYASAAEgLXP_D_BwE&gclsrc=aw.ds&page=2"+str(i)).read()
    soup = BeautifulSoup(websiteCode)
    images = []
    images = soup.findAll('img')

    for image in images:
        print(image.get('src'))
        x = image.get('src')
        f.write(str(x))
        f.write('\n')
f.close()
