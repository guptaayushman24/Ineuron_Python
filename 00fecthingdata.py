import requests
def fetchAndSavteToFile(url,path) :
    r = requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)
url="https://timesofindia.indiatimes.com/city/delhi"

fetchAndSavteToFile(url,"data/times.html")
# What ever data is stored in the times.html we need to organize the data

