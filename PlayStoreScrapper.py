"""
📘 Example Output File (PlayStoreScrapped_Result/com.microsoft.office.onenote.txt)

App Name: Microsoft OneNote
App ID: com.microsoft.office.onenote
Installs: 500,000,000+
Score: 4.7
------------------------------------------------------------

User: John Doe | Score: 5 | Review: Excellent app for note taking!
User: Alice W | Score: 3 | Review: Needs improvement in sync speed.
User: Bob K | Score: 4 | Review: Love the integration with Outlook.

------------------------------------------------------------
Total reviews written: 1250
Time taken: 32.47 seconds

📊 Example Excel Summary (PlayStoreScrapped_Result/NoteAppSummary.xlsx)

| No | App Name                | Package ID                            | PlayStore Count Install | Average Score | PythonPlayStoreCrawlerCount | Time Taken (s) |
|----|--------------------------|---------------------------------------|--------------------------|----------------|------------------------------|----------------|
| 1  | Google Keep             | com.google.android.keep               | 1,000,000,000+          | 4.7            | 193787                       | 103.8          |
| 2  | Microsoft OneNote       | com.microsoft.office.onenote          | 500,000,000+            | 4.7            | 157443                       | 85.03          |
"""

from google_play_scraper import app, reviews_all, Sort
import time
import pandas as pd
import os

# ============================================================
# 🧩 CONFIGURATION SECTION — all main settings centralized here
# ============================================================
CONFIG = {
    "OUTPUT_DIR": "PlayStoreScrapped_Result",             # Folder to store results
    "SUMMARY_FILENAME": "Summary.xlsx",                   # Excel summary file name
    "APP_IDS": [                                          # List of Play Store package IDs
        "com.google.android.keep",
        "com.microsoft.office.onenote",
        "notion.id",
        "com.evernote",
        "com.automattic.simplenote",
        "com.socialnmobile.dictapps.notepad.color.note",
        "com.samsung.android.app.notes",
        "com.zoho.notebook",
        "net.cozic.joplin",
        "com.standardnotes",
        "com.streetwriters.notesnook",
        "com.steadfastinnovation.android.projectpapyrus",
        "com.fiistudio.fiinote",
        "com.rgiskard.fairnote",
        "com.viettran.INKredible",
        "com.yygg.note.app",
        "com.fluidtouch.noteshelf3",
        "md.obsidian",
        "com.bvblogic.nimbusnote",
        "com.mmm.postit"
    ]
}

# Create output directory
os.makedirs(CONFIG["OUTPUT_DIR"], exist_ok=True)

# 🕒 Start overall timer
overall_start = time.time()

# 📊 Store app summaries
summary_data = []

# ============================================================
# 🚀 MAIN SCRAPING LOOP
# ============================================================
for i, app_id in enumerate(CONFIG["APP_IDS"], start=1):
    print("=" * 80)
    print(f"Processing ({i}/{len(CONFIG['APP_IDS'])}): {app_id}")
    start_time = time.time()

    try:
        # Fetch app metadata
        result = app(app_id)
        app_name = result['title']
        installs = result.get('installs', 'N/A')
        score = result.get('score', 'N/A')
        print(f"{app_name} — {installs} installs — Score: {score}")

        # Fetch all reviews (sorted newest first)
        rvs = reviews_all(app_id, sort=Sort.NEWEST)

        # Output file path
        file_name = os.path.join(CONFIG["OUTPUT_DIR"], f"{app_id}.txt")

        # Write metadata + reviews
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"App Name: {app_name}\n")
            f.write(f"App ID: {app_id}\n")
            f.write(f"Installs: {installs}\n")
            f.write(f"Score: {score}\n")
            f.write("-" * 60 + "\n\n")
            for r in rvs:
                f.write(f"User: {r['userName']} | Score: {r['score']} | Review: {r['content']}\n")

        # Measure time taken
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        # Add footer info
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("\n" + "-" * 60 + "\n")
            f.write(f"Total reviews written: {len(rvs)}\n")
            f.write(f"Time taken: {duration} seconds\n")

        # Add to summary data
        summary_data.append({
            "No": i,
            "App Name": app_name,
            "Package ID": app_id,
            "PlayStore Count Install": installs,
            "Average Score": score,
            "PythonPlayStoreCrawlerCount": len(rvs),
            "Time Taken (s)": duration
        })

        print(f"✅ READY — {len(rvs)} reviews saved to {file_name} in {duration} seconds\n")

    except Exception as e:
        print(f"❌ Error processing {app_id}: {e}\n")

# ============================================================
# 📊 EXPORT SUMMARY TO EXCEL
# ============================================================
overall_end = time.time()
total_duration = round(overall_end - overall_start, 2)
print("=" * 80)
print(f"🎯 ALL DONE — Total scraping time: {total_duration} seconds")

df = pd.DataFrame(summary_data)
excel_file = os.path.join(CONFIG["OUTPUT_DIR"], CONFIG["SUMMARY_FILENAME"])
df.to_excel(excel_file, index=False)
print(f"📁 Summary Excel file saved as: {excel_file}")
