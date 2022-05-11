import requests
from diskcache import Cache

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
        self._cache = Cache("/tmp/diskcache")

    def get_access_token(self):
        with Cache(self._cache.directory) as reference:
            if "access_token" not in reference:
                self._generate_access_token(reference)
            return reference.get("access_token")

    def _generate_access_token(self, reference):
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "audience": AUDIENCE,
            "grant_type": GRANT_TYPE,
        }

        res = requests.post(f"https://{DOMAIN}/{ACCESS_TOKEN_API_PATH}", data=data)
        if res.ok:
            json_res = res.json()
            reference.set(
                "access_token", json_res["access_token"], expire=json_res["expires_in"]
            )
        else:
            print("Some error occured")


############### OUTPUT ###################
############ ACCESS TOKEN ################

generator = AcessTokenGenerator()
print(generator.get_access_token())

##########################################
