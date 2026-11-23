
from app.mentor import get_mentor_response


def main():

    print("\n===================================")
    print("       AI INTERVIEW MENTOR")
    print("===================================")
    print("Ask me anything about interview preparation.")
    print("Type 'exit' or 'quit' to end the application.")
    print("-----------------------------------")
    
    chat_history = []  # Initialize chat history for each session

    while True:
        

        user_input = input("\nYou: ").strip()

        # Check whether the user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("\nAI Mentor: Thank you for using AI Interview Mentor. Goodbye!")
            break

        # Handle empty input
        if not user_input:
            print("\nAI Mentor: Please enter a question.")
            continue

        try:
            response = get_mentor_response(user_input, chat_history)

            print("\nAI Mentor:")
            print(response)

        except Exception as e:
            print(f"\nError: Something went wrong: {e}")


if __name__ == "__main__":
    main()
