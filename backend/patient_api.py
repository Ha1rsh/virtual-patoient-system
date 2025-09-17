import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flags
USE_LOCAL_MODEL = os.getenv("USE_LOCAL_MODEL", "false").lower() == "true"
USE_GROQ = bool(os.getenv("GROQ_API_KEY"))

# ---- Option 1: Groq API ----
if USE_GROQ:
    from groq import Groq
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- Option 2: OpenAI API ----
elif os.getenv("OPENAI_API_KEY"):
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

# ---- Option 3: HuggingFace local model ----
if USE_LOCAL_MODEL:
    from transformers import pipeline
    import torch
    device = 0 if torch.cuda.is_available() else -1
    generator = pipeline(
        "text-generation",
        model="google/gemma-2b-it",   # replace with your fine-tuned model path
        device=device,
        torch_dtype=torch.float16,
    )


def generate_patient_response(persona: str, doctor_question: str) -> str:
    """
    Generate a patient response based on persona + doctor's question.
    Supports Groq, OpenAI, or local HuggingFace models.
    """
    prompt = (
        f"You are a virtual patient in a medical simulation.\n"
        f"Your persona is '{persona}'.\n"
        f"The doctor asks: {doctor_question}\n"
        f"Answer as the patient, staying true to the persona.\n"
        f"Keep responses realistic and conversational."
    )

    # ---- Option 1: Groq ----
    if USE_GROQ:
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a simulated patient."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=200,
            )
            # ✅ FIX: use .content (not ["content"])
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"⚠️ Groq API Error: {str(e)}"

    # ---- Option 2: OpenAI ----
    elif os.getenv("OPENAI_API_KEY"):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a simulated patient."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=200,
            )
            return completion.choices[0].message["content"].strip()
        except Exception as e:
            return f"⚠️ OpenAI API Error: {str(e)}"

    # ---- Option 3: Local HuggingFace ----
    elif USE_LOCAL_MODEL:
        try:
            outputs = generator(
                prompt,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.8,
                top_p=0.9,
            )
            return outputs[0]["generated_text"].replace(prompt, "").strip()
        except Exception as e:
            return f"⚠️ Local Model Error: {str(e)}"

    else:
        return "⚠️ No model is configured. Please set GROQ_API_KEY, OPENAI_API_KEY, or USE_LOCAL_MODEL."
