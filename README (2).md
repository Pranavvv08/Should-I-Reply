# **Should I Reply?**  

## **Overview**  

**Should I Reply?** is an AI-powered email assistant that analyzes incoming emails for urgency, emotional tone, and suggests smart, context-aware replies. By leveraging **OpenRouter's DeepSeek-v3**, it helps you prioritize important messages and craft responses effortlessly—saving time and reducing email overload.  

🚀 **Key Benefits:**  
✔ **Never miss an urgent email again**  
✔ **Understand the sender's tone before replying**  
✔ **Get AI-generated replies in seconds**  
✔ **Secure, automated, and easy to use**  

---

## **How It Works**  

1. **📩 Fetch Unread Emails**  
   - Connects to your Gmail via **IMAP** (secure & encrypted).  
   - Retrieves unread emails, extracting sender, subject, and body.  

2. **🤖 AI-Powered Analysis**  
   - Uses **DeepSeek-v3** (via OpenRouter) to analyze:  
     - **🔴 Urgency:** High, Medium, or Low priority.  
     - **😊 Emotional Tone:** Positive, Negative, Neutral, or Mixed.  
     - **💡 Suggested Reply:** A natural, context-aware response.  

3. **📊 Clear & Actionable Insights**  
   - Displays results in an easy-to-read format.  
   - Helps you decide **whether, when, and how** to reply.  

---

## **✨ Key Features**  

| Feature | Description |  
|---------|------------|  
| **Automated Email Fetching** | Securely retrieves unread emails from Gmail. |  
| **AI-Driven Insights** | Detects urgency, tone, and suggests replies. |  
| **Smart Reply Generation** | Custom AI responses tailored to each email. |  
| **Secure & Private** | Uses **Google Secret Manager** for API & email credentials. |  
| **Easy Integration** | Works seamlessly in **Google Colab** or local Python environments. |  

---

## **🚀 Setup & Installation**  

### **Prerequisites**  
Before running the project, ensure you have:  

- **Python 3.10+**  
- A **Gmail account** with **IMAP enabled** ([Enable IMAP access here](https://support.google.com/mail/answer/7126229)).  
- An **OpenRouter API key** ([Get one here](https://openrouter.ai/)).  
- (Optional) **Google Secret Manager** for secure credential storage (if using Google Colab).  

### **Installation**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Pranavvv08/Should-I-Reply-
   cd should-i-reply
   ```
2. **Install Dependencies**
   ```bash
   pip install imapclient openai python-dotenv
   ```
3. **Set Up Environment Variables**
Create a new ```.env ``` file in project directory and add:

   ```bash
   GMAIL_USER="your_email@gmail.com"
   GMAIL_PASSWORD="your_app_password" # Use an App Password for security
   OPENROUTER_API_KEY="your_api_key_here"
   ```
4.**Run the Script**
   ```bash
   python shouldIReply.py

   ```


