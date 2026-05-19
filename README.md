# 📧 AI Email Generator

A Python tool that transforms rough notes into polished, professional emails using Google's Gemini AI.

---

## ✨ Features

- Converts casual notes into professionally written emails
- Maintains appropriate tone based on context
- Uses `[Bracketed Placeholders]` when information is missing
- Simple command-line interface
- Powered by Gemini 2.5 Flash

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A [Google AI Studio](https://aistudio.google.com/) account with a Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-email-generator.git
   cd ai-email-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the root of the project:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and add your actual API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

---

## 💻 Usage

Run the script from your terminal:

```bash
python main.py
```

You will be prompted to enter your notes. For example:

```
Your Notes: Email to John at Acme Corp, following up on the proposal we sent last Monday. Ask if he has any questions and suggest a 30-min call this week.
```

**Sample Output:**

```
Subject: Follow-Up: Proposal & Next Steps

Dear John,

I hope this message finds you well. I wanted to follow up on the proposal
we sent over last Monday and see if you've had a chance to review it.

Please don't hesitate to reach out if you have any questions or would like
to discuss any aspect in more detail. I'd also be happy to schedule a brief
30-minute call at your convenience this week.

Looking forward to hearing from you.

Best regards,
[Your Name]
```

---

## 📁 Project Structure

```
ai-email-generator/
│
├── main.py            # Main application script
├── requirements.txt   # Python dependencies
├── .env.example       # Template for environment variables
├── .env               # Your local API key (never committed)
├── .gitignore         # Files excluded from version control
└── README.md          # Project documentation
```

---

## 🔐 Security

Your API key is stored in a `.env` file which is listed in `.gitignore` and will **never** be uploaded to GitHub. Never hardcode API keys directly in your source code.

---

## 🛠️ Built With

- [Google Generative AI Python SDK](https://github.com/google-gemini/generative-ai-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋 Author

**OM JAYBHAYE**

- GitHub: [@jaybhayeom](https://github.com/jaybhayeom)
- LinkedIn: [@OmJaybhaye](www.linkedin.com/in/om-jaybhaye-py)