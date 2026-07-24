"""
Flask App Template for Hackathon Projects

This template handles the CloudFront proxy setup correctly.
Replace the placeholder routes with your actual logic.

Usage:
    source venv/bin/activate
    python3 app_template.py

Access at: https://YOUR-CLOUDFRONT-ID.cloudfront.net/code/ports/5000/
"""
import json
import os

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# --- AWS Clients (initialize once) ---
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
# Uncomment the services you need:
# polly = boto3.client("polly", region_name="us-east-1")
# textract = boto3.client("textract", region_name="us-east-1")
# translate_client = boto3.client("translate", region_name="us-east-1")
# comprehend = boto3.client("comprehend", region_name="us-east-1")


# --- Helper: Call Claude via Bedrock ---
def ask_claude(prompt, max_tokens=2048, model="us.anthropic.claude-sonnet-4-6"):
    """
    Call Claude via Amazon Bedrock.

    Models available:
        us.anthropic.claude-haiku-4-5-20251001-v1:0   (fast, cheap — good for dev)
        us.anthropic.claude-sonnet-4-6                 (best available — good for demo)
        us.anthropic.claude-sonnet-4-5-20250929-v1:0  (also excellent quality)
    """
    response = bedrock.invoke_model(
        modelId=model,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }),
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response["body"].read())
    return result["content"][0]["text"]


# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """
    Example API endpoint. Replace with your actual logic.
    The frontend should call: fetch('process', {method: 'POST', ...})
    Note: NO leading slash — required for CloudFront proxy to work.
    """
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    user_input = data.get("input", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Replace this with your actual AI logic
        result = ask_claude(f"Process this: {user_input}")
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- Error Handlers (return JSON, not HTML) ---
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
