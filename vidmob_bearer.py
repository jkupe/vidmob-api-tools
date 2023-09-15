import requests


def get_bearer_token(client_id, client_secret, code, grant_type):
    # API endpoint
    url = 'https://api-public.vidmob.com/VidMob/oauth2/access_token'

    # Form data to be sent in the request
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': grant_type
    }

    # Making the POST request
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        token_data = response.json()
        return token_data.get('access_token', None)
    else:
        return None


# Example usage
client_id = 'CLIENT ID'
client_secret = 'CLIENT SECRET'
code = 'REFRESH TOKEN'
grant_type = 'refresh_token' # or 'authorization_code'


token = get_bearer_token(client_id, client_secret, code, grant_type)
if token:
    print("Bearer Token:", token)
else:
    print("Failed to obtain token.")
