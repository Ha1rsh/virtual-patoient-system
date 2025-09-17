🩺 VR Patient Simulator

A web-based medical training tool that lets doctors and students interact with virtual patients who respond with different personalities (calm, anxious, rude, overly patient).
Built with React (Vite) frontend + FastAPI backend + Groq/OpenAI/HuggingFace models.

✨ Features

🎭 Multiple Patient Personas – Calm, Anxious, Rude, Overly Patient

💬 Real-time Q&A – Ask questions and receive simulated patient responses

⚡ AI-Powered Responses – Powered by Groq API / OpenAI / HuggingFace

🌐 Full-Stack App – React frontend + FastAPI backend

🎨 Modern UI – Card-based clean design with custom CSS

📂 Project Structure
vr-patient-simulator/
│── backend/
│   ├── app.py              # FastAPI backend
│   ├── patient_api.py      # AI response generator
│   ├── requirements.txt    # Python dependencies
│   └── .env                # API keys & settings
│
│── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main UI
│   │   ├── api.js          # API calls to backend
│   │   ├── main.jsx        # Entry point
│   │   └── index.css       # Styling
│   ├── index.html          # Root HTML
│   └── package.json        # Frontend dependencies

⚙️ Installation
 
cd vr-patient-simulator

2️⃣ Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt


Create .env file:

GROQ_API_KEY=your_groq_api_key
USE_LOCAL_MODEL=false


Run backend:

python -m uvicorn app:app --reload --port 8000


Check 👉 http://127.0.0.1:8000

3️⃣ Frontend Setup (React + Vite)
cd frontend
npm install
npm run dev


Visit 👉 http://localhost:5173

🛠️ Tech Stack

Frontend: React, Vite, CSS

Backend: FastAPI, Python

AI Models: Groq (Llama-3), OpenAI GPT, HuggingFace (Gemma/LLaMA)

Others: Axios/Fetch for API calls, CORS Middleware

🚀 Usage

Start backend (uvicorn app:app --reload --port 8000)

Start frontend (npm run dev)

Open http://localhost:5173

Select a persona 🎭 and ask a medical question 💬

Read the simulated patient response 🧑‍⚕️

⚡ Challenges Faced

CORS issues → solved with FastAPI CORS middleware

API key handling → fixed with .env file and dotenv

Frontend blank page → corrected Vite entry (main.jsx) and HTML setup

💡 Future Improvements

🎙️ Add speech-to-text and text-to-speech

📊 Patient history tracking & session storage

🎨 Better UI with Tailwind/Material UI

🧠 Train custom medical response model

📜 License

 free to use and modify.

screenshots ()
<img width="877" height="874" alt="image" src="https://github.com/user-attachments/assets/d290d46c-13b3-4754-abfd-a12ae4b1bc9c" />

<img width="822" height="847" alt="image" src="https://github.com/user-attachments/assets/f17be358-e97c-4fff-8ca3-0b9bb6f944fe" />

