from GoogleAuth.BaseGoogleService import BaseGoogleService
from GoogleAuth.ServiceAccountGoogleAuth import ServiceAccountGoogleAuth
from GoogleAuth.ClientSecretGoogleAuth import ClientSecretGoogleAuth
from googleapiclient.errors import HttpError
from oauth2client import file
from oauth2client import tools
from oauth2client import client
import argparse
from datetime import *

def getGoogleService(secretFile,scope,apiName,apiVersion):
	secretFileType = 'user'
	searchSecretFile = open(secretFile, "r")
	for line in searchSecretFile.readlines():
		if '"type": "service_account"' in line: secretFileType = 'service'
		searchSecretFile.close()
	try:
		
		if secretFileType == 'service':
			auth = ServiceAccountGoogleAuth(secretFile, scope=scope)
			serviceSetup = BaseGoogleService(api_name=apiName, api_version=apiVersion, google_auth=auth)
			auth.authorize()
			return serviceSetup.getService()
		else:
			parser = argparse.ArgumentParser(
				formatter_class=argparse.RawDescriptionHelpFormatter,
				parents=[tools.argparser])
			flags = parser.parse_args([])
			flow = client.flow_from_clientsecrets(
				secretFile, scope=scope,
				message=tools.message_if_missing(secretFile,))
			storage = file.Storage(apiName + '.dat')
			credentials = storage.get()
			if credentials is None or credentials.invalid:
				tools.run_flow(flow, storage, flags)
			auth = ClientSecretGoogleAuth(secretFile,apiName + '.dat',scope=scope)
			serviceSetup = BaseGoogleService(api_name=apiName, api_version=apiVersion, google_auth=auth)
			auth.authorize()
			return serviceSetup.getService()
		
	except HttpError as err:
		raise err
	
def setProgramRunningMode(startDate,endDate):
	'''
	Checks to see if dates passed in are equal and the same as yesterday or today.  If they are, set the program
	mode to AUTOMATIC, which means it'll wait for the data to be ready
	:param startDate:
	:param endDate:
	:return: 'AUTO' or 'BACKFILL'
	'''
		
	if ((startDate.strftime("%Y%m%d") == (datetime.now() - timedelta(days=1)).strftime("%Y%m%d") or
			 startDate.strftime("%Y%m%d") == datetime.now().strftime("%Y%m%d")
	     )
	    and startDate.strftime("%Y%m%d") == endDate.strftime("%Y%m%d")):
		return CONSTANT.PROGRAM_MODE_AUTO
	else:
		return CONSTANT.PROGRAM_MODE_BACKFILL
	
		