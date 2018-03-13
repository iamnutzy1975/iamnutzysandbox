from BaseGoogleService import BaseGoogleService

MAJOR_DIM_ROWS = "ROWS"
MAJOR_DIM_COLUMNS = "COLUMNS"

VALUE_INPUT_OPTION_INPUT_VALUE_OPTION_UNSPECIFIED = "INPUT_VALUE_OPTION_UNSPECIFIED"
VALUE_INPUT_OPTION_RAW = "RAW"
VALUE_INPUT_OPTION_USER_ENTERED = "USER_ENTERED"

VALUE_RENDER_OPTION_UNFORMATTED = "UNFORMATTED_VALUE"

class SheetsGoogleService(BaseGoogleService):
    """Representing Google sheets sevice
    """

    def __init__(self, google_auth, scope = []):
        super(SheetsGoogleService, self).__init__("sheets", "v4", google_auth, scope)

    def enableReadOnly(self):
        p = "https://www.googleapis.com/auth/spreadsheets.readonly"
        self.google_auth.addScope(p)

    def enableEdit(self):
        p = "https://www.googleapis.com/auth/spreadsheets"
        self.google_auth.addScope(p)

    def getValues(self, spreadsheetId, range, majorDimension = None, valueRenderOption=None):
        if self.service is None:
            self.getService()

        rslt = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, 
            range=range,
            majorDimension = majorDimension,
            valueRenderOption = valueRenderOption).execute()

        return rslt.get('values', [])

    def updateValues(self, spreadsheetId, range, values, valueInputOption):
        if self.service is None:
            self.getService()

        assert isinstance(values, list)

        rslt = self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheetId, 
            range=range,
            valueInputOption = valueInputOption,
            body = { "range" :range, 
                     "values" : values }).execute()

        return rslt


