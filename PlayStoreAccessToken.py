from google.oauth2 import service_account
import google.auth.transport.requests

# Path to your service account key
KEY_PATH = "service-account.json"

SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH, scopes=SCOPES
)

# Refresh to get access token
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)

print("Access Token:", credentials.token)

# After getting the access token you may use it as bearer and get the App Review
# https://www.googleapis.com/androidpublisher/v3/applications/<App ID>/reviews