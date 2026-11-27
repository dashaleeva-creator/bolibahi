import os
from twilio.rest import Client

def send_whatsapp_reminder(to_phone: str, customer_name: str, added_amount: float, total_balance: float):
    if not to_phone:
        return {"status": "skipped", "reason": "No phone number on file"}
        
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_NUMBER")
    
    if not (sid and token):
        return {"status": "mock_sent", "message": f"Namaste {customer_name}, ₹{added_amount} added to your udhaar. Total balance: ₹{total_balance}."}

    client = Client(sid, token)
    msg = client.messages.create(
        body=f"Namaste {customer_name} 🙏\nAapke khate mein ₹{added_amount} jode gaye hain.\nKul baaki (Total Balance): ₹{total_balance}\n- BoliBahi Digital Khata",
        from_=from_whatsapp,
        to=f"whatsapp:{to_phone}"
    )
    return {"status": "sent", "sid": msg.sid}
