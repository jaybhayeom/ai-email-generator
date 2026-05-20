# 📧 AI Email Generator v2.0

A Python command-line tool that converts your rough notes into polished, professional emails using Google's Gemini AI — with tone selection and email history.

---

## ✨ Features

- 🎯 **3 Tone Options** — Formal, Friendly, or Urgent
- 💾 **Email History** — Every email auto-saved to `email_history.csv` with timestamp
- 📋 **View Past Emails** — Browse all previously generated emails anytime
- 🔒 **Secure API Handling** — API key stored safely in `.env`, never in code
- ⚡ **Powered by Gemini 2.5 Flash**

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- A [Google AI Studio](https://aistudio.google.com/) account with a Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jaybhayeom/ai-email-generator.git
   cd ai-email-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the project folder:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

---

## 💻 Usage

```bash
python main.py
```

You'll see a menu like this:

```
========================================
     AI EMAIL GENERATOR  v2.0
========================================

What would you like to do?
  [1] Generate a new email
  [2] View email history
  [3] Exit
```

### Tone Options

| Tone | Best For |
|------|----------|
| 📄 Formal | Clients, managers, official communication |
| 😊 Friendly | Colleagues, people you know well |
| 🚨 Urgent | Time-sensitive, action required immediately |

### Example

**Your Notes:**
```
Email to John at Acme Corp, following up on the proposal sent last Monday.
Ask if he has questions and suggest a 30-min call this week.
```

**Tone:** Formal

**Output:**
```
Subject: Follow-Up: Proposal & Next Steps

Dear John,

I hope this message finds you well. I wanted to follow up on the proposal
we sent over last Monday and check if you had a chance to review it.

Please don't hesitate to reach out if you have any questions. I'd also be
happy to schedule a brief 30-minute call at your convenience this week.

Looking forward to hearing from you.

Best regards,
[Your Name]
```

---

## 📁 Project Structure

```
ai-email-generator/
│
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── .env.example         # API key template
├── .env                 # Your local API key (never committed)
├── .gitignore           # Files excluded from version control
├── email_history.csv    # Auto-generated history (never committed)
└── README.md            # Project documentation
```

---

## 🔐 Security

Your API key lives in a `.env` file listed in `.gitignore` and will **never** be uploaded to GitHub. Never hardcode API keys directly in source code.

---

## 🛠️ Built With

- [Google GenAI Python SDK](https://github.com/googleapis/python-genai)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋 Author

**Om Jaybhaye**

- GitHub: [@jaybhayeom](https://github.com/jaybhayeom)
- LinkedIn: [@OmJaybhaye](https://www.linkedin.com/in/om-jaybhaye-py)