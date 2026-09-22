from intent.intent_router import detect_intent
from tool_router import execute_tool
from voice.speech_to_text import listen


def main():
    print("================================")
    print("       MiniTARS AI Engine")
    print("================================")
    print("System status: ONLINE")
    print("Press ENTER to speak.")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("Press ENTER to speak: ")

        if user_input.lower().strip() == "exit":
            print("MiniTARS: Goodbye!")
            break

        spoken_text = listen()

        if spoken_text is None:
            print("MiniTARS: I couldn't understand that.\n")
            continue

        print("You said:", spoken_text)

        intent = detect_intent(spoken_text)

        print("Detected intent:", intent)

        if intent == "EXIT":
            print("MiniTARS: Goodbye!")
            break

        elif intent == "GREETING":
            print("MiniTARS: Hello! How can I help you?")

        else:
            response = execute_tool(intent, spoken_text)

            if response:
                print("MiniTARS:", response)

            else:
                print("MiniTARS: I can process that as a general question.")

        print()


if __name__ == "__main__":
    main()