// frontend/src/api.js
const API_BASE = "http://127.0.0.1:8000";

export async function askPatient(persona, doctor_question) {
  try {
    const res = await fetch(`${API_BASE}/simulate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ persona, doctor_question }),
    });

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();
    return data.response;
  } catch (err) {
    console.error("❌ API Error:", err);
    return "⚠️ Failed to reach patient simulator.";
  }
}
