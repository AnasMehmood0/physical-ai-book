from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Physical AI Chatbot API",
        "status": "online",
        "note": "Full RAG functionality coming soon with Qdrant Cloud integration"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}
