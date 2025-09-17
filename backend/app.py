from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from patient_api import generate_patient_response

app = FastAPI()

# ✅ Add CORS so frontend (localhost:5173) can call backend (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DialogueRequest(BaseModel):
    persona: str
    doctor_question: str

@app.post("/simulate")
def simulate_patient(req: DialogueRequest):
    reply = generate_patient_response(req.persona, req.doctor_question)
    return {"persona": req.persona, "response": reply}

@app.get("/")
def root():
    return {"message": "🩺 VR Patient Simulator API is running!"}
