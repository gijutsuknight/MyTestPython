from google_play_scraper import app, reviews_all, Sort
import time

# Configuration
app_id = "com.google.android.keep"

start_time = time.time()  # Start timing

# Get app metadata
result = app(app_id)

print(result['title'], result['installs'])

# Get all reviews
rvs = reviews_all(
    app_id,
    sort=Sort.NEWEST  # optional, but useful
)

# Write metadata + reviews to file
file_name = app_id + ".txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(f"App Name: {result['title']}\n")
    f.write(f"App ID: {app_id}\n")
    f.write(f"Installs: {result.get('installs', 'N/A')}\n")
    f.write(f"Score: {result.get('score', 'N/A')}\n")
    f.write("-" * 60 + "\n\n")

    for r in rvs:
        line = f"User: {r['userName']} | Score: {r['score']} | Review: {r['content']}\n"
        f.write(line)

end_time = time.time()  # End timing
duration = end_time - start_time

# Write duration info at end of file
with open(file_name, "a", encoding="utf-8") as f:
    f.write("\n" + "-" * 60 + "\n")
    f.write(f"Total reviews written: {len(rvs)}\n")
    f.write(f"Time taken: {duration:.2f} seconds\n")

print(f"READY — Reviews saved to {file_name}")
print(f"Time taken: {duration:.2f} seconds")
