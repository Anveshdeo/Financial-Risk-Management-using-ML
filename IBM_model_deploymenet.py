import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "ZaR7nEvVl_NtUszS6kNfB0VUN_HKDhCyM3wNze10_LVD"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]



header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}



# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['x1','x2','x3','x4','x5','x6','x7','x8','r1','r2','r3','t1','t2','t3','t4','u1','u2','u3','q1','q2','p','s','v','w']], "values":[[0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,35,0,45000,36]]}]}



response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/e4f7a068-f004-4584-b30d-a145c8049bf0/predictions?version=2021-08-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=(response_scoring.json())
pred=print(predictions)
if (pred==0):
    print("The risk assessment is bad")
else:
    print("The risk assessment is good")