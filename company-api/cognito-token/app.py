import boto3
import hashlib
import hmac
import base64

def authenticate_and_get_token(username: str, password: str, 
    user_pool_id: str, app_client_id: str) -> None:
    client = boto3.client('cognito-idp')


    key = bytes("rhcsv0ihuep6dn6l30uuh35la6rhpsl6n008j0dj02vjod69rqg", "utf-8")
    msg = bytes(username + app_client_id, "utf-8")

    
    new_digest = hmac.new(key, msg, hashlib.sha256).digest()
    
    SECRET_HASH = base64.b64encode(new_digest).decode()

    # |'ADMIN_USER_PASSWORD_AUTH'

    # DMIN_USER_PASSWORD_AUTH

    response = client.admin_initiate_auth(
    UserPoolId=user_pool_id,
    ClientId=app_client_id,
    AuthFlow='ADMIN_USER_PASSWORD_AUTH',
    AuthParameters={
        "USERNAME": username,
            "PASSWORD": password,
            # "SECRET_HASH": SECRET_HASH
    },
    )
    print(response['AuthenticationResult']['IdToken'])


authenticate_and_get_token('sinamile@gmail.com', 'sinamile123', 'eu-central-1_QuOiWaPvS', '21f6k7usgcmcsocgcsj2l0l94c')