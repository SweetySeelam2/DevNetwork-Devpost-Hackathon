# OmniCare CX Agent – AI-Powered SMS Auto-Responder

## 📌 Overview
- OmniCare CX Agent is a lightweight yet powerful **SMS auto-responder** built using **Vonage APIs** and **FastAPI**.  
- It enables instant acknowledgment of customer inquiries via SMS, ensuring no message is ever left unanswered.  

This project was built for the **DevNetwork Hackathon 2025** under the **Vonage Challenge #2: Transforming Customer Service with Multi-channel Interactions**.

---

## 🚀 Features
- Receive inbound SMS on a Vonage virtual number.
- Auto-reply instantly with configurable responses.
- Webhook-driven via **FastAPI**.
- Secure tunneling with **ngrok** for webhook exposure.
- Logs and tracks messages in real time.
- Extensible to **WhatsApp, Messenger, and Viber** via Vonage Messages API.

---

## 🛠️ Tech Stack
- **Languages/Frameworks**: Python, FastAPI  
- **APIs**: Vonage SMS API  
- **Tools**: ngrok, curl, dotenv  
- **Environment**: Localhost + virtualenv  
- **Future integrations**: PostgreSQL, MongoDB, Hugging Face NLP  

---

## ⚙️ Setup & Installation

**1. Clone the repository:**
```bash
   git clone https://github.com/SweetySeelam2/DevNetwork-Devpost-Hackathon.git
   cd DevNetwork-Devpost-Hackathon
```

**2. Create a virtual environment & install dependencies:**
```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt
```

**3. Create a .env file (text file):**
```ini
    VONAGE_API_KEY=your_api_key
    VONAGE_API_SECRET=your_api_secret
    VONAGE_FROM=+18334296093   # Vonage virtual/toll-free number
    VONAGE_TO=+1XXXXXXXXXX     # test mobile number
```

**4. Run the FastAPI app:**
```bash
    uvicorn app:app --reload --port 8000
```

**5. Start ngrok:**
```bash
    ngrok http 8000
```
*Copy the HTTPS forwarding URL and paste it in your Vonage Inbound Webhook URL.*

---

## 📩 Testing

Send a message to the Vonage number (or simulate with curl):

```bash
curl.exe "https://<your-ngrok>.ngrok-free.app/inbound?msisdn=%2B1YOUR_NUMBER&to=%2B18334296093&text=Hello%20from%20curl"
```

**Expected:**

- Logs show inbound payload.

- Auto-reply sent to your number.

- Delivery report appears in Vonage dashboard.

---

## 🏆 Hackathon Devpost Submission

- **Team**                                                                                                                   
  Solo: Sweety Seelam

- **Track:** Vonage Challenge #2 – Transforming Customer Service

- **Demo Video:** https://youtu.be/A3XbiIEPNAY

- **GitHub Repo:** [DevNetwork-Devpost-Hackathon](https://github.com/SweetySeelam2/DevNetwork-Devpost-Hackathon)

---

## 🔮 Future Work
- AI/NLP for contextual replies.

- Sentiment analysis & escalation.

- Multi-channel integration (WhatsApp, Messenger, Viber).

- Cloud deployment (AWS/GCP/Azure).

- CRM integration (Salesforce, HubSpot).

---

## 🏆 Blurb - Judging Criteria

**Progress – How much progress did you make?**

- Configured Vonage toll-free number + application.

- Built a working FastAPI backend with inbound SMS handling + auto-reply.

- Integrated ngrok for webhook testing and exposed live endpoints.

- Demonstrated end-to-end flow: inbound SMS → FastAPI → auto-reply → Vonage logs.

*✅ Shows real, working code and full-stack progress beyond just an idea.*


**Concept – Does it solve a real problem?**

- Businesses lose customers when texts go unanswered.

- OmniCare CX Agent solves this by providing instant SMS auto-replies, ensuring 24/7 acknowledgment.

- Improves customer experience (CX) and prevents lost opportunities.

*✅ Tackles a universal pain point with a simple, effective solution.*


**Feasibility – Could this become a startup or company?**

- SMS auto-response is just the start → scalable to WhatsApp, Messenger, Viber, and Voice bots.

- Future integrations: AI/NLP for smart replies, CRM (HubSpot, Salesforce), cloud SaaS deployment.

- Monetization potential: SMB subscriptions or per-message enterprise pricing.

*✅ Clear business model + scalability path for a real-world startup.*

---

## 📜 License
MIT License © 2025 Sweety Seelam