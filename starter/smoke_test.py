"""
AWS Smoke Test — Run this first to verify your environment.

Usage:
    export AWS_DEFAULT_REGION="us-east-1"
    export AWS_ACCESS_KEY_ID="..."
    export AWS_SECRET_ACCESS_KEY="..."
    export AWS_SESSION_TOKEN="..."
    python3 smoke_test.py
"""
import json
import sys

print("=" * 50)
print("AWS Environment Smoke Test")
print("=" * 50)

errors = []

# Test 1: boto3 available
print("\n[1/4] Checking boto3...")
try:
    import boto3
    print("  OK: boto3 installed")
except ImportError:
    print("  FAIL: boto3 not found. Run: pip install boto3")
    errors.append("boto3")

# Test 2: AWS credentials valid
print("\n[2/4] Checking AWS credentials...")
try:
    sts = boto3.client("sts", region_name="us-east-1")
    identity = sts.get_caller_identity()
    print(f"  OK: Account {identity['Account']}")
    print(f"      Role: {identity['Arn']}")
except Exception as e:
    print(f"  FAIL: {e}")
    print("  Fix: Re-export credentials from the Event Dashboard")
    errors.append("credentials")

# Test 3: Bedrock access
print("\n[3/4] Checking Amazon Bedrock...")
try:
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    response = bedrock.invoke_model(
        modelId="us.anthropic.claude-haiku-4-5-20251001-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 20,
            "messages": [{"role": "user", "content": "Say OK"}]
        }),
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response["body"].read())
    text = result["content"][0]["text"]
    print(f"  OK: Bedrock responded: '{text.strip()}'")
except Exception as e:
    print(f"  FAIL: {e}")
    errors.append("bedrock")

# Test 4: Polly access
print("\n[4/4] Checking Amazon Polly...")
try:
    polly = boto3.client("polly", region_name="us-east-1")
    resp = polly.synthesize_speech(
        Text="Test",
        OutputFormat="mp3",
        VoiceId="Matthew",
        Engine="neural"
    )
    audio_bytes = len(resp["AudioStream"].read())
    print(f"  OK: Polly returned {audio_bytes} bytes of audio")
except Exception as e:
    print(f"  FAIL: {e}")
    errors.append("polly")

# Summary
print("\n" + "=" * 50)
if not errors:
    print("ALL CHECKS PASSED — You are ready to build!")
else:
    print(f"FAILED: {', '.join(errors)}")
    print("Fix the issues above, then re-run this script.")
    sys.exit(1)
print("=" * 50)
