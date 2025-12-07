# Chatbot Update: From Search to Conversational AI

## Overview

The chatbot has been upgraded from a simple vector search system to a full **Retrieval-Augmented Generation (RAG)** chatbot that provides conversational explanations about the Physical AI book.

## What Changed

### Before (Search-Only)
- User asks a question
- System returns relevant text chunks
- Frontend displays raw search results
- User has to read through chunks manually

### After (RAG Chatbot)
- User asks a question
- System retrieves relevant context from the book
- **Gemini LLM generates a conversational explanation**
- Frontend displays human-like answer
- Sources are shown for reference

## Architecture

```
User Question
      ↓
[Vector Search] → Retrieves 3 most relevant chunks
      ↓
[LLM (Gemini)] → Generates conversational answer
      ↓
User gets: Natural language explanation + Sources
```

## New Components

### 1. LLM Service (`api/llm_service.py`)

**Purpose:** Integrates Google Gemini API to generate conversational responses

**Key Features:**
- RAG prompt engineering for educational explanations
- Context-aware answer generation
- Error handling and fallbacks
- Configurable temperature and token limits

**Key Methods:**
```python
def generate_answer(question, context_chunks, max_tokens=500)
    # Generates conversational answer from retrieved context

def _create_prompt(question, context)
    # Creates RAG prompt with instructions for the LLM
```

### 2. Updated API Endpoint

**Endpoint:** `POST /ask`

**New Response Format:**
```json
{
  "answer": "Physical AI refers to artificial intelligence systems...",
  "sources": [
    {
      "payload": {
        "chapter_id": "01-introduction",
        "source": "intro.md",
        "text": "..."
      },
      "score": 0.85
    }
  ]
}
```

**Old Format (for comparison):**
```json
{
  "results": [...]  // Just raw chunks
}
```

## Configuration

### Gemini API Key

The chatbot uses Google Gemini API. Make sure your API key is set in `.env`:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

**Note:** The example key in the repo is fake. Get a real API key from:
https://makersuite.google.com/app/apikey

### LLM Settings

Edit `api/llm_service.py` to customize:

```python
class LLMService:
    def __init__(self, model="gemini-2.5-flash"):  # Model choice
        # ...

    def generate_answer(..., max_tokens=500):  # Response length
        # ...

    "temperature": 0.7,   # Creativity (0-1)
    "topP": 0.8,         # Nucleus sampling
    "topK": 40           # Top-k sampling
```

## RAG Prompt Template

The chatbot uses a carefully crafted prompt to guide the LLM:

```
You are a helpful AI assistant for the Physical AI Book.
Your role is to explain concepts from the book in a clear,
educational, and friendly manner.

Context from the book:
[Retrieved chunks]

User Question: [Question]

Instructions:
1. Answer based ONLY on the provided context
2. If context doesn't have info, say "I don't have enough information"
3. Be conversational and helpful, like a knowledgeable tutor
4. Cite which chapter/source you're referencing
5. Provide examples if they're in the context
6. Keep answer concise but informative (2-4 paragraphs)
```

## Frontend Changes

### Updated UI
- Bot messages now show natural language explanations
- Sources appear below the answer in a collapsible section
- More conversational tone in the interface

### New Message Format
```typescript
interface Message {
  text: string;        // The LLM-generated answer
  sources?: SearchResult[];  // Reference sources
  // ...
}
```

## Files Modified

### Backend
1. **NEW** `api/llm_service.py` - Gemini LLM integration
2. **MODIFIED** `api/main.py` - Updated /ask endpoint
3. **MODIFIED** `api/ingest.py` - Stores text content in payload
4. **MODIFIED** `api/requirements.txt` - Added `requests`
5. **MODIFIED** `.env` - Gemini API configuration

### Frontend
6. **MODIFIED** `web/src/services/chatbotApi.ts` - New response types
7. **MODIFIED** `web/src/components/GlobalChatWidget.tsx` - Display answers
8. **MODIFIED** `web/src/components/GlobalChatWidget.module.css` - Sources styling

## Installation & Setup

### 1. Install New Dependencies

```bash
cd api
pip install requests
```

Or reinstall all:
```bash
pip install -r requirements.txt
```

### 2. Set Gemini API Key

Edit `.env`:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Recreate Vector Database

The database needs to be recreated to include text content:

```bash
# Delete old database
rm -rf qdrant_storage

# Restart API (will recreate with text content)
uvicorn api.main:app --reload
```

### 4. Test the Chatbot

Start backend and frontend, then try asking:
- "What is physical AI?"
- "Explain how SLAM works"
- "What are the ethical considerations in robotics?"

## Example Interaction

**User:** "What is physical AI?"

**Old Response (Search):**
```
Result 1 (85% match)
Source: intro.md
Chapter: 01-introduction

Result 2 (78% match)
Source: intro.md
Chapter: 01-introduction
```

**New Response (RAG Chatbot):**
```
Physical AI refers to artificial intelligence systems that interact
with and learn from the physical world through embodied agents like
robots. According to Chapter 1, it combines traditional AI techniques
with physical sensors and actuators, enabling machines to perceive
and manipulate their environment.

The book explains that physical AI systems face unique challenges
compared to pure software AI, such as dealing with sensor noise,
real-time constraints, and safety considerations in human-robot
interaction.

Sources:
📄 intro.md - Chapter: 01-introduction (85% match)
📄 intro.md - Chapter: 01-introduction (78% match)
```

## Benefits

1. **Natural Conversation** - Chatbot explains concepts like a tutor
2. **Context-Aware** - Answers are synthesized from multiple sources
3. **Educational** - Focuses on teaching, not just retrieving
4. **Source Citations** - Users can verify information
5. **Better UX** - No need to read through raw chunks

## Limitations

1. **API Costs** - Gemini API calls cost money (but minimal with flash model)
2. **Latency** - Responses take 1-3 seconds (LLM generation time)
3. **Context Window** - Limited to ~3 relevant chunks
4. **API Key Required** - Won't work without valid Gemini key
5. **Hallucination Risk** - LLM might occasionally add details not in context

## Troubleshooting

### "LLM service initialization failed"
- Check your Gemini API key is valid
- Verify internet connection
- Check API key has correct permissions

### "Error generating answer"
- Check Gemini API quota/billing
- Look at backend logs for specific error
- Verify API endpoint is accessible

### Responses are too short/long
- Adjust `max_tokens` in `llm_service.py`
- Modify prompt to request different length

### Responses include information not in book
- LLM is hallucinating - strengthen prompt instructions
- Reduce temperature for more factual responses
- Add more explicit constraints in prompt

## Future Enhancements

Potential improvements:
- [ ] Conversation memory (remember previous questions)
- [ ] Follow-up question suggestions
- [ ] Multi-turn conversations
- [ ] Adjustable response length
- [ ] Different explanation styles (beginner/advanced)
- [ ] Code example generation
- [ ] Image/diagram references
- [ ] Quiz generation from content

## Cost Estimates

**Gemini 2.5 Flash:**
- Input: $0.075 per 1M tokens
- Output: $0.30 per 1M tokens

**Typical Question:**
- Input: ~500 tokens (context + question)
- Output: ~200 tokens (answer)
- Cost: ~$0.00007 per question

**1000 questions ≈ $0.07 USD**

## API Key Security

**Important:**
- Never commit `.env` to git
- Use separate keys for dev/production
- Rotate keys regularly
- Monitor API usage
- Set spending limits in Google Cloud Console

---

**Version:** 2.0.0
**Date:** 2025-12-07
**Type:** Major Feature Update
