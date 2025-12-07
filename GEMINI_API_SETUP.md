# Gemini API Setup Guide

## Quick Fix for API Key Error

If you're seeing this error:
```
API key not valid. Please pass a valid API key.
```

Follow these steps to fix it:

## Step 1: Get Your Free Gemini API Key

1. **Visit Google AI Studio:**
   - Go to: https://aistudio.google.com/app/apikey
   - Or: https://makersuite.google.com/app/apikey

2. **Sign in with your Google Account**

3. **Create API Key:**
   - Click the **"Get API key"** or **"Create API key"** button
   - Select **"Create API key in new project"** (recommended for beginners)
   - Or select an existing Google Cloud project if you have one

4. **Copy Your API Key:**
   - Your key will look like: `AIzaSyAbCdEf1234567890...` (39 characters)
   - **IMPORTANT:** Copy it immediately - you won't see it again!

## Step 2: Update Your `.env` File

1. **Open the `.env` file** in the root of your project

2. **Find this line** (around line 22):
   ```env
   GEMINI_API_KEY=AIzaSyD1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
   ```

3. **Replace with your real API key:**
   ```env
   GEMINI_API_KEY=AIzaSyYOUR_ACTUAL_KEY_HERE
   ```

4. **Save the file**

## Step 3: Restart the Backend

```bash
# Stop the current server (press Ctrl+C in the terminal)

# Start it again:
uvicorn api.main:app --reload
```

The chatbot should now work with conversational AI responses!

## Verification

Test that it's working:

```bash
# Test endpoint
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is physical AI?"}'
```

You should see a conversational answer instead of an error!

## Alternative: Use Without Gemini (Fallback Mode)

If you don't want to use Gemini API right now, the chatbot will automatically work in **fallback mode**:

- It will still search the book
- It will show relevant text chunks
- But responses won't be as conversational
- You'll see a note: "I'm currently running in simple mode"

**To use fallback mode:**
Just leave the API key as is or set it to empty:
```env
GEMINI_API_KEY=
```

## Troubleshooting

### "API key not valid"
- ✅ Make sure you copied the entire key (should be 39 characters)
- ✅ No extra spaces before or after the key
- ✅ Restarted the backend server after changing `.env`

### "API quota exceeded"
- Gemini has free tier limits
- Check your usage: https://aistudio.google.com/app/apikey
- Wait for quota to reset (usually monthly)
- Or upgrade to paid plan

### "Cannot connect to generativelanguage.googleapis.com"
- Check your internet connection
- Verify no firewall blocking Google APIs
- Try accessing https://generativelanguage.googleapis.com in browser

## Free Tier Limits (Gemini 2.5 Flash)

- **Free quota:** 15 requests per minute, 1 million tokens per day
- **More than enough for development and personal use**
- No credit card required for free tier

## Cost Information (If You Exceed Free Tier)

**Gemini 2.5 Flash Pricing:**
- Input: $0.075 per 1 million tokens
- Output: $0.30 per 1 million tokens

**Example usage:**
- 1 question ≈ 500 input tokens + 200 output tokens
- 1 question ≈ $0.00007 USD
- 1000 questions ≈ $0.07 USD

Very affordable even if you exceed free tier!

## Security Best Practices

1. **Never commit `.env` to git**
   - Already in `.gitignore`, but double-check

2. **Don't share your API key**
   - Treat it like a password

3. **Rotate keys regularly**
   - Create new key every few months
   - Delete old keys in Google AI Studio

4. **Monitor usage**
   - Check https://aistudio.google.com/app/apikey regularly
   - Set up billing alerts if using paid tier

## Getting Help

If you still have issues:

1. **Check backend logs:**
   ```bash
   # Look for error messages when starting the server
   ```

2. **Verify API key format:**
   ```bash
   # Should start with AIzaSy and be 39 characters
   echo $GEMINI_API_KEY  # Linux/Mac
   echo %GEMINI_API_KEY%  # Windows
   ```

3. **Test API key directly:**
   ```bash
   curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=YOUR_KEY" \
     -H 'Content-Type: application/json' \
     -d '{"contents":[{"parts":[{"text":"test"}]}]}'
   ```

## Links

- **Get API Key:** https://aistudio.google.com/app/apikey
- **Gemini Documentation:** https://ai.google.dev/docs
- **Pricing:** https://ai.google.dev/pricing
- **Support:** https://ai.google.dev/support

---

**Need More Help?**
Check the main documentation: `CHATBOT_UPDATE_LLM.md`
