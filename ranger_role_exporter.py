import json
from requests import get, post
import requests
import time
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

EXPORT_RANGER_URL = raw_input("SOURCE_RANGER URL:- ")
ROLES_API = "/service/roles/roles/"
EXPORT_RANGER_ADMIN_USER = raw_input("SOURCE_RANGER ADMIN USER:- ")
EXPORT_RANGER_ADMIN_PASSWORD = getpass(prompt='SOURCE_RANGER ADMIN PASSWORD:- ', stream=None)
headers = {'Accept' : 'application/json'}


response = get(EXPORT_RANGER_URL + ROLES_API, headers=headers, verify=False,
               auth=(EXPORT_RANGER_ADMIN_USER, EXPORT_RANGER_ADMIN_PASSWORD))
f = open("roles.json", "w")
f.write(response.content)
f.close()
