import requests

import frappe

@frappe.whitelist()
def click_to_call():
    url = "https://api.exotel.com/v1/Accounts/justsigns1/Calls/connect"

    payload = 'From=918428849121&To=918903733423&CallerId=080-719-09307'
    headers = {
    'Authorization': 'Basic MTg0OWMyOTQ3MTYxYWI3MDgxNTQ1ZmJmYjZkZmJmY2VhN2Y2MjA4YzMxOTYyMWQ5OjliNmE4NTkwODM1MDViNWY2MjlmY2UyNTA3Njc5MDg5OTYxZTlhODYwMWRlMTI4Mw==',
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


    print(response.text)
