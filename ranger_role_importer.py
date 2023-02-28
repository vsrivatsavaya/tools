import json
from requests import get, post
import requests
import time
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

f = open("roles.json", "r")
roles_convert = json.loads(f.read())

ROLES = roles_convert['roles']
TOTAL_ROLES = len(ROLES)

print "Total number of roles " + str(TOTAL_ROLES) + " will be imported."

ROLES_API = "/service/roles/roles/"
IMPORT_RANGER_URL = raw_input("DEST_RANGER URL:- ")
IMPORT_RANGER_ADMIN_USER = raw_input("DEST_RANGER ADMIN USER:- ")
IMPORT_RANGER_ADMIN_PASSWORD = getpass(prompt='DEST_RANGER ADMIN PASSWORD:- ', stream=None)
headers = {'Accept' : 'application/json'}

# Importing roles with all the configured users and groups
FAILED_ROLES = []
IMPORTED_ROLES = []
for ROLE in ROLES :
    del ROLE['id']
    response = post(IMPORT_RANGER_URL + ROLES_API, headers=headers, json=ROLE, verify=False,
                    auth=(IMPORT_RANGER_ADMIN_USER, IMPORT_RANGER_ADMIN_PASSWORD))
    STATUS = response.status_code
    ROLENAME = ROLE['name']
    if STATUS is 200:
        print "Successfully Imported Role " + ROLENAME + " with status " + str(STATUS)
        IMPORTED_ROLES.append(ROLENAME)
    else:
        print "Import for role " + ROLENAME + " failed with status " + str(STATUS)
        FAILED_ROLES.append(ROLENAME)

print "\n" + str(len(FAILED_ROLES)) + " Roles have failed to export" + \
      "\n" + str(len(IMPORTED_ROLES)) + " Roles have been imported successfully"

print "\nCould not import Following roles:- "
for FAILED_ROLE in FAILED_ROLES:
    print FAILED_ROLE
