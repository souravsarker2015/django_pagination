from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import google_auth_oauthlib.flow
import os

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    path = os.getcwd()
    print(path + '/client_secrets.json')
#     flow = client.flow_from_clientsecrets(path + '/client_secrets.json', SCOPES)
#     # flow = flow_from_clientsecrets(os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))
#     creds = tools.run_flow(flow, store)
#
# service = discovery.build('forms', 'v1', http=creds.authorize(
#     Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
#
# # Prints the responses of your specified form:
# form_id = '1KYpJn8_hkYogATJPgsot8rm6JEcOVd1Dgzp_GMTqa6I'
# result = service.forms().responses().list(formId=form_id).execute()
# print(result)
