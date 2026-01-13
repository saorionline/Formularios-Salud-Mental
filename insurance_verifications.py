# Updated Insurance Verification Dashboard with Out-of-Pocket Prevention Flags
verification_dashboard = [
    {
        "patient": "John Doe",
        "scenario": "Standard Active - All Clear",
        "effective_date": "2026-01-01",
        "remaining_annual_max": 1250.00,
        "network_status": "In-Network",
        "deductible_status": {"total": 50.00, "met": 50.00, "remaining": 0.00},
        "frequency_limitations": {
            "prophy_D1110": "2 per 12 months",
            "bitewings_D0274": "1 per calendar year",
            "fmx_D0210": "1 per 5 years"
        },
        "out_of_pocket_prevention": True # All criteria met; low risk.
    },
    {
        "patient": "Mary Vance",
        "scenario": "Max Exhausted - Deductible Not Met",
        "effective_date": "2024-06-01",
        "remaining_annual_max": 75.00,
        "network_status": "In-Network",
        "deductible_status": {"total": 100.00, "met": 0.00, "remaining": 100.00},
        "frequency_limitations": {
            "prophy_D1110": "1 per 6 months",
            "bitewings_D0274": "1 per 12 months",
            "fmx_D0210": "1 per 3 years"
        },
        "out_of_pocket_prevention": False # ALERT: High risk due to exhausted maximum.
    },
    {
        "patient": "Robert Smith",
        "scenario": "Frequency Hit - High Deductible",
        "effective_date": "2025-01-01",
        "remaining_annual_max": 2000.00,
        "network_status": "In-Network",
        "deductible_status": {"total": 150.00, "met": 25.00, "remaining": 125.00},
        "frequency_limitations": {
            "prophy_D1110": "Last used 3 months ago - DENY",
            "bitewings_D0274": "Available",
            "fmx_D0210": "Available"
        },
        "out_of_pocket_prevention": False # ALERT: High risk of denial due to frequency.
    },
    {
        "patient": "Alice Young",
        "scenario": "Out-of-Network - Tier 2 Plan",
        "effective_date": "2026-01-01",
        "remaining_annual_max": 1500.00,
        "network_status": "Out-of-Network",
        "deductible_status": {"total": 50.00, "met": 50.00, "remaining": 0.00},
        "frequency_limitations": {
            "prophy_D1110": "2 per calendar year",
            "bitewings_D0274": "1 per calendar year",
            "fmx_D0210": "1 per 5 years"
        },
        "out_of_pocket_prevention": True # Set to True IF patient signed OON financial waiver.
    },
    {
        "patient": "Carlos Ruiz",
        "scenario": "Waiting Period - Major Work Only",
        "effective_date": "2026-01-01",
        "remaining_annual_max": 1000.00,
        "network_status": "In-Network",
        "deductible_status": {"total": 50.00, "met": 0.00, "remaining": 50.00},
        "frequency_limitations": {
            "prophy_D1110": "Available",
            "bitewings_D0274": "Available",
            "fmx_D0210": "12-month waiting period active"
        },
        "out_of_pocket_prevention": False # ALERT: Risk for major procedures (Waiting period).
    }
]

print("--- DAILY INSURANCE VERIFICATION REPORT ---")
print("-" * 50)

for p in verification_dashboard:
    name = p["patient"]
    rem_max = p["remaining_annual_max"]
    rem_ded = p["deductible_status"]["remaining"]
    net = p["network_status"]
    prevention = "SECURE" if p["out_of_pocket_prevention"] else "ACTION REQUIRED"
    
    # Printing the report
    print(f"PATIENT: {name}")
    print(f"  > Scenairo: {p['scenario']}")
    print(f"  > Network: {net}")
    print(f"  > Remaining Max: ${rem_max:,.2f}")
    print(f"  > Unmet Deductible: ${rem_ded:,.2f}")
    print(f"  > Status: [{prevention}]")
    print("-" * 50)


    # Assuming 'verification_dashboard' is your list from the previous step


## Out of Pocket Prevention

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