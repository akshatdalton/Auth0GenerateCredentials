import requests
from datetime import datetime, timedelta

################# USER INPUT #################

DOMAIN = ""
ACCESS_TOKEN_API_PATH = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
AUDIENCE = ""  # aka `identifier`
GRANT_TYPE = ""

##############################################


class AcessTokenGenerator(object):
    def __init__(self) -> None:
        self._access_token, self._expiry_date = None, None
        self._generate_access_token()

    def get_access_token(self):
        if self.is_expired():
            self._generate_access_token()
        return self._access_token

    def is_expired(self):
        return self._expiry_date <= datetime.now()

    def _generate_access_token(self):
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "audience": AUDIENCE,
            "grant_type": GRANT_TYPE,
        }

        res = requests.post(f"https://{DOMAIN}/{ACCESS_TOKEN_API_PATH}", data=data)
        if res.ok:
            json_res = res.json()
            self._access_token = json_res["access_token"]
            self._update_expiry_date(json_res["expires_in"])
        else:
            print("Some error occured")

    def _update_expiry_date(self, expires_in: int):
        self._expiry_date = datetime.now() + timedelta(0, expires_in)


############### OUTPUT ###################
############ ACCESS TOKEN ################

generator = AcessTokenGenerator()
print(generator.get_access_token())

##########################################
