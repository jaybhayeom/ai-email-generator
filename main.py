import google.generativeai as genai
import os

# 1. Setup and Configuration
# Replace 'YOUR_API_KEY' with your actual Gemini API Key from Google AI Studio
os.environ["GOOGLE_API_KEY"] = "AIzaSyB5Q8KhEUc7NqFqLsRDeUUA71UY519PwT4"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate_professional_email(user_input):
    """
    Takes raw user input and generates a structured, error-free email.
    """
    
    # Define the behavior of the AI
    system_instruction = (
        "You are an expert executive assistant. Your task is to write a professional, "
        "grammatically perfect email based on the user's notes. "
        "Strict Rules: "
        "1. Do not hallucinate facts. Only use information provided. "
        "2. If information is missing (like a name), use [Bracketed Placeholders]. "
        "3. Ensure the tone is appropriate for the context provided."
    )

    # Initialize the model
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction
    )

    prompt = f"Convert these notes into a high-quality email:\n\nNotes: {user_input}"

    try:
        response = model.generate_content(prompt)
        
        if response.text:
            return response.text
        else:
            return "Error: The AI was unable to generate a response."
            
    except Exception as e:
        return f"An error occurred: {str(e)}"

# 2. Execution Flow
if __name__ == "__main__":
    print("--- AI Email Generator ---")
    print("Enter the details for your email (e.g., 'Email to Sarah, asking for a meeting Friday at 2pm about the budget')")
    
    raw_info = input("\nYour Notes: ")
    
    if not raw_info.strip():
        print("Error: No information provided. Please enter some details.")
    else:
        print("\nGenerating your email...\n" + "="*30)
        email_result = generate_professional_email(raw_info)
        print(email_result)
        print("="*30)