import React, { useState } from "react";
import "./App.css"

function App() {
  const [pdf, setPdf] = useState(null);
  const [script, setScript] = useState("");

  // Handle file upload
  const handleUpload = (e) => {
    setPdf(e.target.files[0]);
  };

  // Generate script (placeholder for now)
  const generateScript = () => {
    setScript("This is where the generated script will appear.");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Script Generator</h2>
      <input type="file" accept=".pdf" onChange={handleUpload} />
      <button onClick={generateScript}>Generate Script</button>
      <br />
      <textarea
        value={script}
        onChange={(e) => setScript(e.target.value)}
        rows={15}
        cols={80}
        style={{ marginTop: "20px" }}
      />
      <br />
      <button onClick={() => navigator.clipboard.writeText(script)}>Copy Script</button>
    </div>
  );
}

export default App;