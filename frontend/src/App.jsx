import React, { useState } from "react";
import { askPatient } from "./api";
import "./index.css";

export default function App() {
  const [persona, setPersona] = useState("calm");
  const [query, setQuery] = useState("");
  const [chat, setChat] = useState([]); // stores full conversation
  const [loading, setLoading] = useState(false);

  const personas = {
    calm: "😌 Calm",
    anxious: "😟 Anxious",
    rude: "😠 Rude",
    patient: "🙂 Overly Patient",
  };

  const handleAsk = async () => {
    if (!query.trim()) return;

    // Add doctor question to chat
    setChat((prev) => [...prev, { sender: "doctor", text: query }]);

    setLoading(true);

    const res = await askPatient(persona, query);

    // Add patient response
    setChat((prev) => [...prev, { sender: "patient", text: res }]);

    setQuery("");
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h2>🩺 VR Patient Simulator</h2>

      <div className="persona-select">
        <label>Choose Patient Persona:</label>
        <select value={persona} onChange={(e) => setPersona(e.target.value)}>
          {Object.entries(personas).map(([key, label]) => (
            <option key={key} value={key}>
              {label}
            </option>
          ))}
        </select>
      </div>

      {/* Chat window */}
      <div className="chat-box">
        {chat.map((msg, i) => (
          <div
            key={i}
            className={`chat-bubble ${msg.sender === "doctor" ? "doctor" : "patient"}`}
          >
            <strong>{msg.sender === "doctor" ? "👨‍⚕️ Doctor:" : personas[persona] + " Patient:"}</strong>
            <p>{msg.text}</p>
          </div>
        ))}

        {loading && <div className="typing">Patient is typing...</div>}
      </div>

      {/* Input area */}
      <div className="input-box">
        <textarea
          placeholder="Ask the patient about symptoms..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleAsk}>Send</button>
      </div>
    </div>
  );
}
