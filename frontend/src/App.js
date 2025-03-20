import React, { useState } from "react";
import axios from "./api";
import "./index.css"; // Import CSS file

function App() {
  const [url, setUrl] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ingestURL = async () => {
    await axios.post("/ingest", { url });
    alert("Content ingested successfully!");
  };

  const askQuestion = async () => {
    const response = await axios.post("/ask", { question });
    setAnswer(response.data.answer);
  };

  return (
    <div className="container">
      <h2>Web Q&A Tool</h2>
      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL"
      />
      <button onClick={ingestURL}>Ingest</button>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question"
      />
      <button onClick={askQuestion}>Ask</button>

      {answer && <div className="answer-box"><strong>Answer:</strong> {answer}</div>}
    </div>
  );
}

export default App;
