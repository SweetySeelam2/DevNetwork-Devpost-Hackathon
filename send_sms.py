# send_sms.py  (legacy SDK)
import os
from dotenv import load_dotenv
import vonage
import sys

load_dotenv()  # loads .env from current folder

API_KEY = os.getenv("VONAGE_API_KEY")
API_SECRET = os.getenv("VONAGE_API_SECRET")

# Read either VONAGE_FROM or VONAGE_FROM_NUMBER (fallback)
FROM = os.getenv("VONAGE_FROM") or os.getenv("VONAGE_FROM_NUMBER")
TO   = os.getenv("VONAGE_TO")

def die(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

if not API_KEY or not API_SECRET:
    die("Missing VONAGE_API_KEY or VONAGE_API_SECRET in .env")

if not FROM:
    die("Missing VONAGE_FROM (your Toll-Free) in .env")

if not TO:
    die("Missing VONAGE_TO (your handset) in .env")

print("DEBUG FROM:", repr(FROM))
print("DEBUG TO:", repr(TO))

client = vonage.Client(key=API_KEY, secret=API_SECRET)
sms = vonage.Sms(client)

print(f"Sending SMS from {FROM} to {TO} ...")
resp = sms.send_message({"from": FROM, "to": TO, "text": "OmniCare SMS test - hello"})
print(resp)


