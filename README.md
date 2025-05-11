# **Should I Reply?**  

## **Overview**  

**Should I Reply?** is an AI-powered email assistant that analyzes incoming emails for urgency, emotional tone, and suggests smart, context-aware replies. By leveraging **OpenRouter's LLM Models**, it helps you prioritize important messages and craft responses effortlessly—saving time and reducing email overload.  

🚀 **Key Benefits:**  
✔ **Never miss an urgent email again**  
✔ **Understand the sender's tone before replying**  
✔ **Get AI-generated replies in seconds**  
✔ **Secure, automated, and easy to use**  

---

## **How It Works**  

1. **📩 Fetch Recent Emails**  
   - Connects to your Gmail via **IMAP** (secure & encrypted).  
   - Retrieves recent emails, extracting sender, subject, and body.  

2. **🤖 AI-Powered Analysis**  
   - Uses **Llama-4-Maverick** (via OpenRouter) to analyze:  
     - **📝 Summary:** Concise overview of email content.
     - **🔴 Urgency:** Categorizes as Urgent, Important, or Ignorable.  
     - **💡 Suggested Reply:** A natural, context-aware response when needed.  

3. **📊 Clear & Actionable Insights**  
   - Displays results in an easy-to-read format.  
   - Helps you decide **whether, when, and how** to reply.  

---

## **✨ Key Features**  

| Feature | Description |  
|---------|------------|  
| **Automated Email Fetching** | Securely retrieves emails from Gmail. |  
| **AI-Driven Insights** | Detects urgency and suggests replies. |  
| **Smart Reply Generation** | Custom AI responses tailored to each email. |  
| **Web Interface** | Clean Django web application for easy use. |  
| **Secure Authentication** | Direct use of your email credentials without storage. |  

---

## **🚀 Setup & Installation**  

### **Prerequisites**  
Before running the project, ensure you have:  

- **Python 3.11+**  
- A **Gmail account** with **IMAP enabled** ([Enable IMAP access here](https://support.google.com/mail/answer/7126229))
- For Gmail, you'll need to use an **App Password** ([Create one here](https://myaccount.google.com/apppasswords))

### **Installation**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Pranavvv08/Should-I-Reply.git
   cd Should-I-Reply
   ```

2. **Create a Virtual Environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django Development Server**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Enter your Gmail address and app password when prompted
   - View your analyzed emails!

### **Note on Email Security**
This application requires your Gmail credentials to access your emails. For security:
- Use an App Password instead of your main Google password
- The app doesn't store your credentials anywhere
- All processing happens locally on your machine
