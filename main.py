from google import genai
from dotenv import load_dotenv
import os
import csv
from datetime import datetime

# ── Setup ──────────────────────────────────────────────────────────────────────

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

client = genai.Client(api_key=api_key)

# ── Constants ──────────────────────────────────────────────────────────────────

HISTORY_FILE = "email_history.csv"

TONES = {
    "1": ("Formal",   "professional, polished, and respectful — suitable for clients or managers."),
    "2": ("Friendly", "warm, conversational, and approachable — suitable for colleagues you know well."),
    "3": ("Urgent",   "direct, time-sensitive, and action-oriented — suitable when immediate response is needed."),
}

# ── Functions ──────────────────────────────────────────────────────────────────

def select_tone():
    """Ask the user to pick a tone and return the name and description."""
    print("\nSelect Email Tone:")
    print("  [1] Formal   — Professional & polished")
    print("  [2] Friendly — Warm & conversational")
    print("  [3] Urgent   — Direct & time-sensitive")

    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice in TONES:
            name, description = TONES[choice]
            print(f"✔ Tone set to: {name}")
            return name, description
        print("Invalid choice. Please enter 1, 2, or 3.")


def generate_email(notes, tone_name, tone_description):
    """Call Gemini API and return the generated email."""

    prompt = (
        f"You are an expert assistant who writes emails.\n\n"
        f"Rules:\n"
        f"1. Only use facts from the notes below. Do not add anything extra.\n"
        f"2. Use [Bracketed Placeholders] for any missing details like names.\n"
        f"3. Tone must be: {tone_description}\n\n"
        f"Convert these notes into a {tone_name.lower()} email:\n\n"
        f"Notes: {notes}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text if response.text else "Error: No response received from AI."

    except Exception as e:
        return f"Error: {str(e)}"


def save_to_history(tone, notes, email):
    """Append the generated email to the CSV history file."""
    file_exists = os.path.isfile(HISTORY_FILE)

    with open(HISTORY_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Tone", "Notes", "Generated Email"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tone, notes, email])

    print(f"✔ Email saved to '{HISTORY_FILE}'")


def view_history():
    """Print a summary of all previously generated emails."""
    if not os.path.isfile(HISTORY_FILE):
        print("\nNo history yet. Generate your first email!")
        return

    with open(HISTORY_FILE, mode="r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("\nHistory file is empty.")
        return

    print(f"\n{'='*60}")
    print(f"  EMAIL HISTORY — {len(rows)} email(s) saved")
    print(f"{'='*60}")

    for i, row in enumerate(rows, 1):
        notes_preview = row["Notes"][:80] + ("..." if len(row["Notes"]) > 80 else "")
        email_preview = row["Generated Email"][:120].strip() + "..."
        print(f"\n[{i}] {row['Timestamp']}  |  Tone: {row['Tone']}")
        print(f"    Notes   : {notes_preview}")
        print(f"    Preview : {email_preview}")
        print(f"    {'-'*56}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 40)
    print("     AI EMAIL GENERATOR  v2.0")
    print("=" * 40)

    while True:
        print("\nWhat would you like to do?")
        print("  [1] Generate a new email")
        print("  [2] View email history")
        print("  [3] Exit")

        action = input("\nEnter choice (1/2/3): ").strip()

        if action == "1":
            print("\nExample: 'Email to Sarah asking for a meeting on Friday about the budget'")
            notes = input("\nYour Notes: ").strip()

            if not notes:
                print("No notes entered. Please try again.")
                continue

            tone_name, tone_description = select_tone()

            print("\nGenerating your email...\n" + "=" * 40)
            email = generate_email(notes, tone_name, tone_description)
            print(email)
            print("=" * 40 + "\n")

            save_to_history(tone_name, notes, email)

            again = input("\nGenerate another email? (y/n): ").strip().lower()
            if again != "y":
                print("\nGoodbye! Emails saved in 'email_history.csv'.")
                break

        elif action == "2":
            view_history()

        elif action == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()