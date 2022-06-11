import json
import os
import requests
import jwt
import time

client_id = "0oavclgbdPRVVg16S4h6"#0oa1ka16on25YMLck1d8"
OKTA_URL = "https://shield-databricks.okta.com"
issuer_url = f"{OKTA_URL}/oauth2/v1/token"


headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
    }

body = {
    "aud": issuer_url,
    "iss": client_id,
    "sub": client_id,
    "exp": int(time.time()) + 3600
}

pvt_file_path = "/Users/prajwal.shetty/Documents/okta_private_key"

with open(pvt_file_path, "r") as f:
    private_key = f.read()

token = jwt.encode(body, private_key, algorithm='RS256')

jwt_key = token#.decode()

params = {
    "grant_type": "client_credentials",
    "scope": "okta.users.read okta.apps.read okta.groups.read",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": jwt_key
    }

response = requests.post(issuer_url, headers=headers, params=params)

print(response)

USER_EMAIL = "fergal.walsh@databricks.com"#arjun.kaimaparambilrajan@databricks.com"

if response.status_code < 300:
    access_token = response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
    }
USER_URL = f"{OKTA_URL}/api/v1/users/{USER_EMAIL}"

USER_GROUP_URL = f"{USER_URL}/groups"
user_group_details = requests.get(USER_GROUP_URL, headers=headers)

if user_group_details.status_code < 300:
    user_group_details_json = user_group_details.json()
#print(user_group_details_json)
d = {}
okta_list = user_group_details_json
for item in okta_list:
    d[item.get('profile').get('name')] = item.get('_links').get('logo')[0]
print(d)
