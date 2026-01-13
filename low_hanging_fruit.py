# 1. Our Data Structure: List of Patient Balances
patient_accounts = [
    {"patient": "Carlos R.", "balance": 15.50, "last_contact": 45},
    {"patient": "Beatriz M.", "balance": 250.00, "last_contact": 10},
    {"patient": "Julian D.", "balance": 8.00, "last_contact": 60},
    {"patient": "Elena G.", "balance": 12.25, "last_contact": 30},
    {"patient": "David O.", "balance": 500.00, "last_contact": 5},
    {"patient": "Sara L.", "balance": 19.99, "last_contact": 90}
]

def filter_low_hanging_fruit(accounts, threshold=20.00):
    print(f"--- SEARCHING FOR LOW-HANGING FRUIT (Under ${threshold}) ---")
    print(f"{'Patient Name':<15} | {'Balance':<10} | {'Strategy'}")
    print("-" * 45)
    
    total_recoverable = 0
    fruit_count = 0
    
    for acc in accounts:
        # Check if the balance is a 'small' amount (Low-Hanging Fruit)
        if 0 < acc["balance"] <= threshold:
            strategy = "Send Text-to-Pay"
            print(f"{acc['patient']:<15} | ${acc['balance']:<9.2f} | {strategy}")
            
            total_recoverable += acc["balance"]
            fruit_count += 1
            
    print("-" * 45)
    print(f"Total Found: {fruit_count} accounts")
    print(f"Potential Quick Recovery: ${total_recoverable:.2f}")

# Trigger the filter
filter_low_hanging_fruit(patient_accounts)