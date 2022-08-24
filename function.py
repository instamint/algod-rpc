import os
import json
import requests

server = "http://143.198.164.105:8080"
token = "7dda5b4dc7e63769ce9dd2003f2904c59fcb068296f67c1cae5b418af0c1d0bd"
server_header = {
    "X-Algo-API-Token":  token,
}

## LOGGING ##


def log(data: str):
    os.system("clear")

    print(f"\n----------------")
    print(json.dumps(data, indent=2, sort_keys=True))
    print("----------------")

## COMMON ##
def get_health():
    health = requests.get(f"{server}/health")
    if health.status_code == 200:
        return '{"status": "OK" }'
    else:
        return '{"status": "UNAVAILABLE" }'


def get_genesis():
    return requests.get(f"{server}/genesis").json()


def get_version():
    return requests.get(f"{server}/versions").json()

## DEFAULT ##
def get_status():
    return requests.get(f"{server}/v2/status", headers=server_header).json()

def get_account_by_address(address_id: str):
    return requests.get(f"{server}/v2/accounts/{address_id}?format=json", headers=server_header).json()

def get_application_by_address(application_id: str):
    return requests.get(f"{server}/v2/applications/{application_id}", headers=server_header).json()

def get_asset_by_address(asset_id: str):
    return requests.get(f"{server}/v2/assets/{asset_id}", headers=server_header).json()

def get_transaction_params():
    return requests.get(f"{server}/v2/transactions/params", headers=server_header).json()

def post_transaction(rawtxn):
    return requests.post(f"{server}/v2/transactions", data=rawtxn ,headers={
        "X-Algo-API-Token":  token,
        "Content-Type": "application/octet-stream"
    }).json()

def get_pending_transaction(tx_id: str):
    return requests.get(f"{server}/v2/transactions/pending/{tx_id}?format=json", headers=server_header).json()
