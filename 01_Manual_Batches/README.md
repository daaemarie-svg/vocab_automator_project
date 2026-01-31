README.md
# NAESHIN WORKSHET SYSTEM v2.0
- **Rule 1:** Always generate Version A and Version B for drills.
- **Rule 2:** Always use 'base' instead of 'root'.
- **Rule 3:** The "No-Drop" audit must be performed in P4.
- **Rule 4:** Student Worksheet and Teacher Key must remain separate sections.
- **Rule 5:** Word count adjustment required per book series (Day 1-3 for 30-day books).

# WORKSHEET SYSTEM v1.0
This is the file that holds the manual batches. Class worksheets can be manually created until the automated system is up and running.
## ⚙️ Configuration & Scaling
- **Word Count Variable:** The `Total_Vocab` count must be manually adjusted in the System Prompt when switching book series.
    - *Example (어휘끝):* 60 words per batch (Distributed 15/15/15/15).
    - *Example (Grade Level Bridge):* 30 words per batch (Distributed 7/8/7/8).
- **Prompt Synchronization:** Ensure the `Segmentation` logic in Part 1 matches the total words provided in Part 2.

