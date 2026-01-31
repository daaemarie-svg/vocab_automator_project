🛠️ Vocabulary Curriculum Engines: Automation Documentation
This document outlines the four-module architecture for generating ESL vocabulary materials tailored for Korean Naeshin (GPA) prep. These prompts are designed to be "plug-and-play" with Python-driven JSON inputs.

📐 Core System Principles
Precision is Kindness: Instructions must be 100% bilingual (English/Korean). Use plain text formatting.

Visual Anchor: Strict non-negotiable rule: All target vocabulary words used in sentences or passages must be bolded.

Dual-Path Design: Every generation must produce a Version A and a Version B.

Anti-Lazy Logic: Distractors and "Bugs" must use a 40/40/20 split (Word Class / Functional / Semantic).

No "Base" Labeling: Do not use the term "base" in student-facing materials. Focus on form and function.

🏗️ The Four Modules
1. Syntax (Word Form & Positioning)

Goal: Mastery of derivational and inflectional morphology.

Input: Vocabulary List + Grammar Overlay.

Logic: Multiple Choice Questions (MCQ) that move beyond simple suffix-swapping.

Traps: Tests whether the student can distinguish between active/passive, -ing/-ed, and nuanced semantic differences (e.g., sensible vs. sensitive).

2. Context (Logic & Narrative Endurance)

Goal: Reading endurance and logical fact-checking.

Input: Vocabulary List + Contextual Theme + Grammar Overlay.

Structure: Interleaved narratives (tracking two characters/ideas) to force comparison.

Logic Traps: Includes "Contextual Bugs" where a word choice contradicts the character's goal, and sentence-insertion tasks to test structural flow.

3. Audit (High-Level Error Detection)

Goal: High-ROI "Bug Hunting" for "Killer" exam questions.

Input: Vocabulary List + Grammar Overlay + Error Density.

Method: 15-20 sentences where students must find and fix subtle errors in vocabulary usage or grammar.

Teacher Key: Must follow the 6-Step Logical Debugger framework (Restate, Audit, Fix).

4. Recursive Review (Spaced Repetition)

Goal: Tilling the soil of previous weeks to ensure long-term retention.

Input: Current Word List + Review Word List (Current - 2 units).

Logic: "Opposite Pairings" where words from two different units are placed in the same sentence to create syntactic contrast.

Synthesis: High-pressure synthesis drills that prevent "Unit Dumping."

📁 Data Integration (Junior Dev Notes)
To scale this system, the prompts should be treated as functions. The following "Ports" must be satisfied in your Python script:

Port	Description
vocab_list	The target words for the current session.
grammar_overlay	The specific syntax rule to rotate (e.g., Relative Clauses).
theme	The narrative setting (e.g., Leo & Hana / Architecture).
review_list	The list from 2 units prior (for Recursive Review only).