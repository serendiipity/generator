from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import openai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow CORS (React can connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to save uploaded PDFs temporarily
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# OpenAI API Key (store securely, don't hardcode in production)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate-script")
async def generate_script(pdf: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, pdf.filename)

    # Save the uploaded PDF file
    with open(file_path, "wb") as f:
        content = await pdf.read()
        f.write(content)

    # Extract basic text from the PDF (placeholder)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        pdf_text = f.read()
    
    # Use OpenAI to generate a script
    prompt = f"""
    I have an EDI guideline document that specifies how to map fields.
    Extract and generate a script in JavaScript that follows the instructions in this text:

    {pdf_text}
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
        n=1,
        stop=None
    )

    generated_script = response.choices[0].text.strip()
    
    return {"script": generated_script}