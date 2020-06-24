from bs4 import BeautifulSoup
import requests

search=input("Enter Seach Keyword : ")
params={'q':search}
r=requests.get("https://www.bing.com/search",params=params)

soup=BeautifulSoup(r.text,"html.parser")
results=soup.find("ol",{"id":"b_results"})
print(results)

links=results.findAll("li",{"class":"b_algo"})

for item in links:
    itemname=item.find("a").text
    item_href=item.find("a").attrs["href"]

    if itemname and item_href:
        print(itemname)
        print(item_href)
        print("Summary : ",item.find("a").parent.parent.find("p").text)
