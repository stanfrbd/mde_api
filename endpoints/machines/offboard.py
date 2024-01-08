import json

from utils.api_request import make_api_request

# Offboard a machine using its ID
def offboard_machine(args):

    machine_id = args.machineid

    body = {
        'Comment': 'Offboard machine by automation',
    }

    url = "https://api.securitycenter.microsoft.com/api/machines/{}/offboard".format(machine_id)

    try:
        response = make_api_request('POST', url, body)
        json_response = json.loads(response.content)
    
    except Exception as err:
        print("Unable to proceed to offboarding request: {}".format(str(err)))

    with open("offboard.json", "w") as f:
        f.write(response.text)
    
    print(json.dumps(json_response, indent=4))