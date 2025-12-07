# Quick Start: RAG Chatbot

## ✅ You're Ready to Go!

Your chatbot is now configured with:
- **Gemini 2.5 Flash** for conversational AI
- **Vector search** for finding relevant content
- **RAG (Retrieval-Augmented Generation)** for smart explanations

## Start the System

### 1. Start Backend (Terminal 1)

```bash
# Make sure you're in the project root
uvicorn api.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     LLM service initialized successfully
```

### 2. Start Frontend (Terminal 2)

```bash
cd web
npm start
```

You should see:
```
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

## Test the Chatbot

1. Open http://localhost:3000
2. Click the chat button (💬) in bottom-right
3. Ask questions like:
   - "What is physical AI?"
   - "Explain SLAM in simple terms"
   - "What are sensors and actuators?"
   - "Tell me about robot ethics"

## What You'll See

### Conversational AI Response (with Gemini 2.5 Flash)
```
Physical AI refers to artificial intelligence systems that interact
with and learn from the physical world through embodied agents like
robots. According to Chapter 1, it combines traditional AI techniques
with physical sensors and actuators...

Sources:
📄 intro.md - Chapter: 01-introduction (85% match)
```

### Fallback Mode (if API key issue)
```
Based on the book content, here's what I found:

From intro.md (Chapter: 01-introduction):
[Raw text from the book]

💡 Note: I'm currently running in simple mode...
```

## Common Issues & Quick Fixes

### "API key not valid"
```bash
# Update .env with your real key from:
# https://aistudio.google.com/app/apikey

# Then restart backend
```

### "LLM service initialization failed"
The chatbot will automatically work in fallback mode - still functional!

### Chat widget not appearing
```bash
cd web
npm run clear
npm start
```

### Backend port already in use
```bash
# Use a different port
uvicorn api.main:app --reload --port 8001

# Then update web/src/config/chatbot.config.ts:
apiUrl: 'http://localhost:8001'
```

## Features

✅ **Conversational AI** - Natural language explanations
✅ **Context-Aware** - Answers based on book content
✅ **Source Citations** - Shows which chapters were used
✅ **Fallback Mode** - Works even without API key
✅ **Real-time Search** - Fast vector similarity search
✅ **Responsive UI** - Works on desktop and mobile

## Model Info

**Current Model:** Gemini 2.5 Flash
- Fast and efficient
- Great for educational content
- Free tier: 15 RPM, 1M tokens/day
- Cost: ~$0.00007 per question

## Customization

### Change Response Length
Edit `api/llm_service.py`:
```python
def generate_answer(..., max_tokens=500):  # Increase for longer answers
```

### Adjust Search Results
Edit `.env`:
```env
CHUNK_SIZE=512        # Larger chunks = more context
CHUNK_OVERLAP=64      # More overlap = better continuity
```

### Change API URL (Frontend)
Edit `web/src/config/chatbot.config.ts`:
```typescript
apiUrl: 'http://localhost:8000',  // Change port or domain
debug: true,                       // Enable debug logging
```

## Files Structure

```
.env                     # Your configuration (API keys, settings)
api/
  ├── llm_service.py     # Gemini 2.5 Flash integration
  ├── main.py            # FastAPI backend
  ├── vector_store.py    # Vector search
  └── ingest.py          # Document processing
web/
  └── src/
      ├── components/GlobalChatWidget.tsx  # Chat UI
      ├── services/chatbotApi.ts           # API client
      └── config/chatbot.config.ts         # Frontend config
```

## Documentation

- **Setup Guide:** `GEMINI_API_SETUP.md`
- **Full Documentation:** `CHATBOT_UPDATE_LLM.md`
- **Implementation Details:** `CHATBOT_IMPLEMENTATION.md`

## Get Help

1. Check backend logs for errors
2. Check browser console (F12) for frontend issues
3. Verify API key at: https://aistudio.google.com/app/apikey
4. Read `GEMINI_API_SETUP.md` for troubleshooting

---

**Enjoy your AI-powered book assistant! 🤖📚**
