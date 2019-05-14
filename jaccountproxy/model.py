from jaccountproxy import app
from oauthjaccount import JaccountClient


def get_client():
    return JaccountClient(
        client_id=app.config['CLIENT_ID'],
        client_secret=app.config['CLIENT_SECRET']
    )
