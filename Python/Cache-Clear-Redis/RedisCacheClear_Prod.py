import requests
import pickle
from requests.structures import CaseInsensitiveDict
import time
import json
import urllib3
urllib3.disable_warnings()

with open("mailing.txt", "w+") as file:
    file.truncate()
with open("cache.txt","w+") as file:
    file.truncate()
with open("caches.json", 'w+') as file:
    file.truncate()

headers = CaseInsensitiveDict()
url = "https://cache-prodauth-us.corp.hpicloud.net/cm/cache/clearall"
cache_response = requests.delete(url, headers=headers, verify=False)
print(cache_response.status_code)
if cache_response.status_code == 200:
    status = "Success"
    file = open("status.txt","w+")
    pickle.dump(status,file)
    file.close()
    print(status)
else:
    status = "Failed"
    file = open("status.txt","w+")
    pickle.dump(status,file)
    file.close()
    print(status)

count_url = "https://cache-prodauth-us.corp.hpicloud.net/cm/cache/"
cache_count = requests.get(count_url, verify=False)
cache_content = str(cache_count.content)


file = open("cache.txt", "w+")
file.write(cache_content)
file.close()
with open("cache.txt", 'r') as infile, open('caches.json', 'w+') as outfile:
    data = infile.read()
    data = data.replace("b'", "")
    data = data.replace("'", "")
    outfile.write(data)


with open("caches.json") as file:
    data = json.load(file)
