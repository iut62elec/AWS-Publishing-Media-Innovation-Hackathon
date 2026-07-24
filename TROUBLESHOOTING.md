# Troubleshooting Guide

Quick fixes for common issues participants hit during the hackathon.

---

## AWS Credential Issues

### `ExpiredTokenException` or `The security token included in the request is expired`

Your session credentials have expired (they last ~1-3 hours).

**Fix:** Go back to https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US, get fresh credentials, and re-export them in your terminal.

### `AccessDeniedException` or `is not authorized to perform`

The sandbox account restricts certain actions.

**Fix:** You have access to Bedrock, Polly, Textract, Translate, Comprehend, and S3. You do NOT have access to create IAM roles, Lambda functions, or VPCs. Keep it local — you likely don't need to deploy.

---

## Bedrock Model Issues

### `ResourceNotFoundException: Access denied. This Model is marked by provider as Legacy`

You're using an old model ID. Claude 3 Sonnet/Haiku base models are now legacy.

**Fix:** Use inference profile IDs instead:

```python
# WRONG (legacy, won't work)
modelId='anthropic.claude-3-sonnet-20240229-v1:0'
modelId='anthropic.claude-3-haiku-20240307-v1:0'

# CORRECT (active inference profiles)
modelId='us.anthropic.claude-haiku-4-5-20251001-v1:0'   # Fast + cheap
modelId='us.anthropic.claude-sonnet-4-5-20250929-v1:0'  # Best quality
```

### `ValidationException: Invocation of model ID ... with on-demand throughput isn't supported`

Same issue — you need the `us.` prefixed inference profile ID, not the base model ID.

**Fix:** Add `us.` prefix. Change `anthropic.claude-haiku-4-5-20251001-v1:0` to `us.anthropic.claude-haiku-4-5-20251001-v1:0`.

### `AccessDeniedException: ... is not available for this account`

Some models (like Opus) require separate access approval and aren't available on sandbox accounts.

**Fix:** Use models that work immediately:
```python
# These work on sandbox accounts:
modelId='us.anthropic.claude-sonnet-4-6'               # Best available
modelId='us.anthropic.claude-sonnet-4-5-20250929-v1:0' # Also excellent
modelId='us.anthropic.claude-haiku-4-5-20251001-v1:0'  # Fastest/cheapest
```

### How to list all available models

```python
import boto3
client = boto3.client('bedrock', region_name='us-east-1')
profiles = client.list_inference_profiles()
for p in profiles['inferenceProfileSummaries']:
    if 'anthropic' in p['inferenceProfileId']:
        print(f"{p['inferenceProfileId']} - {p.get('status')}")
```

---

## Amazon Polly Issues

### `InvalidSsmlException: Unsupported Neural feature`

Polly's Neural engine does NOT support `<prosody>`, `<emphasis>`, `<amazon:effect>`, or most SSML tags.

**Fix:** With Neural voices, only use:
- `<speak>` (required wrapper)
- `<break time="500ms"/>` (pauses)

```python
# WRONG — will fail with Neural engine
ssml = '<speak><prosody rate="slow">Hello world</prosody></speak>'
ssml = '<speak><emphasis level="strong">Important!</emphasis></speak>'

# CORRECT — works with Neural engine
ssml = '<speak>Hello world. <break time="500ms"/> How are you?</speak>'
```

**Alternative:** Use `TextType='text'` instead of `TextType='ssml'` to avoid SSML entirely:
```python
polly.synthesize_speech(
    Text='Hello world. How are you?',
    TextType='text',
    OutputFormat='mp3',
    VoiceId='Matthew',
    Engine='neural'
)
```

### `TextLengthExceededException`

Polly has a 3000-character limit per `synthesize_speech` call.

**Fix:** Split your text into chunks under 3000 characters, synthesize each separately, and stitch them together with `pydub`:

```python
from pydub import AudioSegment
import tempfile, os

combined = AudioSegment.empty()
for chunk in text_chunks:
    audio_bytes = synthesize(chunk)
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
        f.write(audio_bytes)
        segment = AudioSegment.from_mp3(f.name)
        combined += segment
        os.unlink(f.name)
combined.export('final.mp3', format='mp3')
```

---

## Web App / Browser Issues

### `Unexpected token '<', "<html> <h"... is not valid JSON`

Your JavaScript `fetch()` calls are using absolute paths that go to the CloudFront proxy root instead of your app.

**Fix:** Remove the leading `/` from all fetch URLs:

```javascript
// WRONG
const resp = await fetch('/analyze', { method: 'POST', ... });
const resp = await fetch('/api/submit', { method: 'POST', ... });

// CORRECT
const resp = await fetch('analyze', { method: 'POST', ... });
const resp = await fetch('api/submit', { method: 'POST', ... });
```

### `ERR_CONNECTION_REFUSED` or page won't load

Your Flask server isn't running, or is on the wrong port.

**Fix:**
1. Make sure your app runs on `0.0.0.0` (not `127.0.0.1`):
   ```python
   app.run(host='0.0.0.0', port=5000)
   ```
2. Access via: `https://YOUR-CLOUDFRONT-ID.cloudfront.net/code/ports/5000/`
3. Make sure the port number in the URL matches your app's port.

### App loads but API calls fail silently

Check the browser developer console (F12 → Console tab) for errors. Common causes:
- Mixed content (HTTP vs HTTPS) — your app is HTTP but CloudFront is HTTPS. This should work through the proxy, but if not, it's a proxy issue.
- CORS errors — shouldn't happen since frontend and backend are same-origin through the proxy.

---

## Python / Environment Issues

### `ModuleNotFoundError: No module named 'flask'` (or boto3, pydub, etc.)

You haven't activated your virtual environment or haven't installed dependencies.

**Fix:**
```bash
source venv/bin/activate
pip install flask boto3 pydub requests
```

### `pydub` or `AudioSegment` fails with "Couldn't find ffmpeg"

**Fix:**
```bash
sudo apt-get install -y ffmpeg
```

### `No module named 'pip'`

**Fix:**
```bash
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip install flask boto3 pydub requests
```

---

## General Tips

### My Claude Code session timed out / context got too long

Start a new conversation. Your files are still on disk. Tell Claude Code:
> "I'm building [idea name]. Read my PLAN.md and REQUIREMENTS.md to catch up, then continue from where we left off."

### How do I know what port my app is on?

```bash
ss -tlnp | grep LISTEN
```

### How do I kill a stuck server?

```bash
pkill -f "python3 app.py"
```
Or find and kill by port:
```bash
lsof -ti:5000 | xargs kill -9
```

### My AWS calls are slow

Bedrock calls typically take 5-20 seconds depending on model and prompt size. This is normal. Use Haiku 4.5 for faster responses during development, switch to Sonnet 4.5 for the demo if quality matters.
