# mde_api

This script is a wrapper for Microsoft Defender for Endpoint API.

For a better understanding, refer to the official Microsoft Defender for Endpoint API documentation: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/api/exposed-apis-list?view=o365-worldwide

## Install dependencies

You might want to create a [`venv`](https://docs.python.org/3/library/venv.html) before installing the dependencies.

```
pip install -r requirements.txt
```

## Usage

```
usage: mde_api.py [-h] {token,machines,indicators,vulnerabilities,users,software} ...

List machines, offboard or token

positional arguments:
  {token,machines,indicators,vulnerabilities,users,software}
    token               Get token
    machines            Perform actions on machines
    indicators          Perform actions on indicators
    vulnerabilities     Perform actions on vulnerabilities
    users               Perform actions on users
    software            Perform actions on software

options:
  -h, --help            show this help message and exit
```

# Quick start

Follow the instructions to get a working App Registration in Azure Entra ID.
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/api/exposed-apis-create-app-webapp?view=o365-worldwide#create-an-app

## Edit the config file
```
cp secrets-sample.json secrets.json
```

Then edit the config with the good values.

| Secret | Explaination |
|----------|--------------|
|`tenantId`| Microsoft Tenant ID (?tid=... in MDE console URL) |
|`appId`| Called `clientId` sometimes |
|`appSecret`| Your App / Client secret |
|`proxyUrl`| Your proxy if needed - leave blank if not |

```
{
    "tenantId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "appId": " XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "appSecret": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "proxyUrl": ""
}
```

## Get a report of onboarded machines (Windows Servers only)

> Windows

```
PS C:\Users\Me\Test> python mde_api.py machines report
```

> Linux

```
$ python3 mde_api.py machines report
```

> Linux  

```
$ chmod +x mde_api.py
$ ./mde_api.py machines report
```

## Output for the report

- An Excel (autofiltered) file will be created with datetime.

```
PS C:\Users\Me\Test> python .\mde_api.py machines report
55 fully onboarded, 5 can be onboarded, 5 inactive.
Processed 323 API results.
Successfully created 2023-12-21-15_47_24-mde-api-results.xlsx
```

# Other commands and subcommands

### machines

* `machines report`

* `machines offboard`

Requests offboarding of a given machine using its `machineid`

```
PS C:\Users\A107426\Local\mde_api> python .\mde_api.py machines offboard dc977c3c84ba18e1174affaff68e70cd81ffxxxx
Offboarding machine with ID: dc977c3c84ba18e1174affaff68e70cd81ffxxxx
{
    "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#MachineActions/$entity",
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "type": "Offboard",
    "title": null,
    "requestor": "YOUR APP REGISTRATION",
    "requestorComment": "Offboard machine by automation",
    "status": "Pending",
    "machineId": "dc977c3c84ba18e1174affaff68e70cd81ffxxxx",
    "computerDnsName": "computer.your.domain",
    "creationDateTimeUtc": "2024-01-02T13:39:46.7738206Z",
    "lastUpdateDateTimeUtc": "2024-01-02T13:39:46.773821Z",
    "cancellationRequestor": null,
    "cancellationComment": null,
    "cancellationDateTimeUtc": null,
    "errorHResult": 0,
    "scope": null,
    "externalId": null,
    "requestSource": "PublicApi",
    "relatedFileInfo": null,
    "commands": [],
    "troubleshootInfo": null
}
```

### vulnerabilities

### TODO

# Errors

If the `secrets.json` is not properly filled.
```
General error: HTTP error: check your secrets file and App Registration.
```
