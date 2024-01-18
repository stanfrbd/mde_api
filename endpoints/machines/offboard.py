import json

from utils.api_request import make_api_request

# Offboard a machine using its ID
def offboard_machine(args):
    """
    Offboards a machine by sending a POST request to the Microsoft Security Center API.

    Args:
        args (object): The arguments passed to the function.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the offboarding request.

    """

    if args.input_file:
        offboard_multiple_machines(args)
        return
    elif args.machineid:
        offboard_unique_machine(args.machineid)
    
def offboard_unique_machine(machine_id):

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

def offboard_multiple_machines(args):
    with open(args.input_file, "r") as f:
        machine_ids = [line.strip() for line in f]
    
    for machine_id in machine_ids:
        offboard_unique_machine(machine_id)
    
