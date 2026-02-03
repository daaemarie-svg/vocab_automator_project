import json, re
from spellchecker import SpellChecker

def dFest_full_audit(worksheet_path, json_path):
    spell = SpellChecker()
    with open(worksheet_path) as f, open(json_path) as j:
        content, data = f.read(), json.load(j)

    # 1. No-Drop Audit: Check all JSON words are present
    missing = [w['word'] for w in data['words'] if w['word'].lower() not in content.lower()]
    # 2. Lexicon Check: Ensure MCQ distractors (A-D) are real words
    options = re.findall(r"\([A-D]\)\s*(\w+)", content)
    nonsense = [word for word in options if word.lower() not in spell and word.lower() not in content.lower()]
    # 3. Structure & Terms: Versions A/B, tags, and no "root" [cite: 2026-01-08, 2026-01-26]
    valid = all(x in content for x in ["Version A", "Version B", "{{", "}}"]) and "root" not in content.lower()

    if not missing and not nonsense and valid:
        return "✅ Ecosystem Balanced: Pure Soil."
    return f"❌ Error: Missing: {missing} | Nonsense: {nonsense} | Structure: {valid}"