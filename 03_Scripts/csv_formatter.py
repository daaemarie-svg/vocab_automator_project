import csv
import os
import re

def table_to_csv():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base, 'temp_gemini_table.txt')
    output_file = os.path.join(base, '06_Generated_Prompts', 'canva_upload.csv')

    if not os.path.exists(input_file):
        print("❌ Error: 'temp_gemini_table.txt' not found. Please create it and paste Gemini's table inside.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract table rows using regex to find content between pipes |
    data_rows = []
    for line in lines:
        if '|' in line and '---' not in line: # Skip headers/separators if needed
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells and cells[0] != "Version": # Skip the header row
                data_rows.append(cells)

    # Define Canva-friendly Headers
    headers = ['Version', 'Q_Num', 'Sentence', 'A', 'B', 'C', 'D', 'Correct']

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_rows)

    print("\n" + "="*50)
    print(f"✅ HARVEST COMPLETE: CSV generated for Canva")
    print(f"📂 File: {output_file}")
    print("="*50 + "\n")

if __name__ == "__main__":
    table_to_csv()