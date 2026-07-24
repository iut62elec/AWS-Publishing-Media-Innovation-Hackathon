# Participant Setup Guide

This guide gets your environment ready before you start building. Complete these steps first, then follow the [BUILD-GUIDE.md](BUILD-GUIDE.md).

---

## 1. Get Your AWS Credentials

1. Go to your **Event Dashboard**: https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US
2. Click **"Get AWS CLI credentials"** (or Open AWS Console → copy credentials)
3. You will see four values:
   ```
   export AWS_DEFAULT_REGION="us-east-1"
   export AWS_ACCESS_KEY_ID="ASIA..."
   export AWS_SECRET_ACCESS_KEY="..."
   export AWS_SESSION_TOKEN="..."
   ```
4. Copy **all four lines** — you'll paste them into your terminal in the next step.

> **Important:** These credentials expire. If you get `ExpiredTokenException` later, come back to the dashboard and get fresh ones.

---

## 2. Open Claude Code

You are using Claude Code in a browser-based environment. Your workspace URL looks like:

```
https://YOUR-ID.cloudfront.net/code/
```

This is a full terminal with Claude Code already installed. You can start working immediately.

---

## 3. Set Your AWS Credentials

In the Claude Code terminal, paste the four export lines from Step 1:

```bash
export AWS_DEFAULT_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
```

---

## 4. Verify Everything Works (Smoke Test)

Run this to confirm your environment is ready:

```bash
python3 -c "
import boto3, json

# Test 1: AWS Identity
sts = boto3.client('sts', region_name='us-east-1')
identity = sts.get_caller_identity()
print(f'AWS Account: {identity[\"Account\"]}')
print(f'Identity: {identity[\"Arn\"]}')
print('STS: OK')

# Test 2: Bedrock model access
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
response = bedrock.invoke_model(
    modelId='us.anthropic.claude-haiku-4-5-20251001-v1:0',
    body=json.dumps({
        'anthropic_version': 'bedrock-2023-05-31',
        'max_tokens': 50,
        'messages': [{'role': 'user', 'content': 'Say hello in one word'}]
    }),
    contentType='application/json',
    accept='application/json'
)
result = json.loads(response['body'].read())
print(f'Bedrock: OK - {result[\"content\"][0][\"text\"]}')

# Test 3: Polly
polly = boto3.client('polly', region_name='us-east-1')
resp = polly.synthesize_speech(Text='Hello world', OutputFormat='mp3', VoiceId='Matthew', Engine='neural')
audio_bytes = len(resp['AudioStream'].read())
print(f'Polly: OK - {audio_bytes} bytes')

print()
print('ALL CHECKS PASSED — you are ready to build!')
"
```

You should see:
```
AWS Account: ...
Identity: ...
STS: OK
Bedrock: OK - Hello
Polly: OK - 5820 bytes

ALL CHECKS PASSED — you are ready to build!
```

If any step fails, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

---

## 5. Install Common Dependencies

Most projects will need these:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask boto3 pydub requests
sudo apt-get install -y ffmpeg
```

---

## 6. Important: Web App Access (Read This!)

Your web apps are accessible through a **CloudFront proxy**. When you run a Flask/web server on port 5000, access it at:

```
https://YOUR-ID.cloudfront.net/code/ports/5000/
```

**Critical rule for JavaScript:** Always use **relative URLs** in your frontend code:

```javascript
// CORRECT — works through the proxy
fetch('analyze', { method: 'POST', ... })
fetch('api/data')

// WRONG — will give "Unexpected token '<'" JSON errors
fetch('/analyze', { method: 'POST', ... })
fetch('/api/data')
```

The leading `/` sends requests to the CloudFront root instead of your app. Drop it.

---

## 7. Start Building

You're ready! Open the [BUILD-GUIDE.md](BUILD-GUIDE.md) and follow the six steps. Pick your idea from the [vision-docs/](vision-docs/) folder, or bring your own using the [template](templates/).

**Quick tip:** Tell Claude Code your idea and paste your vision doc. It will handle the rest — just review what it proposes before approving.

---

## Available AWS Services (Quick Reference)

> **Note:** Some newer Opus models (4.7, 4.8) may not be available on sandbox accounts. Use **Opus 4.6** for the best quality, or **Sonnet 4.6** for a fast and excellent alternative.

| Service | Use Case | Bedrock Model ID |
|---------|----------|-----------------|
| Amazon Bedrock (Claude Opus 4.6) | Highest quality — complex reasoning, nuanced tasks | `us.anthropic.claude-opus-4-6-v1` |
| Amazon Bedrock (Claude Sonnet 4.6) | Best speed/quality balance — recommended default | `us.anthropic.claude-sonnet-4-6` |
| Amazon Bedrock (Claude Haiku 4.5) | Fastest — classification, extraction, quick tasks | `us.anthropic.claude-haiku-4-5-20251001-v1:0` |
| Amazon Bedrock (Claude Sonnet 4.5) | Complex analysis, creative generation | `us.anthropic.claude-sonnet-4-5-20250929-v1:0` |
| Amazon Polly | Text-to-speech (neural voices) | N/A — use `polly` client |
| Amazon Textract | Document/PDF text extraction | N/A — use `textract` client |
| Amazon Translate | Language translation | N/A — use `translate` client |
| Amazon Comprehend | Sentiment, entities, key phrases | N/A — use `comprehend` client |
| Amazon S3 | File storage (if needed) | N/A — use `s3` client |

### Bedrock Code Pattern (Copy-Paste Ready)

```python
import boto3, json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def ask_claude(prompt, max_tokens=2048):
    """Call Claude via Bedrock. Works with any idea."""
    response = bedrock.invoke_model(
        modelId='us.anthropic.claude-sonnet-4-6',
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': max_tokens,
            'messages': [{'role': 'user', 'content': prompt}]
        }),
        contentType='application/json',
        accept='application/json'
    )
    result = json.loads(response['body'].read())
    return result['content'][0]['text']

# Example usage
answer = ask_claude("Summarize this article in 3 bullet points: ...")
print(answer)
```

### Polly Code Pattern (for ideas needing audio)

```python
import boto3

polly = boto3.client('polly', region_name='us-east-1')

def text_to_speech(text, voice='Matthew'):
    """Convert text to MP3 audio. Neural voices: Matthew, Joanna, Stephen, Kimberly, Joey."""
    response = polly.synthesize_speech(
        Text=text,
        TextType='text',  # Use 'ssml' only with <speak> + <break> tags
        OutputFormat='mp3',
        VoiceId=voice,
        Engine='neural'
    )
    return response['AudioStream'].read()

# Save to file
audio = text_to_speech("Hello, welcome to our demo.")
with open('output.mp3', 'wb') as f:
    f.write(audio)
```
