import requests
from database import get_access_token, insert_access_token

################# USER INPUT #################

DOMAIN = ""
ACCESS_TOKEN_API_PATH = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
AUDIENCE = ""   # aka `identifier`
GRANT_TYPE = ""

##############################################


class AcessTokenGenerator(object):
    def get_access_token(self):
        access_token = get_access_token()
        if access_token is None:
            access_token = self._generate_access_token()
        return access_token

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
            insert_access_token(json_res["access_token"], json_res["expires_in"])
            return json_res["access_token"]
        else:
            print("Some error occured")


############### OUTPUT ###################
############ ACCESS TOKEN ################

generator = AcessTokenGenerator()
print(generator.get_access_token())

##########################################
