import requests

################# USER INPUT #################

DOMAIN = ""
ACCESS_TOKEN_API_PATH = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
AUDIENCE = ""     # aka `identifier`
GRANT_TYPE = ""

##############################################


data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "audience": AUDIENCE,
    "grant_type": GRANT_TYPE,
}


res = requests.post(f"https://{DOMAIN}/{ACCESS_TOKEN_API_PATH}", data=data)


################## OUTPUT ####################
############### ACCESS TOKEN #################

if res.ok:
    print(res.json())
else:
    print("Some error occured")

###############################################
