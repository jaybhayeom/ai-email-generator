# MailCraft CLI ⚡

**MailCraft CLI** is an enterprise-grade, terminal-native AI email generation and editing assistant. Engineered specifically to bridge the gap between robotic, low-quality AI output and sharp, context-aware human communication, MailCraft leverages a **Dual AI Engine Architecture** (Groq + Google Gemini) to craft tailored emails, polish raw drafts, and generate high-converting subject lines across diverse user personas.

Whether you are an academic navigating complex university outreach, a professional handling corporate communications, or a business founder pitching prospective clients, MailCraft CLI structures prompts dynamically to eliminate AI cliches like *"I hope this email finds you well"* and deliver high-impact copy.

---

## 📋 Table of Contents

* [Key Features](https://www.google.com/search?q=%23-key-features)
* [Dual AI Engine Architecture](https://www.google.com/search?q=%23-dual-ai-engine-architecture)
* [System Architecture & Workflow](https://www.google.com/search?q=%23-system-architecture--workflow)
* [Prerequisites](https://www.google.com/search?q=%23-prerequisites)
* [Installation & Setup](https://www.google.com/search?q=%23-installation--setup)
* [Environment Configuration](https://www.google.com/search?q=%23-environment-configuration)
* [Usage Walkthrough](https://www.google.com/search?q=%23-usage-walkthrough)
* [Preset Directory](https://www.google.com/search?q=%23-preset-directory)
* [Directory Structure](https://www.google.com/search?q=%23-directory-structure)
* [Troubleshooting & FAQ](https://www.google.com/search?q=%23-troubleshooting--faq)
* [Contributing](https://www.google.com/search?q=%23-contributing)
* [License](https://www.google.com/search?q=%23-license)

---

## 🌟 Key Features

### ⚡ Dual AI Engine Switcher

* **Groq Acceleration**: Uses `llama-3.3-70b-versatile` on Groq's LPU infrastructure for ultra-low latency response times.
* **Google Gemini Integration**: Uses `gemini-2.5-flash` for deep contextual reasoning and nuanced tone matching.
* **Hot-Swapping & Dynamic Fallbacks**: Switch engines instantly inside the terminal interface or rely on automatic detection based on configured API keys.

### 🎓 Persona-Centric Copywriting Presets

* Specialized workflows built for three distinct user groups: **Students**, **Corporate Professionals**, and **Business Owners / Entrepreneurs**.
* Strict anti-cliche system instructions designed to yield human, authentic, and persuasive tone dynamics.

### ✍️ Draft Critique & Refinement Engine

* Paste rough, unformatted, or sensitive drafts directly into the terminal.
* The engine provides a 2–3 point structural analysis followed by a rewritten, polished final version optimized for clarity and conciseness.

### 🎯 High-Converting Subject Line Multi-Generator

* Generates 5 distinct subject line angles for any prompt:
1. *Direct & Clear*
2. *Curiosity-Driven*
3. *Value / Benefit-First*
4. *Urgent / Action-Oriented*
5. *Casual / Human*



### 💻 Rich Terminal UI & Workflow Export

* Fully stylized interface powered by `rich` featuring custom tables, panels, color codes, and spinner animations.
* Native operating system clipboard integration (`pyperclip`) and structured Markdown (`.md`/`.txt`) file saving options.

---

## ⚡ Dual AI Engine Architecture

MailCraft CLI treats model access abstractly through a unified client wrapper (`DualAIEngine`). This decoupled design ensures seamless provider switching without breaking user workflows.

| Feature | Groq Engine | Google Gemini Engine |
| --- | --- | --- |
| **Default Model** | `llama-3.3-70b-versatile` | `gemini-2.5-flash` |
| **Primary Strength** | Sub-second response latency, direct-to-point formatting | High contextual capacity, nuanced vocabulary |
| **Ideal For** | Quick follow-ups, brief updates, rapid subject lines | Complex negotiations, intricate proposals, sensitive edits |
| **Authentication** | `GROQ_API_KEY` in `.env` | `GOOGLE_API_KEY` in `.env` |

---

## 📐 System Architecture & Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            MAILCRAFT CLI                                │
└─────────────────────────────────────────────────────────────────────────┘
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
┌──────────────────────┐                           ┌──────────────────────┐
│  Environment Check   │                           │  User Interface      │
│  Loads `.env` keys   │                           │  Rich Menu System    │
└──────────────────────┘                           └──────────────────────┘
           │                                                   │
           └─────────────────────────┬─────────────────────────┘
                                     ▼
                  ┌─────────────────────────────────────┐
                  │           Mode Selection            │
                  │  1. Preset / Custom Generation      │
                  │  2. Critique & Polish               │
                  │  3. Subject Line Multi-Gen          │
                  │  4. Switch Active AI Engine         │
                  └─────────────────────────────────────┘
                                     │
                                     ▼
                  ┌─────────────────────────────────────┐
                  │    Unified Dual AI Engine Dispatch  │
                  │   [ Groq Llama 3.3 | Gemini 2.5 ]   │
                  └─────────────────────────────────────┘
                                     │
                                     ▼
                  ┌─────────────────────────────────────┐
                  │  Formatting & Post-Processing Panel │
                  │  Markdown Render | Clipboard | Save │
                  └─────────────────────────────────────┘

```

---

## ⚙️ Prerequisites

Before installing MailCraft CLI, ensure your environment meets the following requirements:

* **Python**: `3.9` or higher
* **Operating System**: Linux, macOS, or Windows (WSL recommended for Windows users)
* **API Keys**: At least one active key from:
* [Groq Console](https://www.google.com/url?sa=E&source=gmail&q=https://console.groq.com/)
* [Google AI Studio](https://www.google.com/url?sa=E&source=gmail&q=https://aistudio.google.com/)



---

## 📥 Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/mailcraft-cli.git
cd mailcraft-cli

```


2. **Create and Activate a Virtual Environment**
* *Linux / macOS:*
```bash
python3 -m venv venv
source venv/bin/activate

```


* *Windows (Command Prompt):*
```cmd
python -m venv venv
venv\Scripts\activate

```




3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


*Or install packages manually:*
```bash
pip install python-dotenv groq google-genai rich pyperclip

```



---

## 🔑 Environment Configuration

MailCraft CLI manages API secrets securely using `python-dotenv`.

1. Create a `.env` file in the root project directory:
```bash
touch .env

```


2. Open the `.env` file in your preferred editor and populate your keys:
```env
# API Key for Groq Engine (https://console.groq.com/)
GROQ_API_KEY=gsk_your_groq_api_key_string_here

# API Key for Google Gemini Engine (https://aistudio.google.com/)
GOOGLE_API_KEY=AIzaSy_your_google_api_key_string_here

```



> **Security Note:** Never commit your `.env` file to public source control. The `.gitignore` file included in this repository excludes `.env` by default.

---

## 🚀 Usage Walkthrough

Launch MailCraft CLI from your terminal:

```bash
python email_gen.py

```

### 1. Generating a Preset Email

1. Select **Option [1]** from the main menu.
2. Choose your Target Persona: `🎓 Student`, `💼 Professional`, or `🏢 Business Owner`.
3. Select an email template (e.g., *Cold Internship Inquiry* or *Overdue Invoice Reminder*).
4. Enter contextual details:
* **Recipient Name/Role** (e.g., *Dr. Aris Thorne, Head of AI Lab*)
* **Key Details & Core Goals** (e.g., *Undergrad in CS, interested in low-bit quantization, requesting 15-minute chat*)


5. Select tone, length, and target language.
6. MailCraft outputs a formatted email with a subject line and signature block.

### 2. Polishing an Existing Draft

1. Select **Option [2]** from the main menu.
2. Paste your raw text into the terminal and hit `Enter` twice.
3. Specify your editing objective (e.g., *"Make it sound more assertive without being disrespectful"*).
4. Review the AI's structural critique alongside the improved final draft.

### 3. Subject Line Multi-Generator

1. Select **Option [3]** from the main menu.
2. Input the email's topic and audience.
3. Receive 5 marketing-tested subject lines spanning different psychological triggers.

---

## 📂 Preset Directory

MailCraft CLI ships with built-in prompt engineering frameworks for common communication scenarios:

| Category | Template Name | Objective |
| --- | --- | --- |
| **🎓 Student** | Assignment Extension Request | Request deadline extensions with accountability and professionalism. |
|  | Professor Office Hours Inquiry | Ask technical questions or request appointments with faculty. |
|  | Cold Internship Outreach | Pitch academic projects and skill sets to researchers or recruiters. |
|  | Recommendation Letter Request | Request reference letters complete with relevant project highlights. |
| **💼 Professional** | Meeting Summary & Action Items | Send clean post-call recaps with designated ownership and deadlines. |
|  | Compensation / Role Review | Formally request salary or title discussions backed by performance. |
|  | Project Status Update | Provide concise status reports outlining milestones, blockers, and timelines. |
|  | Networking Follow-Up | Re-engage contacts after events, panels, or informal meetings. |
|  | Formal Resignation | Professional notice maintaining positive relationships and exit assistance. |
| **🏢 Business Owner** | Cold B2B Outreach Pitch | Punchy value propositions focusing on client pain points. |
|  | Proposal / Quote Follow-Up | Gentle nudge on outstanding quotes without sounding over-eager. |
|  | Overdue Invoice Reminder | Firm, professional demand for past-due account settlements. |
|  | Issue Resolution / De-escalation | Apologize for service issues while offering clear remedial steps. |
|  | Partnership / Brand Inquiry | Propose strategic cross-promotions or mutual growth initiatives. |

---

## 📁 Directory Structure

```text
mailcraft-cli/
├── .env.example          # Sample environment file template
├── .gitignore            # Standard git ignore file (hides .env, venv, pycache)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies list
└── email_gen.py          # Primary application source code

```

---

## ❓ Troubleshooting & FAQ

#### Q: I get `No valid API keys found in .env!` on startup.

* **Fix**: Ensure your `.env` file is named exactly `.env` (not `.env.txt`) and is saved in the same directory as `email_gen.py`. Verify that at least one of the keys (`GROQ_API_KEY` or `GOOGLE_API_KEY`) is populated with a valid key string.

#### Q: Copying to clipboard throws a warning or fails.

* **Fix**: MailCraft relies on `pyperclip`. On Linux systems (X11/Wayland), `pyperclip` requires `xclip` or `xsel` to be installed on your operating system:
```bash
# Debian/Ubuntu
sudo apt install xclip

# Arch Linux
sudo pacman -S xclip

```



#### Q: How do I default to Google Gemini instead of Groq?

* **Fix**: Go to **Option [4]** in the main menu (**Switch AI Engine**) to set Gemini as your active provider. If only `GOOGLE_API_KEY` is present in your `.env` file, MailCraft automatically defaults to Gemini on launch.

---

## 🤝 Contributing

Contributions are welcome! If you want to add new presets, enhance formatting, or support additional models, follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
```bash
git checkout -b feature/NewPresetCollection

```


3. **Commit Your Changes**
```bash
git commit -m "Add preset for academic grant requests"

```


4. **Push to Your Branch**
```bash
git push origin feature/NewPresetCollection

```


5. **Open a Pull Request**

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
