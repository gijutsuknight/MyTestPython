from google_play_scraper import app, reviews_all, Sort
import time

# 🧩 Configuration: list of app IDs
app_ids = [
    "com.google.android.keep",
    "com.microsoft.office.onenote",
    "com.evernote",
    "notion.id",
    "com.automattic.simplenote"
]

# 🕒 Global start time (for all apps)
overall_start = time.time()

for app_id in app_ids:
    print("=" * 80)
    print(f"Processing: {app_id}")

    start_time = time.time()

    try:
        # Get app metadata
        result = app(app_id)
        print(f"{result['title']} — {result.get('installs', 'N/A')} installs")

        # Get all reviews
        rvs = reviews_all(
            app_id,
            sort=Sort.NEWEST
        )

        # Write metadata + reviews to file
        file_name = f"{app_id}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"App Name: {result['title']}\n")
            f.write(f"App ID: {app_id}\n")
            f.write(f"Installs: {result.get('installs', 'N/A')}\n")
            f.write(f"Score: {result.get('score', 'N/A')}\n")
            f.write("-" * 60 + "\n\n")

            for r in rvs:
                line = f"User: {r['userName']} | Score: {r['score']} | Review: {r['content']}\n"
                f.write(line)

        # End timing for this app
        end_time = time.time()
        duration = end_time - start_time

        # Write summary footer
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("\n" + "-" * 60 + "\n")
            f.write(f"Total reviews written: {len(rvs)}\n")
            f.write(f"Time taken: {duration:.2f} seconds\n")

        print(f"✅ READY — {len(rvs)} reviews saved to {file_name} in {duration:.2f} seconds\n")

    except Exception as e:
        print(f"❌ Error processing {app_id}: {e}\n")

overall_end = time.time()
print("=" * 80)
print(f"🎯 ALL DONE — Total time: {overall_end - overall_start:.2f} seconds")
