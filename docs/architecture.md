# OmniCare CX Agent – Project Documentation

## 📌 Architecture Overview
- The OmniCare CX Agent is a lightweight SMS auto-responder powered by Vonage APIs and FastAPI.  
- It listens for inbound SMS on a Vonage virtual number, processes them via FastAPI, and replies instantly.

---

### 🔄 Flow Diagram
[User SMS] → [Vonage Virtual Number] → [Ngrok Tunnel] → [FastAPI /inbound Endpoint] → [Auto-reply via Vonage SMS API]

---

### 🛠 Components
- **Vonage SMS API** → receives and sends SMS.  
- **FastAPI App (`app.py`)** → webhook handler & auto-reply logic.  
- **Ngrok** → secure tunnel exposing localhost for inbound delivery.  
- **send_sms.py** → helper for testing outbound SMS.  
- **Vonage Dashboard** → logs, monitoring, and troubleshooting.

---

## 📌 Demo Flow
1. User sends SMS to the Vonage virtual number.  
2. Vonage forwards message via webhook (ngrok → FastAPI).  
3. FastAPI `/inbound` logs the message and triggers an auto-reply.  
4. Vonage Dashboard shows outbound attempt (logs).  
5. User sees instant acknowledgment.  

---

## 📌 Deployment Notes
- Works locally with ngrok.  
- Can be containerized (Docker) for cloud deployment.  
- Recommended for hackathon demo: **Terminal + Ngrok + Vonage Logs**.  