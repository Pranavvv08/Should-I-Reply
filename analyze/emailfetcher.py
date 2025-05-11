import imaplib
import email
from email.header import decode_header
import re
from bs4 import BeautifulSoup

def strip_html(html):
    """Clean and extract visible text from HTML content."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get raw text
    text = soup.get_text(separator="\n", strip=True)

    # Remove common placeholders like Mailchimp preview text
    text = re.sub(r"\*\|.*?\|\*", "", text)

    # Collapse multiple newlines and remove leading/trailing spaces
    text = re.sub(r"\n+", "\n", text).strip()

    # Optionally truncate long link-heavy footers
    if len(text) > 1000:
        text = text[:1000] + "\n... (truncated)"

    return text

def fetch_recent_emails(user_email, password, max_emails=5):
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(user_email, password)
        imap.select("inbox")

        status, messages = imap.search(None, 'ALL')
        email_ids = messages[0].split()[-max_emails:]

        emails = []

        for eid in reversed(email_ids):
            res, msg_data = imap.fetch(eid, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decode subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(errors='ignore')

                    body = ""
                    html_body = ""

                    # Parse email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition", ""))
                            if "attachment" in content_disposition:
                                continue

                            payload = part.get_payload(decode=True)
                            if payload:
                                decoded = payload.decode(errors='ignore')
                                if content_type == "text/plain" and not body:
                                    body = decoded
                                elif content_type == "text/html" and not html_body:
                                    html_body = decoded
                    else:
                        payload = msg.get_payload(decode=True)
                        if payload:
                            decoded = payload.decode(errors='ignore')
                            if msg.get_content_type() == "text/plain":
                                body = decoded
                            elif msg.get_content_type() == "text/html":
                                html_body = decoded

                    # Fallback to cleaned HTML
                    if not body and html_body:
                        body = strip_html(html_body)

                    # Final fallback
                    clean_body = body.strip() if body else "(No readable content found)"
                    emails.append({"subject": subject, "body": clean_body})

        imap.logout()
        return emails

    except Exception as e:
        return [{"subject": "Error", "body": str(e)}]
