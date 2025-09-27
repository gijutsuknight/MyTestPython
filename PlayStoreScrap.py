from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/androidpublisher']
SERVICE_ACCOUNT_FILE = 'service-account.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('androidpublisher', 'v3', credentials=credentials)

package_name = "com.example.myapp"
result = service.reviews().list(packageName=package_name).execute()

for review in result.get("reviews", []):
    print(review["reviewId"], review["comments"][0]["userComment"]["text"])
