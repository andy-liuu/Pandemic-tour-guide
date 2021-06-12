import requests
import re

def destinations(country):
    result = requests.get("http://www.geonames.org/search.html?q="+country+"&country=")
    #print(result.status_code)

    src = result.content
    lines = src.splitlines()
    for i in range (53,58):
        lines[i].split()
        #print(lines[54])

        test = str(lines[i])
        try:
            found = re.search('html\">[^<](.*?)</a>', test).group(0)
            print()
            found = found[6:len(found)-4]
            print(found)
        except:
            print("fail")    

#destinations("canada") 