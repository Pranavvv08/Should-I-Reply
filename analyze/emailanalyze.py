import requests

OPENROUTER_API_KEY = "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"

def analyze_email(subject, body):
    prompt = f"""
    You are an AI assistant helping Pranav Sasank manage and respond to emails. Your job is to:
    1. **Summarize the email** in 2–4 sentences, focusing on the main topic and any important details.
    - The summary should be concise and informative, capturing the essence of the email without unnecessary details.
    
    2. **Assess the urgency** of the email:
    - "Urgent": Requires immediate attention or action within 24 hours.
    - "Important": Needs a timely response but not immediately.
    - "Ignore": No reply or action is needed (e.g., spam, FYI, irrelevant, newsletter).

    Respond with a complete sentence that describes the urgency level.

    3. **Decide whether a reply is necessary.**
    - If a reply is **not needed**, clearly state: "No reply needed."
    - If a reply **is needed**, generate a formal and personalized email response in 3–5 sentences.
        The reply must:
        - Be written in a professional tone.
        - Be context-aware and helpful.
        - End with:
        ```
        Regards,
        Pranav Sasank
        ```

    Here is the email to analyze:

    Subject: {subject}
    Body: {body}

    Respond in the following format:

    Summary: [Your summary of the email]
    Urgency: [Your sentence about the urgency]
    Reply: [If needed, your personalized reply. If not needed, write: "No reply needed."]
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        return parse_ai_response(content)
    except Exception as e:
        return {"urgency": "Error", "reply": f"AI analysis failed: {str(e)}"}

def parse_ai_response(ai_text):
    lines = ai_text.strip().splitlines()
    summary = ""
    urgency = ""
    reply = []
    reading_reply = False

    for line in lines:
        if line.lower().startswith("summary:"):
            summary = line.split(":", 1)[1].strip()
        elif line.lower().startswith("urgency:"):
            urgency = line.split(":", 1)[1].strip()
        elif line.lower().startswith("reply:"):
            reading_reply = True
            reply_line = line.split(":", 1)[1].strip()
            if reply_line:
                reply.append(reply_line)
        elif reading_reply:
            reply.append(line.strip())

    return {
        "summary": summary if summary else "No summary found.",
        "urgency": urgency if urgency else "Unknown",
        "reply": "\n".join(reply).strip() if reply else "No reply found."
    }

