from utils.api_request import make_api_request

def isolate(args):
    machine_id = args.machineid
    url = f"https://api.securitycenter.microsoft.com/api/machines/{machine_id}/isolate"

    body = {
        "Comment": "Isolate machine due to alert",
        "IsolationType": "Full"
    }
    response = make_api_request(url, "POST", json=body)
    
    if response.status_code == 200:
        print("Machine isolated successfully.")
    else:
        print("Failed to isolate machine.")
