from google_play_scraper import app, reviews_all, Sort
import time
import pandas as pd
import os

# ============================================================
# 🧩 CONFIGURATION SECTION
# ============================================================
CONFIG = {
    "OUTPUT_DIR": "PlayStoreScrapped_Result",
    "SUMMARY_FILENAME": "Summary.xlsx",
    "APP_IDS": [
        "my.com.tngdigital.ewallet",
        "com.shopeepay.my",
        "com.maybank2u.life",
        "com.cimb.octo",
        "com.rhbgroup.rhbmobilebanking",
        "com.pbb.mypb",
        "com.bankislam.bimbmobile",
        "com.beubankislam",
        "com.bsn.mybsn",
        "com.asnb.app",
        "my.kwsp.ikaun",
        "com.uob.mightymy",
        "com.ambank.amonline",
        "com.ocbc.mobile",
        "com.hlb.connect",
        "com.htsu.hsbcmobilebanking",
        "my.com.alliancebank",
        "com.irakyatmob.bkrm",
        "my.com.aeon.wallet",
        "com.wise.android"
    ]
}

os.makedirs(CONFIG["OUTPUT_DIR"], exist_ok=True)
overall_start = time.time()
summary_data = []

# ============================================================
# 🚀 MAIN SCRAPING LOOP
# ============================================================
for i, app_id in enumerate(CONFIG["APP_IDS"], start=1):
    print("=" * 80)
    print(f"Processing ({i}/{len(CONFIG['APP_IDS'])}): {app_id}")
    start_time = time.time()

    app_name = "-"
    installs = "-"
    score = "-"
    review_count = 0
    duration = 0
    exists = "No"

    try:
        # Fetch app metadata
        result = app(app_id)
        app_name = result.get('title', '-')
        installs = result.get('installs', '-')
        score = result.get('score', '-')
        exists = "Yes"
        print(f"{app_name} — {installs} installs — Score: {score}")

        # Fetch reviews
        rvs = reviews_all(app_id, sort=Sort.NEWEST)
        review_count = len(rvs)

        # Save reviews
        file_name = os.path.join(CONFIG["OUTPUT_DIR"], f"{app_id}.txt")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"App Name: {app_name}\nApp ID: {app_id}\nInstalls: {installs}\nScore: {score}\n")
            f.write("-" * 60 + "\n\n")
            for r in rvs:
                f.write(f"User: {r['userName']} | Score: {r['score']} | Review: {r['content']}\n")

        duration = round(time.time() - start_time, 2)
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("\n" + "-" * 60 + "\n")
            f.write(f"Total reviews written: {review_count}\n")
            f.write(f"Time taken: {duration} seconds\n")

        print(f"✅ READY — {review_count} reviews saved in {duration}s\n")

    except Exception as e:
        print(f"❌ Error processing {app_id}: {e}\n")

    # Add summary (even if failed)
    summary_data.append({
        "No": i,
        "App Name": app_name,
        "Package ID": app_id,
        "PlayStore Count Install": installs,
        "Average Score": score,
        "PythonPlayStoreCrawlerCount": review_count,
        "Time Taken (s)": duration,
        "Exist in PlayStore": exists
    })

# ============================================================
# 📊 EXPORT SUMMARY TO EXCEL
# ============================================================
df = pd.DataFrame(summary_data)
excel_file = os.path.join(CONFIG["OUTPUT_DIR"], CONFIG["SUMMARY_FILENAME"])
df.to_excel(excel_file, index=False)

total_duration = round(time.time() - overall_start, 2)
print("=" * 80)
print(f"🎯 ALL DONE — Total scraping time: {total_duration} seconds")
print(f"📁 Summary Excel file saved as: {excel_file}")
