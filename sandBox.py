import os
import helpers

CLIENT_SECRET_CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), 'creds', 'APMK-GN.json')
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

g = helpers.getGoogleService(secretFile=CLIENT_SECRET_CREDENTIALS_PATH,scope=SCOPES,apiName='webmasters',apiVersion='v3')

print g