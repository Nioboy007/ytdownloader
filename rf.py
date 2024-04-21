import requests
from urllib.parse import urlencode

# Replace these with your client details from the provided JSON file
CLIENT_ID = "840842605914-pjajijhgefeku92f49vlffrsrm52mluq.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = 'http://localhost'
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

# Step 1: Direct user to authorization URL
def get_authorization_url():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': ' '.join(SCOPES),
        'access_type': 'offline',  # This will prompt for a refresh token
        'include_granted_scopes': 'true'
    }
    url = f'https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}'
    return url

# Step 2: User will grant access and receive an authorization code
# This code should be handled by your redirect URI in a real application
# For this script, you'll need to paste the code manually
authorization_url = get_authorization_url()
print(f'Please go to the following URL and authorize access: {authorization_url}')
authorization_code = input('Enter the authorization code: ')

# Step 3: Exchange authorization code for a refresh token and access token
def exchange_code_for_tokens(authorization_code):
    token_url = 'https://oauth2.googleapis.com/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        'code': authorization_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, headers=headers, data=body)
    return response.json()  # This will contain the refresh token and access token

tokens = exchange_code_for_tokens(authorization_code)
print(f'Access Token: {tokens.get("access_token")}')
print(f'Refresh Token: {tokens.get("refresh_token")}')
 
