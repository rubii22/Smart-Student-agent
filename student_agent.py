import os
from dotenv import load_dotenv
from colorama import init, Fore, Style
import google.generativeai as genai

# Initialize colorama
init(autoreset=True)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
chat = model.start_chat()

# --- Tool 1: Answer Academic Questions ---
def answer_question(question: str) -> str:
    try:
        response = chat.send_message(question)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# --- Tool 2: Study Tips ---
def study_tips() -> str:
    return f"""
{Fore.YELLOW}📚 Study Tips:
1. Set clear goals and break tasks into chunks.
2. Use Pomodoro technique: 25min study, 5min break.
3. Practice active recall and spaced repetition.
4. Avoid multitasking, stay focused.
5. Review your notes regularly.
"""

# --- Tool 3: Summarize Text ---
def summarize_text(text: str) -> str:
    prompt = f"Summarize this text briefly:\n{text}"
    try:
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# --- Main Interface ---
def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}\n🧠 Welcome to Smart Student Agent Assistant!\n")
    print(f"{Fore.MAGENTA}Choose an option:\n")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Answer an Academic Question")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Get Study Tips")
    print(f"{Fore.GREEN}3.{Style.RESET_ALL} Summarize Text")
    print(f"{Fore.GREEN}4.{Style.RESET_ALL} Exit")

    while True:
        choice = input(f"\n{Fore.CYAN}Enter your choice (1/2/3/4): {Style.RESET_ALL}")

        if choice == "1":
            question = input(f"{Fore.YELLOW}Enter your academic question: {Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}Answer:\n{Fore.WHITE}{answer_question(question)}")

        elif choice == "2":
            print(study_tips())

        elif choice == "3":
            text = input(f"{Fore.YELLOW}Paste the text to summarize: {Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}Summary:\n{Fore.WHITE}{summarize_text(text)}")

        elif choice == "4":
            print(f"{Fore.CYAN}Goodbye! 👋")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
