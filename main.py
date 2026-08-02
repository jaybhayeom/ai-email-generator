#!/usr/bin/env python3
"""
MailCraft CLI - Advanced AI Email Assistant
Supported AI Engines: Groq (Llama 3.3) & Google Gemini (2.5 Flash)
"""

import os
import sys
from datetime import datetime
from typing import Optional, Tuple
from dotenv import load_dotenv

# Rich CLI formatting
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.table import Table
from rich.markdown import Markdown

# API SDKs
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

# Initialize Rich Console
console = Console()

# Load environment variables from .env
load_dotenv()


class DualAIEngine:
    """Manages switching and API interactions between Groq and Google Gemini."""

    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.google_key = os.getenv("GOOGLE_API_KEY")

        self.groq_client = None
        self.gemini_client = None

        if GROQ_AVAILABLE and self.groq_key:
            try:
                self.groq_client = Groq(api_key=self.groq_key)
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to init Groq: {e}[/yellow]")

        if GEMINI_AVAILABLE and self.google_key:
            try:
                self.gemini_client = genai.Client(api_key=self.google_key)
            except Exception as e:
                console.print(f"[yellow]Warning: Failed to init Gemini: {e}[/yellow]")

        # Set default provider
        if self.groq_client:
            self.active_provider = "groq"
        elif self.gemini_client:
            self.active_provider = "google"
        else:
            self.active_provider = None

    def get_status(self) -> Tuple[bool, str]:
        if not self.active_provider:
            return False, "No valid API keys found in .env! Add GROQ_API_KEY or GOOGLE_API_KEY."
        return True, f"Active Engine: [bold green]{self.active_provider.upper()}[/bold green]"

    def set_provider(self, provider: str) -> bool:
        if provider == "groq" and self.groq_client:
            self.active_provider = "groq"
            return True
        elif provider == "google" and self.gemini_client:
            self.active_provider = "google"
            return True
        return False

    def generate(self, prompt: str, system_instruction: str = "") -> str:
        """Dispatches generation request to active provider."""
        if not self.active_provider:
            raise RuntimeError("No API key available. Please configure your .env file.")

        with console.status(f"[bold cyan]Generating email with {self.active_provider.upper()}...[/bold cyan]", spinner="dots"):
            if self.active_provider == "groq":
                messages = []
                if system_instruction:
                    messages.append({"role": "system", "content": system_instruction})
                messages.append({"role": "user", "content": prompt})

                response = self.groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000,
                )
                return response.choices[0].message.content.strip()

            elif self.active_provider == "google":
                full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt
                response = self.gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=full_prompt,
                )
                return response.text.strip()


# Global Presets
PRESETS = {
    "1": {
        "category": "🎓 Student",
        "templates": [
            ("Assignment Extension", "Requesting deadline extension due to unforeseen circumstances"),
            ("Professor Office Hours / Inquiry", "Asking for clarification on topic/assignment or meeting appointment"),
            ("Cold Internship Inquiry", "Reaching out to a researcher or company for an internship position"),
            ("Letter of Recommendation Request", "Politely asking a professor or manager for a reference letter"),
        ]
    },
    "2": {
        "category": "💼 Professional",
        "templates": [
            ("Meeting Summary & Next Steps", "Recapping key points and action items from a recent call"),
            ("Salary / Promotion Review", "Formally requesting a conversation regarding compensation or role growth"),
            ("Project Status Update", "Updating team/stakeholders on deliverables, blockers, and timelines"),
            ("Networking / Warm Follow-up", "Reconnecting with an industry peer or coffee chat contact"),
            ("Formal Resignation", "Professional, courteous resignation notice with transition support"),
        ]
    },
    "3": {
        "category": "🏢 Business Owner",
        "templates": [
            ("Cold B2B Sales Pitch", "Punchy value proposition outreach to potential prospective clients"),
            ("Client Proposal / Quote Follow-up", "Following up on a sent proposal without sounding desperate"),
            ("Overdue Invoice Reminder (Firm)", "Professional but assertive payment request for past-due invoice"),
            ("Customer Service Issue Resolution", "De-escalating customer complaint with action plan and empathy"),
            ("Partnership / Collaboration Inquiry", "Proposing mutual value collaboration to another brand/creator"),
        ]
    }
}


def render_header(ai_engine: DualAIEngine):
    """Prints application banner."""
    console.clear()
    status_ok, status_msg = ai_engine.get_status()
    
    banner = Panel.fit(
        "[bold magenta]⚡ MailCraft AI CLI ⚡[/bold magenta]\n"
        "[dim]Tailored Email Copywriting for Students, Professionals & Business Leaders[/dim]\n\n"
        f"Status: {status_msg}",
        border_style="cyan",
        title="[bold yellow]v2.0[/bold yellow]"
    )
    console.print(banner)


def choose_preset() -> Tuple[str, str]:
    """Helper to select persona category and specific template."""
    console.print("\n[bold cyan]Select Your Category:[/bold cyan]")
    for key, data in PRESETS.items():
        console.print(f"  [bold green][{key}][/bold green] {data['category']}")

    cat_choice = Prompt.ask("Choose category", choices=list(PRESETS.keys()), default="1")
    selected_cat = PRESETS[cat_choice]

    console.print(f"\n[bold cyan]Select Template for {selected_cat['category']}:[/bold cyan]")
    for idx, (title, desc) in enumerate(selected_cat["templates"], 1):
        console.print(f"  [bold green][{idx}][/bold green] [bold]{title}[/bold]: [dim]{desc}[/dim]")

    tmpl_choice = IntPrompt.ask("Choose template number", default=1)
    tmpl_idx = max(1, min(tmpl_choice, len(selected_cat["templates"]))) - 1
    
    return selected_cat["category"], selected_cat["templates"][tmpl_idx][0]


def generate_email_flow(ai_engine: DualAIEngine):
    """Interactive wizard for generating a fresh email."""
    render_header(ai_engine)
    
    category, template_title = choose_preset()

    console.print(f"\n[bold green]Selected Preset:[/bold green] {category} -> {template_title}")
    
    # Context inputs
    recipient = Prompt.ask("\n👤 [bold]Who is the recipient?[/bold] (e.g. 'Prof. Davis', 'Potential Client', 'Hiring Team')")
    key_details = Prompt.ask("📝 [bold]Key details / core goal of email[/bold] (bullet points or short sentence)")

    # Customization options
    console.print("\n[bold cyan]Tone Options:[/bold cyan]")
    tones = ["Professional & Formal", "Warm & Friendly", "Direct & Persuasive", "Empathetic & Apologetic"]
    for i, t in enumerate(tones, 1):
        console.print(f"  [{i}] {t}")
    tone_idx = IntPrompt.ask("Choose tone", default=1)
    selected_tone = tones[max(1, min(tone_idx, len(tones))) - 1]

    lengths = ["Concise (<120 words)", "Standard (150-250 words)", "Detailed (Detailed & Thorough)"]
    console.print("\n[bold cyan]Length Options:[/bold cyan]")
    for i, l in enumerate(lengths, 1):
        console.print(f"  [{i}] {l}")
    len_idx = IntPrompt.ask("Choose length", default=2)
    selected_len = lengths[max(1, min(len_idx, len(lengths))) - 1]

    language = Prompt.ask("\n🌐 [bold]Language[/bold]", default="English")

    # Build Prompt
    system_instruction = (
        "You are MailCraft AI, an expert copywriter. Write realistic, effective, and non-generic emails. "
        "Avoid overused AI cliches like 'I hope this email finds you well'. "
        "Format the output strictly as:\n"
        "SUBJECT: <Catchy Subject Line>\n\n"
        "BODY:\n<Salutation>\n<Email Content>\n<Sign-off>"
    )

    prompt = f"""
    Category: {category}
    Goal/Scenario: {template_title}
    Recipient: {recipient}
    Key Details & Facts to Include: {key_details}
    Tone: {selected_tone}
    Target Length: {selected_len}
    Language: {language}

    Write the complete email now.
    """

    try:
        email_result = ai_engine.generate(prompt, system_instruction)
        display_and_handle_output(ai_engine, email_result, prompt)
    except Exception as e:
        console.print(f"\n[bold red]Error generating email:[/bold red] {e}")


def critique_and_polish_flow(ai_engine: DualAIEngine):
    """Improves an existing email draft provided by the user."""
    render_header(ai_engine)
    console.print("[bold yellow]✍️ Email Critique & Polish Mode[/bold yellow]\n")

    console.print("Paste your draft below (Press [bold green]Enter[/bold green] twice when finished):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    user_draft = "\n".join(lines).strip()

    if not user_draft:
        console.print("[red]No text provided. Returning to main menu.[/red]")
        return

    instruction = Prompt.ask(
        "\n⚡ [bold]What should be improved?[/bold]", 
        default="Fix grammar, make it more natural, persuasive, and remove filler words."
    )

    system_instruction = (
        "You are an expert executive editor. Review the user's email draft, provide 2 short constructive critiques, "
        "and then provide the fully polished, improved version."
    )

    prompt = f"""
    Original Draft:
    ---
    {user_draft}
    ---

    Improvement Goal: {instruction}

    Please output:
    1. 💡 BRIEF CRITIQUE (2-3 bullet points)
    2. ✨ POLISHED VERSION (with Subject line and Body)
    """

    try:
        result = ai_engine.generate(prompt, system_instruction)
        console.print("\n", Panel(Markdown(result), title="[bold green]Polished Email & Critique[/bold green]", border_style="green"))
        post_generation_menu(result)
    except Exception as e:
        console.print(f"\n[bold red]Error during critique:[/bold red] {e}")


def subject_line_generator_flow(ai_engine: DualAIEngine):
    """Generates 5 distinct subject line styles for an email idea."""
    render_header(ai_engine)
    console.print("[bold yellow]🎯 High-Converting Subject Line Generator[/bold yellow]\n")

    topic = Prompt.ask("Briefly describe what your email is about")
    target_audience = Prompt.ask("Who is receiving this?", default="General professional")

    system_instruction = "You are a direct-response email marketing expert specializing in open-rate optimization."
    prompt = f"""
    Topic: {topic}
    Audience: {target_audience}

    Generate 5 distinct subject line variations:
    1. Direct & Clear
    2. Curiosity-Driven
    3. Benefit / Value First
    4. Urgency / Action-Oriented
    5. Casual / Personal
    """

    try:
        result = ai_engine.generate(prompt, system_instruction)
        console.print("\n", Panel(Markdown(result), title="[bold cyan]Subject Line Options[/bold cyan]", border_style="cyan"))
        post_generation_menu(result)
    except Exception as e:
        console.print(f"\n[bold red]Error generating subject lines:[/bold red] {e}")


def display_and_handle_output(ai_engine: DualAIEngine, content: str, original_prompt: str):
    """Renders the output email in a panel and presents post-generation tools."""
    console.print("\n", Panel(Markdown(content), title="[bold green]Generated Email[/bold green]", border_style="green"))
    post_generation_menu(content)


def post_generation_menu(content: str):
    """Actions after content generation: copy, save, etc."""
    while True:
        console.print("\n[dim]Options: [1] Copy to Clipboard  [2] Export to File  [3] Back to Main Menu[/dim]")
        action = Prompt.ask("Select action", choices=["1", "2", "3"], default="1")

        if action == "1":
            if CLIPBOARD_AVAILABLE:
                pyperclip.copy(content)
                console.print("[bold green]✓ Copied to clipboard![/bold green]")
            else:
                console.print("[yellow]pyperclip package not installed. Cannot access clipboard.[/yellow]")
        elif action == "2":
            filename = Prompt.ask("Enter filename", default="generated_email.txt")
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"Generated via MailCraft AI on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write(content)
                console.print(f"[bold green]✓ Email saved successfully to '{filename}'[/bold green]")
            except Exception as e:
                console.print(f"[bold red]Failed to save file:[/bold red] {e}")
        elif action == "3":
            break


def switch_engine_flow(ai_engine: DualAIEngine):
    """UI for switching active AI provider."""
    render_header(ai_engine)
    console.print("[bold yellow]⚙️ Switch AI Engine[/bold yellow]\n")

    table = Table(title="Available Providers")
    table.add_column("Provider", style="cyan")
    table.add_column("Key Configured", style="bold")
    table.add_column("Active", style="green")

    table.add_row("Groq (Llama 3.3)", "Yes" if ai_engine.groq_key else "No", "★" if ai_engine.active_provider == "groq" else "")
    table.add_row("Google (Gemini 2.5)", "Yes" if ai_engine.google_key else "No", "★" if ai_engine.active_provider == "google" else "")

    console.print(table)

    choice = Prompt.ask("\nSelect Provider", choices=["groq", "google", "cancel"], default="cancel")
    if choice != "cancel":
        if ai_engine.set_provider(choice):
            console.print(f"[bold green]Successfully switched to {choice.upper()}![/bold green]")
        else:
            console.print(f"[bold red]Cannot switch to {choice.upper()}. Please check if API key exists in .env[/bold red]")
    
    Prompt.ask("\nPress Enter to return...")


def main():
    ai_engine = DualAIEngine()

    while True:
        render_header(ai_engine)

        console.print("\n[bold cyan]Main Menu:[/bold cyan]")
        console.print("  [bold green][1][/bold green] 📧 Generate New Email (Presets & Custom)")
        console.print("  [bold green][2][/bold green] ✍️ Critique & Polish Existing Draft")
        console.print("  [bold green][3][/bold green] 🎯 Generate Subject Line Variations")
        console.print("  [bold green][4][/bold green] ⚙️ Switch AI Engine (Groq / Gemini)")
        console.print("  [bold green][5][/bold green] ❌ Exit")

        choice = Prompt.ask("\nSelect option", choices=["1", "2", "3", "4", "5"], default="1")

        status_ok, _ = ai_engine.get_status()
        if not status_ok and choice in ["1", "2", "3"]:
            console.print("\n[bold red]Cannot generate without an API key. Please configure your .env file.[/bold red]")
            Prompt.ask("\nPress Enter to continue...")
            continue

        if choice == "1":
            generate_email_flow(ai_engine)
        elif choice == "2":
            critique_and_polish_flow(ai_engine)
        elif choice == "3":
            subject_line_generator_flow(ai_engine)
        elif choice == "4":
            switch_engine_flow(ai_engine)
        elif choice == "5":
            console.print("\n[bold magenta]Thank you for using MailCraft! Goodbye. 👋[/bold magenta]")
            sys.exit(0)


if __name__ == "__main__":
    main()
