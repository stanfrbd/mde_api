import json
import requests

# disable ssl warning in case of proxy like Zscaler which breaks ssl...
requests.packages.urllib3.disable_warnings()

# Read secrets from "secrets.json"
def read_secrets():
    with open('secrets.json') as f:
        secrets = json.load(f)
    if not (key in secrets for key in ['tenantId', 'appId', 'appSecret']):
        raise ValueError('Error: Invalid secrets file')
    return secrets

# Make Post request to get AAD Token
def get_token(secrets):

    url = "https://login.microsoftonline.com/{}/oauth2/token".format(secrets['tenantId'])

    resourceAppIdUri = 'https://api.securitycenter.microsoft.com'

    body = {
        'resource': resourceAppIdUri,
        'client_id': secrets['appId'],
        'client_secret': secrets['appSecret'],
        'grant_type': 'client_credentials'
    }

    proxies = { 'http': secrets['proxyUrl'], 'https': secrets['proxyUrl'] }

    try:
        response = requests.post(url, data=body, proxies=proxies, verify=False)
        json_response = json.loads(response.content)
    except Exception as err:
        print("Error: " + str(err))
    try:
        aad_token = json_response["access_token"]
    except:
        print("Error: Unable to retrieve token")
        aad_token = "invalid"
    return aad_token

def show_token():
    print("\nHere is your JWT token, test it here: https://jwt.ms/\n")
    print(get_token(read_secrets()))
    print("")