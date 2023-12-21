# mde_api

This script helps to get the list of EDR onboarded machines (Windows Servers) in an easy way.

For a better understanding, refer to the official Microsoft Defender for Endpoint API documentation: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/api/exposed-apis-list?view=o365-worldwide

## Install dependencies

```
pip install -r requirements.txt
```

## Usage

```
usage: mde_api.py [-h] {machines,token}

List onboarded machines or token

positional arguments:
  {machines,token}
                        Action to perform

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
|`tenantId`| the display name of your company |
|`appId`| Called `clientId` sometimes |
|`appSecret`| Your secret |

```
{
    "tenantId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "appId": " XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "appSecret": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
}
```

## Execute the script

```
PS C:\Users\Me\Test> python mde_api.py machines
```

or

```
python3 mde_api.py machines
```

## Output

- An Excel (autofiltered) file will be created with datetime.

```
PS C:\Users\Me\Test> python .\mde_api.py
55 fully onboarded, 5 can be onboarded, 5 inactive.
Processed 323 API results.
Successfully created 2023-12-21-15_47_24-mde-api-results.xlsx
```

# Errors

If the `secrets.json` is not properly filled.
```
General error: HTTP error: 401 check your config file and API Token
```