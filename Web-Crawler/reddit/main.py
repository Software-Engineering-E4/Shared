import json
import requests
import pandas as pd
from datetime import datetime

def get_user_data(filename):
    with open(filename) as file:
        data = json.load(file)
        return data["username"], data["password"],data["client_id"],data["secret_key"]


user_name, user_pass, CLIENT_ID, SECRET_KEY = get_user_data("user_data.json")
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': user_name,
    'password': user_pass

}
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN=res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'


res = requests.get('https://oauth.reddit.com/r/cancer/hot',
                 headers=headers, params={'limit':'100'})


#for post in res.json()['data']['children']:
#    print(post['data']['title'])

#df=pd.DataFrame()
df=[]
for post in res.json()['data']['children']:
    df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score'],

    })
for line in df:
    print(line)

