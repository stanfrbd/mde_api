import argparse
import inspect

from utils.api_request import show_token
from endpoints.machines.offboard import offboard_machine
from endpoints.machines.report import get_windows_servers_onboarding_status
from endpoints.tag.tag import add_tag, remove_tag

def mde_api_parse_args():

    parser = argparse.ArgumentParser(description='List machines, offboard or token')
    
    subparsers = parser.add_subparsers(dest='command')

    # Create the parser for the "token" command
    token_parse = subparsers.add_parser('token', help='Get token')

    # create the parser for the "machines" command
    machines_parser = subparsers.add_parser('machines', help='Perform actions on machines')
    machines_subparsers = machines_parser.add_subparsers(dest='subcommand')

    # create the argument for the "report" command
    machines_subparsers.add_parser('report', help='Generate Excel report')

    # create the parser for the "offboard" command
    offboard_parser = machines_subparsers.add_parser('offboard', help='Offboard machine')
    offboard_parser.add_argument('machineid', help='Machine ID')

    # create the parser for the "isolate" command
    isolate_parser = machines_subparsers.add_parser('isolate', help='Isolate machine')
    isolate_parser.add_argument('machineid', help='Machine ID')

    # create the parser for the "tag" command
    tag_parser = subparsers.add_parser('tag', help='Perform actions on tags')
    tag_subparsers = tag_parser.add_subparsers(dest='subcommand')

    tag_add_parser = tag_subparsers.add_parser('add', help='Add a tag to a machine')
    tag_add_parser.add_argument('--value', help='Tag value')
    tag_add_parser.add_argument('--machineid', help='Machine ID')
    tag_add_parser.add_argument('--input-file', help='Input file')
    
    tag_remove_parser = tag_subparsers.add_parser('remove', help='Remove a tag from a machine')
    tag_remove_parser.add_argument('--value', help='Tag value')
    tag_remove_parser.add_argument('--machineid', help='Machine ID')
    tag_remove_parser.add_argument('--input-file', help='Input file')

    # create the parser for the "indicators" command
    indicators_parser = subparsers.add_parser('indicators', help='Perform actions on indicators')
    indicators_subparsers = indicators_parser.add_subparsers(dest='subcommand')

    # create the parser for the "add" command
    indicators_add_parser = indicators_subparsers.add_parser('add', help='Add an indicator')
    indicators_add_parser.add_argument('indicator', help='Indicator')

    # create the parser for the "vulnerabilities" command
    vulnerabilities_parser = subparsers.add_parser('vulnerabilities', help='Perform actions on vulnerabilities')
    vulnerabilities_subparsers = vulnerabilities_parser.add_subparsers(dest='subcommand')

    # create the parser for the "get_devices" command
    get_devices_parser = vulnerabilities_subparsers.add_parser('get_devices', help='Get devices for a CVE')
    get_devices_parser.add_argument('cveid', help='CVE ID')

    # create the parser for the "users" command
    users_parser = subparsers.add_parser('users', help='Perform actions on users')
    users_subparsers = users_parser.add_subparsers(dest='subcommand')

    # create the parser for the "list" command
    list_parser = users_subparsers.add_parser('list', help='List all users')

    # create the parser for the "get" command
    get_parser = users_subparsers.add_parser('get', help='Get a user')
    get_parser.add_argument('userUpn', help='User UPN')

    # create the parser for the "software" command
    software_parser = subparsers.add_parser('software', help='Perform actions on software')
    software_subparsers = software_parser.add_subparsers(dest='subcommand')

    # create the parser for the "alerts" command
    alerts_parser = subparsers.add_parser('alerts', help='Perform actions on alerts')
    alerts_subparsers = alerts_parser.add_subparsers(dest='subcommand')

    return parser.parse_args()

# Check if function has arguments or not, and execute it following the case
def execute_function(func, args):
    if args is None:
        args = {}

    parameters = inspect.signature(func).parameters

    if any(p.default == inspect.Parameter.empty for p in parameters.values()):
        # Function takes arguments
        func(args)
    else:
        # Function does not take arguments
        func()

def dispatch_command(args):
    command_actions = {
        "machines": handle_machines_command,
        "vulnerabilities": handle_vulnerabilities_command,
        "users": handle_users_command,
        "software": handle_software_command,
        "alerts": handle_alerts_command,
        "indicators": handle_indicators_command,
        "tag": handle_tag_command,
        "token": show_token
    }

    # Get the function corresponding to the command, defaulting to None
    action_function = command_actions.get(args.command)

    # Call the function if it exists, otherwise parser will print an error
    if action_function:
        execute_function(action_function, args)

def handle_machines_command(args):
    sub_command_actions = {
        "report": get_windows_servers_onboarding_status,
        "offboard": offboard_machine
        # "isolate": # todo,
    }

    # Get the function corresponding to the command, defaulting to None
    action_function = sub_command_actions.get(args.subcommand)

    # Call the function if it exists, otherwise parser will print an error
    if action_function:
        execute_function(action_function, args)

def handle_vulnerabilities_command(args):
    print("Not yet implemented")

def handle_users_command(args):
    print("Not yet implemented")

def handle_software_command(args):
    print("Not yet implemented")

def handle_indicators_command(args):
    print("Not yet implemented")

def handle_alerts_command(args):
    print("Not yet implemented")

def handle_tag_command(args):
    sub_command_actions = {
        "remove": remove_tag,
        "add": add_tag,
    }

    # Get the function corresponding to the command, defaulting to None
    action_function = sub_command_actions.get(args.subcommand)

    # Call the function if it exists, otherwise parser will print an error
    if action_function:
        execute_function(action_function, args)
