#!/usr/bin/env python3

# Stanislas M. 2023-12-26

"""
This script is a command-line interface for performing various actions on machines, indicators, vulnerabilities, users, software, and alerts using the MDE API.

usage: mde_api.py [-h] {token,machines,indicators,vulnerabilities,users,software,alerts} ...

positional arguments:
  {token,machines,indicators,vulnerabilities,users,software,alerts}
    token               Get token
    machines            Perform actions on machines
    indicators          Perform actions on indicators
    vulnerabilities     Perform actions on vulnerabilities
    users               Perform actions on users
    software            Perform actions on software
    alerts              Perform actions on alerts

options:
  -h, --help            show this help message and exit
"""

from utils.argument_parser import mde_api_parse_args, dispatch_command

def main():
    """
    The main function of the script.
    It parses the command-line arguments and dispatches the appropriate command.
    """
    args = mde_api_parse_args()
    dispatch_command(args)

if __name__ == '__main__':
    try: 
        main()   
    except Exception as err:
        print("General error: {} check your secrets file and App Registration.".format(str(err))) 
        exit(1)
