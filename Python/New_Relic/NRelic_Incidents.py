import requests
import json
import pandas as pd
import os

if os.path.exists(r"D:\Users\ksi\Desktop\siva\Scripts\New_Relic\NRelic_Inc.csv"):
    print("Found the File NRelic_Inc.csv and attempting to delete.")
    os.remove(r"D:\Users\ksi\Desktop\siva\Scripts\New_Relic\NRelic_Inc.csv")
    print("Deleted the File NRelic_Inc.csv")
else:
    print("The file does not exist.. Proceeding Further")

api_token = 'NRAK-25ASG88WY8WEC5VCTPVGMFJQ2HR'
headers={'x-api-key':api_token}
url = 'https://api.newrelic.com/v2/alerts_incidents.json'
parameters = "only_open=true"
result = requests.get(url, headers=headers,  params=parameters)

data = result.json()
incident = data["incidents"]
inc_list = []
opened_list = []
incident_obj = {"Incident":inc_list, "Opened":opened_list}
for key in incident:
    inc_list.append(key["id"])
    opened_list.append(key["opened_at"])

f_result = pd.DataFrame.from_dict(incident_obj)
f_result.index += 1 
print("Please find the Open New Relic Incidents:")
print(f_result)
f_result.to_csv(r"D:\Users\ksi\Desktop\siva\Scripts\New_Relic\NRelic_Inc.csv")
file = pd.read_csv(r"D:\Users\ksi\Desktop\siva\Scripts\New_Relic\NRelic_Inc.csv",index_col=[0])
file.to_html("Table.htm")
mail_result = file.to_html()
