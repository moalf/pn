import phonenumbers
import csv

INPUT_FILE="contacts.csv"
OUTPUT_FILE="formatted_contacts.csv"

# 🌎 Probable regions covering Americas + global anchors
probable_regions = [
    "US", "CA", "MX",  # North America
    "BR", "AR", "CL", "CO", "PE", "VE", "UY", "EC", "BO", "PY", "SR", "GY",  # South America
    "GT", "HN", "SV", "NI", "CR", "PA", "BZ",  # Central America
    "DO", "HT", "JM", "TT", "CU",  # Caribbean
    "GB", "FR", "DE", "IN", "JP", "NG"  # Global anchors
]

def format_to_e164(raw_number):
    for region in probable_regions:
        try:
            num = phonenumbers.parse(raw_number, region)
            if phonenumbers.is_valid_number(num):
                return phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            continue
    return "UNKNOWN"

# 🚀 Read from source CSV and write to new one
with open(INPUT_FILE, mode="r", newline='', encoding="utf-8") as infile, \
     open(OUTPUT_FILE, mode="w", newline='', encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["FormattedPhone"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        raw = row.get("Phone", "").strip()
        row["FormattedPhone"] = format_to_e164(raw)
        writer.writerow(row)
