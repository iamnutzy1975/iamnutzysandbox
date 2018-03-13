from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
# from this link :
# https://cloud.google.com/compute/docs/tutorials/python-guide#gettingstarted

credentials = GoogleCredentials.get_application_default()
api = build('iam', 'v1', credentials=credentials)

req_body = {
    "accountId":"gnapi3sa"
    ,"serviceAccount":{
        "displayName": "DisplayName"
    }
}
sa = api.projects().serviceAccounts().create(name="projects/ap-gordnuttall",body=req_body).execute()

print sa
