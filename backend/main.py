from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow CORS (so React can connect to this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your React frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to save uploaded PDFs temporarily
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/generate-script")
async def generate_script(pdf: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, pdf.filename)

    # Save the uploaded PDF file
    with open(file_path, "wb") as f:
        content = await pdf.read()
        f.write(content)
    
    # For now, we will just return a placeholder script
    script = f"// This is a placeholder script for {pdf.filename}\n"
    script += "console.log('Hello, this is a generated script!');"
    
    return {"script": script}