import pandas as pd
import json
import os

# 1. Load your CSV file
csv_file = 'SchoolYear-EnglishGrammarPoint-KoreanName-ExampleSentenceEnglish-ExampleSentenceKorean.csv'
df = pd.read_csv(csv_file)

# 2. Create the dictionary (The 'Brain' of the JSON)
grammar_bank = {}

for index, row in df.iterrows():
    # Create a 'key' by making the English name lowercase and replacing spaces with underscores
    key = row['English Grammar Point'].lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "")
    
    grammar_bank[key] = {
        "level": row['School Year'],
        "en": row['English Grammar Point'],
        "kr": row['Korean Name'],
        "example_en": row['Example Sentence (English)'],
        "example_kr": row['Example Sentence (Korean)']
    }

# 3. Save to your Data folder
output_path = '02_Data_JSON/grammar_bank.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(grammar_bank, f, ensure_ascii=False, indent=2)

print(f"Success! {len(grammar_bank)} grammar points converted to {output_path}")