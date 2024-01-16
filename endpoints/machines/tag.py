import json

from utils.api_request import make_api_request


def add_tag(args):
    if args.input_file:
        add_tag_for_multiple_machines(args)
        return

    machine_id = args.machineid
    url = "https://api.securitycenter.microsoft.com/api/machines/{}/tags".format(machine_id)
    body = {
        "Value": args.value,
        "Action": "Add"
    }

    try:
        response = make_api_request('POST', url, body)
        json_response = json.loads(response.content)
        print("Successfully tagged machine {} ({}) with value '{}'.".format(str(json_response["computerDnsName"]), machine_id, args.value))
    except Exception as err:
        print("Unable to tag: {}".format(str(err)))

    with open("tag.json", "w") as f:
        f.write(response.text)


def remove_tag(args):
    if args.input_file:
        remove_tag_for_multiple_machines(args)
        return

    machine_id = args.machineid
    url = "https://api.securitycenter.microsoft.com/api/machines/{}/tags".format(machine_id)
    body = {
        "Value": args.value,
        "Action": "Remove"
    }

    try:
        response = make_api_request('POST', url, body)
        json_response = json.loads(response.content)
        print("Successfully untagged machine {} ({}) with value '{}'.".format(str(json_response["computerDnsName"]), machine_id, args.value))
    except Exception as err:
        print("Unable to tag: {}".format(str(err)))

    with open("tag.json", "w") as f:
        f.write(response.text)


def add_tag_for_multiple_machines(args):
    url = "https://api.securitycenter.microsoft.com/api/machines/AddOrRemoveTagForMultipleMachines"

    with open(args.input_file, "r") as f:
        machine_ids = [line.strip() for line in f]

    body = {
        "Value": args.value,
        "Action": "Add",
        "MachineIds": machine_ids
    }

    try:
        response = make_api_request('POST', url, body)
        print("Successfully tagged {} machines with value '{}'.".format(len(machine_ids), args.value))
    except Exception as err:
        print("Unable to tag: {}".format(str(err)))

    with open("tag.json", "w") as f:
        f.write(response.text)


def remove_tag_for_multiple_machines(args):
    url = "https://api.securitycenter.microsoft.com/api/machines/AddOrRemoveTagForMultipleMachines"

    with open(args.input_file, "r") as f:
        machine_ids = [line.strip() for line in f]

    body = {
        "Value": args.value,
        "Action": "Remove",
        "MachineIds": machine_ids
    }

    try:
        response = make_api_request('POST', url, body)
        print("Successfully untagged {} machines with value '{}'.".format(len(machine_ids), args.value))
    except Exception as err:
        print("Unable to untag: {}".format(str(err)))

    with open("tag.json", "w") as f:
        f.write(response.text)
