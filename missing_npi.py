# A claim that might have errors
raw_claim = {
    "patient": "John Doe",
    "provider_npi": None,  # Missing NPI!
    "code": "D2750"
}

def clearinghouse_scrubber(claim):
    if claim["provider_npi"] is None:
        return "Rejected: Missing Provider NPI"
    return "Clean: Transmitted to Payer"

# Trigger the check
print(clearinghouse_scrubber(raw_claim))