# app.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
FROM_NUMBER = os.getenv("VONAGE_FROM")  # e.g. +18334296093

def normalize_msisdn(s: str | None) -> str | None:
    if not s:
        return None
    s = s.strip().replace(" ", "")
    if not s.startswith("+") and s.isdigit():
        s = "+" + s
    return s

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.api_route("/inbound", methods=["GET", "POST"])
async def inbound(req: Request):
    # Vonage SMS webhooks are GET with query params; support POST just in case
    if req.method == "GET":
        data = dict(req.query_params)
    else:
        try:
            data = await req.json()
        except Exception:
            data = {}

    print("📩 Inbound payload:", data)

    sender = normalize_msisdn(data.get("msisdn") or data.get("from"))
    text = (data.get("text") or "").strip()

    if not sender:
        return JSONResponse({"status": "ignored", "reason": "no sender"})

    # Send auto-reply via the legacy REST SMS API
    url = "https://rest.nexmo.com/sms/json"
    payload = {
        "api_key": VONAGE_API_KEY,
        "api_secret": VONAGE_API_SECRET,
        "to": sender,
        "from": FROM_NUMBER,
        "text": f"Auto-reply: Received '{text}' ✅",
    }

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.post(url, data=payload)
        try:
            jr = r.json()
        except Exception:
            jr = {"status_code": r.status_code, "text": r.text}

    print("📤 Auto-reply response:", jr)
    return {"status": "ok", "vonage": jr}