import json
import requests

from utils.api_request import read_secrets, get_token

# disable ssl warning in case of proxy like Zscaler which breaks ssl...
requests.packages.urllib3.disable_warnings()

# Offboard a machine using its ID
def offboard_machine(args):
    machine_id = args.machineid
    secrets = read_secrets()
    token = get_token(secrets)

    headers = { 
        'Content-Type': 'application/json',
        'Accept':'application/json',
        'Authorization': "Bearer {}".format(token)
    }

    body = {
        'Comment': 'Offboard machine by automation',
    }

    proxies = { 'http': secrets['proxyUrl'], 'https': secrets['proxyUrl'] }

    url = "https://api.securitycenter.microsoft.com/api/machines/{}/offboard".format(machine_id)

    try:
        response = requests.post(url, json=body, headers=headers, proxies=proxies, verify=False)
        json_response = json.loads(response.content)
    
    except Exception as err:
        print("Unable to proceed to offboarding request: {}".format(str(err)))

    with open("offboard.json", "w") as f:
        f.write(response.text)
    
    print(json.dumps(json_response, indent=4))