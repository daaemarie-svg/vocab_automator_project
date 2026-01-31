import pandas as pd
import json
import os

# ==========================================
# 1. THE CONFIGURATION (Your Control Panel)
# ==========================================
BOOKS = {
    "BASIC": {
        "folder": "wm_basic",
        "file": "WM중등 BASIC_2022개정_어휘리스트_배포본.xlsx"
    },
    "SIL_LYEOK": {
        "folder": "wm_sil_lyeok",
        "file": "WM중등 실력_2022개정_어휘리스트_배포본.xlsx"
    },
    "GO_NAN_DO": {
        "folder": "wm_go_nan_do",
        "file": "WM 중등 고난도_2022개정_어휘리스트_배포본.xlsx"
    }
}

# --- CHANGE THIS TO "BASIC","SIL_LYEOK" OR "GO_NAN_DO" AS NEEDED ---
CURRENT_BOOK_KEY = "GO_NAN_DO" 
# ==========================================

# 2. Path Setup (Pointing to your new 05 folder)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = BOOKS[CURRENT_BOOK_KEY]

excel_path = os.path.join(base_dir, '05_Source_Excel', config["file"])
output_dir = os.path.join(base_dir, '02_Data_JSON', config["folder"])

os.makedirs(output_dir, exist_ok=True)

def save_day_file(name, words):
    if name and words:
        # Precision: Filename safety for "Day 30(+Plus)"
        clean_name = name.replace(" ", "_").replace("(", "").replace(")", "").replace("+", "_PLUS").upper()
        file_path = os.path.join(output_dir, f"{clean_name}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=4)
        print(f"💾 {CURRENT_BOOK_KEY}: Saved {len(words)} words to {clean_name}.json")

# 3. Harvest Logic
try:
    df = pd.read_excel(excel_path)
    current_day = None
    day_words = []

    for index, row in df.iterrows():
        # WM Column Logic: 0=Day, 1=Word, 2=Meaning
        day_val = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
        word_val = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ""
        meaning_val = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ""

        if "Day" in day_val and day_val != current_day:
            save_day_file(current_day, day_words)
            current_day = day_val
            day_words = []
            print(f"🎯 Processing: {current_day}")

        if current_day and word_val.lower() != "단어" and len(word_val) > 1:
            day_words.append({
                "word": word_val,
                "meaning": meaning_val,
                "bolded": f"**{word_val}**"
            })

    save_day_file(current_day, day_words)
    print(f"\n✅ SUCCESS! {CURRENT_BOOK_KEY} complete.")

except Exception as e:
    print(f"❌ ERROR: {e}")