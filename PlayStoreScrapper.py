from google_play_scraper import app, reviews

# Get app metadata
result = app('com.whatsapp')
print(result['title'], result['installs'])

# Get reviews
rvs, _ = reviews(
    'com.whatsapp',
    lang='en',   # language
    country='us', # country
    count=10     # number of reviews
)
for r in rvs:
    print(r['userName'], r['score'], r['content'])
