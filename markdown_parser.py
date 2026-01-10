#!/usr/bin/env python3
import os
import random # Added for shuffling (optional but helpful)

def load_organized_questions(filepath):
    # Dictionary format: { "Section Name": ["Question 1", "Question 2"] }
    study_data = [] # Changed to a list of dicts for easier counting
    current_section = "General"

    if not os.path.exists(filepath):
        return []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            # Identify a Section (e.g., # Remote Workflow & Communication)
            if line.startswith('#'):
                current_section = line.lstrip('# ').strip()
            # Identify Question (e.g., - How do you ensure seamless communication with the in-office clinical team while working remotely?)    
            elif line.startswith(('-', '*')):
               # We strip the bullet point and save immediately
                clean_text = line.lstrip('-* ').strip()
                # Only add if there is actually text after the dash
                if clean_text:
                    study_data.append({
                        "section": current_section, 
                        "text": clean_text
                    })                
    return study_data

def run_exam(questions):
    total_available = len(questions)
    if total_available == 0:
        print("No questions found.")
        return

# --- NEW PROMPT SECTION ---
    print(f"Total healthcare questions loaded: {total_available}")
    try:
        limit_input = input(f"How many questions would you like to practice? (Press Enter for ALL): ")
        if limit_input == "":
            limit = total_available
        else:
            limit = int(limit_input)
    except ValueError:
        print("Invalid number. Showing all questions.")
        limit = total_available

    # Limit the list to the user's choice
    selected_questions = questions[:limit]
    
    # --- LOOP THROUGH SELECTED QUESTIONS ---
    for index, q in enumerate(selected_questions):
            # Visual feedback
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- US HEALTHCARE STUDY SESSION ---")
            print(f"SECTION: {q['section'].upper()}")
            print(f"Question {index + 1} of {len(selected_questions)}")
            print("-" * 30)
            
            print(f"\nPROMPT: {q['text']}")
            
            input("\n[Press Enter for next question]")

    print("\nGreat job! You've finished all sections.")

if __name__ == "__main__":
    # This finds the directory where your script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # This joins that directory with your filename
    file_path = os.path.join(script_dir, 'study_material.md')
    
    data = load_organized_questions(file_path)
    run_exam(data)