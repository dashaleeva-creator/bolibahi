# 🎙️ BoliBahi — Voice-First Inventory & Udhaar Ledger

**BoliBahi** is a hands-free, voice-first bookkeeping and inventory assistant built for India's 60M+ micro-retailers (*kirana* stores, pharmacies, hardware shops, and street vendors). 

Shopkeepers manage daily sales, customer credit (*udhaar*), and stock levels simply by speaking in natural Hinglish or regional Indian languages—eliminating paper notebooks (*khatas*) and slow smartphone typing during peak rush hours.

---

## 🚨 The Problem
* **Daily Cash & Credit Leaks:** During busy morning and evening rush hours, regular customers take goods on *udhaar* and say *"write it down later,"* leading to forgotten entries.
* **Typing Friction:** Typing names, items, and quantities on a small keyboard while five customers wait in line is too slow.
* **Language Barrier:** Most accounting apps rely on complex English menus and financial jargon.
* **Unnoticed Stockouts:** Busy solo shopkeepers forget to note down low-stock items, losing repeat sales.

## ✨ Key Features
* **🗣️ Multilingual Voice Logging:** Understands rapid Hinglish, Hindi, Odia, Marathi, and Tamil with local shop terminology (*"Ramesh ke khate mein do kilo chini aur ek sabun likh do"*).
* **📒 Automated Udhaar Tracking:** Extracts customer names, items, quantities, and prices to update customer credit balances automatically.
* **📦 Real-Time Inventory Deduction:** Deducts sold items from shop stock simultaneously and flags low inventory.
* **🔊 Instant Voice Readback:** Confirms the recorded transaction and updated balance aloud in the shopkeeper's language.
* **📲 WhatsApp Payment Reminders:** Automatically sends a transparent digital receipt and balance update to the customer via WhatsApp.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **Speech-to-Text & NLU:** OpenAI Whisper + GPT-4o-mini (Structured Outputs) *(extensible to Bhashini / Sarvam AI)*
* **Database:** SQLite (MVP) / PostgreSQL
* **Messaging:** Twilio WhatsApp Business API

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com
cd bolibahi
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Add your OPENAI_API_KEY and Twilio credentials inside .env
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```
Open `http://127.0.0` in your browser to test the `/process-text` and `/process-voice` endpoints interactively.

---

## 🧪 Example Voice Command
**Shopkeeper speaks:**
> *"Ramesh ke khate mein 2 kilo chini aur 1 sabun add kar do."*

**BoliBahi Output:**
* **Customer:** Ramesh
* **Items:** 2 kg Sugar, 1 pc Soap
* **Ledger Update:** +₹120 added to Ramesh's *udhaar*
* **Voice Reply:** *"Ramesh ke khate mein ₹120 jod diye gaye hain. Kul baaki ₹370 hai."*
* **WhatsApp Triggered:** Automated balance summary sent to Ramesh.
