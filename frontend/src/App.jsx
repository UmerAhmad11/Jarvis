import { useState } from "react";
import Visualizer from "./Visualizer";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [thinking, setThinking] = useState(false);

  const askJarvis = async () => {
    if (!prompt.trim()) return;

    setThinking(true);
    setResponse("🤖 Thinking...");

    try {
      const res = await fetch("http://127.0.0.1:5000/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse("❌ Error: Backend not responding.");
    }

    setThinking(false);
    setPrompt("");
  };

  return (
    <div className="app">
      <h1 className="title">🤖 Jarvis Assistant</h1>

      {thinking && <Visualizer />}

      <input
        type="text"
        placeholder="Ask Jarvis something..."
        className="prompt-input"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && askJarvis()}
      />

      <button className="ask-button" onClick={askJarvis}>
        Ask
      </button>

      <p className="response">{response}</p>
    </div>
  );
}

export default App;
