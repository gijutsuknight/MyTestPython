import jwt, time, requests

KEY_ID = "YOUR_KEY_ID"
ISSUER_ID = "YOUR_ISSUER_ID"
PRIVATE_KEY = open("AuthKey.p8").read()

token = jwt.encode(
    {
        "iss": ISSUER_ID,
        "exp": int(time.time()) + 1200,
        "aud": "appstoreconnect-v1"
    },
    PRIVATE_KEY,
    algorithm="ES256",
    headers={"kid": KEY_ID}
)

headers = {"Authorization": f"Bearer {token}"}
url = "https://api.appstoreconnect.apple.com/v1/apps"
response = requests.get(url, headers=headers)

print(response.json())
