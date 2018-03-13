from BaseGoogleService import BaseGoogleService

class GAGoogleService(BaseGoogleService):
    """Representing GA  service"""

    def __init__(self, google_auth, scope=[]):
        super(GAGoogleService, self).__init__("analytics", "v3", google_auth, scope)

    def enableReadOnly(self):
        p = "https://www.googleapis.com/auth/analytics.readonly"
        self.google_auth.addScope(p)

    def enableEdit(self):
        p = "https://www.googleapis.com/auth/analytics.edit"
        self.google_auth.addScope(p)


