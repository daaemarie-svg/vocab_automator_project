import json
import os
import re
from datetime import datetime

def build_prompt(module, book, days_string):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base, '02_Data_JSON')
    
    # 1. Load Vocab
    all_vocab = []
    day_list = [d.strip() for d in days_string.split(',')] 
    for day in day_list:
        vocab_path = os.path.join(data_path, book, f"{day}.json")
        if os.path.exists(vocab_path):
            with open(vocab_path, 'r', encoding='utf-8') as f:
                all_vocab.extend(json.load(f))
        else:
            print(f"❌ Error: Could not find {day}.json in {book}")
            return

    # 2. Universal Grammar Rotation Logic
    grammar_bank_path = os.path.join(data_path, 'grammar_bank.json')
    with open(grammar_bank_path, 'r', encoding='utf-8') as f:
        grammar_bank = json.load(f)
    
    all_grammar_keys = list(grammar_bank.keys())
    day_num_match = re.search(r'\d+', day_list[0])
    day_num = int(day_num_match.group()) if day_num_match else 0
    
    grammar_index = day_num % len(all_grammar_keys)
    g_key = all_grammar_keys[grammar_index]
    g = grammar_bank[g_key]

    # 3. Load Module Template
    template_path = os.path.join(base, '04_Automated Prompts', f"template_{module}.txt")
    if not os.path.exists(template_path):
        print(f"❌ Error: Template file 'template_{module}.txt' not found.")
        return
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 4. Inject Syntax-Specific Strict Rules
    # Note: Using g.get('en') as a fallback to prevent 'rigor' key errors
   # 4. Inject Syntax-Specific Strict Rules (CSV/Canva Ready)
    strict_rules = f"""
[STRICT RULE]: Generate exactly 10 questions for Version A and 10 questions for Version B.
[STRICT RULE]: Restart numbering for Version B (1-10).
[STRICT RULE]: Ensure every word in the [VOCAB_LIST] is used at least once across the 20 total questions to ensure full rotation.
[STRICT RULE]: Randomization Key: Before each version, output: "RANDOMIZATION KEY A: [10 letters]" and "RANDOMIZATION KEY B: [10 letters]". Max 3 of any letter (A, B, C, D) per version. No triple repeats.
[STRICT RULE]: Distractor Logic (40/40/20): 40% Word Class (Noun/Adj/Adv swap), 40% Functional (Grammar Overlay: {g.get('en', 'Standard')}), 20% Semantic nuance traps.

[FORMATTING RULE]: After generating the 20 questions, you MUST provide a MARKDOWN TABLE containing all 20 questions for easy data extraction. Use these exact columns:
| Version | Q_Num | Sentence_Stem | Option_A | Option_B | Option_C | Option_D | Correct_Ans |
[STRICT RULE]: In the "Sentence_Stem" column, use a double underscore (__) for the blank space.
"""
    
    prompt = template.replace("[VOCAB_LIST]", json.dumps(all_vocab, ensure_ascii=False, indent=2))
    prompt = prompt.replace("[GRAMMAR_OVERLAY]", f"{g.get('en', '')} ({g.get('kr', '')})")
    prompt = prompt.replace("[STRICT_RULES]", strict_rules)
    prompt = prompt.replace("[WORD_COUNT]", str(len(all_vocab)))
    
    # 5. Save to 06_Generated_Prompts
    output_dir = os.path.join(base, '06_Generated_Prompts')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    safe_days = days_string.replace(", ", "_").replace(",", "_")
    filename = f"{timestamp}_{book}_{safe_days}_{module}.txt"
    file_path = os.path.join(output_dir, filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(prompt)

    print("\n" + "="*50)
    print(f"🚀 {module.upper()} PROMPT GENERATED & SAVED")
    print(f"📂 File: {file_path}")
    print(f"📚 Book: {book} | 🗓️ Days: {days_string}")
    print(f"🧠 Grammar Overlay: {g.get('en', 'N/A')}")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("\n--- 🛠️ Danielle Marie: dFest Curriculum Builder 🛠️ ---")
    mod = input("Enter module (syntax, context, audit, recursive): ").strip().lower()
    bk = input("Enter book folder (e.g., wm_basic): ").strip()
    ds = input("Enter day files (e.g., DAY_17, DAY_18): ").strip()
    
    try:
        build_prompt(mod, bk, ds)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")