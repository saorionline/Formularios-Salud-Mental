# Assuming 'verification_dashboard' is your list from the previous step

print("--- MORNING CALL LIST: PREVENTING BILLING DISPUTES ---")
print(f"{'PATIENT':<15} | {'REASON FOR CALL'}")
print("-" * 50)

for patient in verification_dashboard:
    # We ONLY want to trigger a report if prevention is False
    if not patient["out_of_pocket_prevention"]:
        name = patient["patient"]
        issue = patient["scenario"]
        
        # Accessing the nested frequency for a specific detail
        if "Frequency" in issue:
            detail = patient["frequency_limitations"]["prophy_D1110"]
        elif "Waiting" in issue:
            detail = patient["frequency_limitations"]["fmx_D0210"]
        else:
            detail = f"Only ${patient['remaining_annual_max']} left."

        print(f"{name:<15} | {issue} ({detail})")

print("-" * 50)
print("Total calls to make: ", sum(1 for p in verification_dashboard if not p["out_of_pocket_prevention"]))