import itertools
from urlparse import urljoin
import requests
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
import pickle
import sys
import urllib3
urllib3.disable_warnings()

name1 = "url_status"
name2 = "cp_code_status"

filename1 = "%s.txt" %name1
with open(filename1, "w+") as file:
    file.truncate()

filename2 = "%s.txt" %name2
with open(filename2, "w+") as file:
    file.truncate()

#---------------------------------------------Choice of Purge -------------------------------------------------------#

Choice1 = str(sys.argv[1])
#---------------------------------------Converting Text File into seperate URLs/CP CODE for AKAMAI-----------------------------#

with open('purge_url.txt','r') as f:
	url_list=[]
	for line in f:
            strip_lines = line.strip()
	    listli = strip_lines.split()
	    url_list.append(listli)

Purge_urls = list(itertools.chain(*url_list))
print("Please find the Objects to be Purged")
print(Purge_urls)
payload = {"Objects":Purge_urls}
with open("mailing.json", "w+") as outfile: 
    json.dump(payload, outfile)
# -----------------------------------Separating CP CODES & URLS --------------------------------------------#
cpcodes = []
urls = []
for item in range(len(Purge_urls)):
    res = str.isdigit(Purge_urls[item])
    if res == True:
        cpcode = int(Purge_urls[item])
        cpcodes.append(cpcode)
    else:
        urls.append(Purge_urls[item])
 

#-------------------------------URLS has been separated and ready to purge--------------------------------------------#
# -----------------------------------------------Edge Grid Auth Configure -----------------------------------------#
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'method': 'post'}
diagnostic_url = 'diagnostic-tools/v2/ghost-locations/available'

s = requests.Session()
edgerc = EdgeRc('/home/wcsuser/.edgerc')
section = 'purge'
baseurl = 'https://%s' % edgerc.get(section, 'host')
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)




def purging(url,datum,name):
    response = s.post(url,data=datum,headers=headers)
    print(response.status_code)
    print(response.content)
    if response.status_code == 201:
        print("akamai Request accepted for %s" %name)
        status = "Success"
        filename = "%s.txt" %name
        file = open(filename,"wb")
        #file = open('%s.csv' % name, 'wb')
        pickle.dump(status,file)
        file.close()
    else:
        print("akamai  request rejected for %s" %name)
        status = "Failed"
        filename = "%s.txt" %name
        file = open(filename,"wb")
        pickle.dump(status,file)
        file.close()


api_url1 = '/ccu/v3/'+Choice1+'/url'
complete_url = urljoin(baseurl,api_url1)
api_url2 = '/ccu/v3/'+Choice1+'/cpcode'
complete_cpcode_url = urljoin(baseurl,api_url2)
payload1 = {"objects": urls}
payload2 = {"objects": cpcodes}
data1 = json.dumps(payload1)
data2 = json.dumps(payload2)

if len(urls) > 0:
    url_purging = purging(url=complete_url,datum=data1,name=name1)
else:
    print("No URLs Specified!!")

if len(cpcodes) > 0:
    cp_purging = purging(url=complete_cpcode_url,datum=data2,name=name2)
else:
    print("No CPCODES Specified!!")
    
