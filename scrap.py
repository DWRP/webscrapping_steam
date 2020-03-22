import requests
from bs4 import BeautifulSoup

with open("links.txt","w") as links:
    for page in range(89):
        print(page)
        data = requests.get("https://store.steampowered.com/specials#p=%d&tab=TopSellers"%page)
        soup = BeautifulSoup(data.content,"html.parser")

        table = soup.findAll("a",{"class":"tab_item"})

        for row in table:
            desc = row.contents[3].find("div",{"class":"discount_pct"})
            desc_atual = str(desc.text).replace("-","").replace("%","")
            if (int(desc_atual)>=75):
                links.write(row.attrs['href']+";"+desc_atual+"\n")
        
        print("finish")
