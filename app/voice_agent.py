import os
import json
from openai import OpenAI
from pydantic import BaseModel
from typing import List, Optional

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ItemEntry(BaseModel):
    item_name: str
    quantity: float
    unit: str
    estimated_price: float

class LedgerAction(BaseModel):
    intent: str  # "add_credit", "record_payment", "check_balance"
    customer_name: str
    items: List[ItemEntry]
    total_amount: float
    spoken_confirmation: str  # Natural response in user's language (Hinglish/Hindi/Odia/etc.)

def transcribe_audio(file_path: str) -> str:
    """Transcribes Hinglish / Indian regional languages using Whisper."""
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            prompt="Hinglish, Hindi, Odia, Marathi, Tamil kirana shop ledger terms like udhaar, kilo, chini, sabun, hisab."
        )
    return transcript.text

def parse_shopkeeper_command(transcript_text: str) -> LedgerAction:
    """Extracts structured ledger and inventory updates from messy spoken text."""
    system_prompt = """
    You are BoliBahi, a voice assistant for Indian small shopkeepers.
    Extract the customer name, items sold, quantities, and total amount from the shopkeeper's speech.
    If prices aren't mentioned, estimate standard Indian retail prices in INR.
    Generate a short, polite 'spoken_confirmation' in the same language/Hinglish mix the user spoke.
    """
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript_text}
        ],
        response_format=LedgerAction
    )
    return response.choices[0].message.parsed
