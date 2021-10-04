import requests
from requests.structures import CaseInsensitiveDict
import time
import json
import urllib3
urllib3.disable_warnings()

with open("mailing.txt", "w+") as file:
    file.truncate()
with open("cache.txt","w+") as file:
    file.truncate()
with open("caches.json", "w+") as file:
    file.truncate()

headers = CaseInsensitiveDict()
caches=['baseCache','services/cache/DM_Cache','services/cache/PSTCache','services/cache/PerfCache','services/cache/ProdCache']
index = 0
base_url = "https://cache-uat3auth-us.corp.hpicloud.net/cm/cache/clear?cache="
count_url = "https://cache-uat3auth-us.corp.hpicloud.net/cm/cache/"


while index <= 4:
    cache_url = base_url+caches[index]
    print("Clearing cache for the URL:", cache_url)
    cache_response = requests.delete(cache_url, headers=headers, verify=False)
    if cache_response.status_code == 200:
        print("Status for ", caches[index], ": Success ", cache_response.status_code)
    else:
        print("Status for ", caches[index], ": Failed ", cache_response.status_code)
    index += 1
    time.sleep(5)

cache_count = requests.get(count_url, verify=False)
cache_content = str(cache_count.content)
#print(cache_content)

file = open("cache.txt", "w+")
file.write(cache_text)
file.close()
with open("cache.txt", 'r') as infile, open('caches.json', 'w+') as outfile:
    data = infile.read()
    data = data.replace("b'", "")
    data = data.replace("'", "")
    outfile.write(data)


with open("caches.json") as file:
    data = json.load(file)

mail_dict = {}
for key in caches:
    if key in data:
        print(key,"=", data[key])
        mail_dict[key] = data[key]

with open("mailing.txt", 'w+') as f:
    for key, value in mail_dict.items():
        f.write('%s:%s\n' % (key, value))


