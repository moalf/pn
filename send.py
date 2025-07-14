import csv
from twilio.rest import Client

OUTPUT_FILE="formatted_contacts.csv"

# 🔐 Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+1234567890'  # Replace with your Twilio number

# 📨 Message content
message_body = "Hello from Dunamyx! 🚀 Your productivity upgrade starts now."

def send_sms(recipient, message_body):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=recipient
        )
        print(f"✅ Sent to {recipient} | SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send to {recipient}: {e}")

# 📂 Load contacts and send messages
with open(OUTPUT_FILE, mode="r", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        phone = row.get("FormattedPhone", "").strip()
        if phone and phone != "UNKNOWN":
            send_sms(phone, message_body)
