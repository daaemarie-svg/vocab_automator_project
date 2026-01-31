import pandas as pd
import json
import os
import re

# 1. Path Setup (Precision is Kindness)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_file = os.path.join(base_dir, '05_Source_Excel', '어휘끝_중학 고난도_어휘리스트.xlsx')
output_dir = os.path.join(base_dir, '02_Data_JSON', 'eohwi_kkuet')
os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(excel_file, header=None)
current_unit = None
unit_words = []

def save_unit(name, words):
    if name and words:
        file_path = os.path.join(output_dir, f"{name}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=4)
        print(f"💾 EOHWI: Saved {len(words)} words to {name}.json")

# 2. The Loop
for index, row in df.iterrows():
    row_values = [str(val).strip() for val in row if pd.notna(val)]
    row_text = " ".join(row_values).upper()
    
    if "UNIT" in row_text:
        save_unit(current_unit, unit_words)
        match = re.search(r"UNIT\s*(\d+)", row_text)
        if match:
            current_unit = f"UNIT_{match.group(1).zfill(2)}"
            unit_words = []
            print(f"🎯 Triggered: {current_unit}")
        continue

    # Harvest: Broad Scan for Eohwi Kkuet layout
    if current_unit and len(row_values) >= 2:
        if row_values[0].isdigit():
            word = row_values[1]
            meaning = " ".join(row_values[2:])
            if word.lower() not in ["english", "word"]:
                unit_words.append({
                    "word": word,
                    "meaning": meaning,
                    "bolded": f"**{word}**"
                })

save_unit(current_unit, unit_words)
print(f"\n✅ Finished harvesting Eohwi Kkuet")