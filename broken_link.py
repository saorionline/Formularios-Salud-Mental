# A dictionary representing the "Database" of attachments
nea_database = {
    "Claim_101": "NEA-998234",
    "Claim_102": "NEA-776121",
    "Claim_103": None  # <--- This is the "Broken Link"
}

# The "Ideal Action" Code
def fix_missing_attachment(claim_id, new_attachment_id):
    nea_database[claim_id] = new_attachment_id
    print(f"Success: {claim_id} is now linked to {new_attachment_id}. Ready for adjudication.")

# --- THE TRIGGER (The Action) ---
# We are calling the function to fix Claim_103
fix_missing_attachment("Claim_103", "NEA-555000")

# Verify that the database was actually updated
print(f"Updated Database: {nea_database}")    