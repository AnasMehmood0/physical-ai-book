from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat, documents

app = FastAPI(title="Physical AI Book RAG API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(documents.router, prefix="/api", tags=["documents"])

@app.get("/")
def read_root():
    return {"message": "Physical AI Book RAG API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}