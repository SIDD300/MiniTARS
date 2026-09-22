from intent.intent_router import detect_intent
from tool_router import execute_tool


def main():
    print("================================")
    print("       MiniTARS AI Engine")
    print("================================")
    print("System status: ONLINE")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("You: ")

        intent = detect_intent(user_input)

        print("Detected intent:", intent)

        if intent == "EXIT":
            print("MiniTARS: Goodbye!")
            break

        elif intent == "GREETING":
            print("MiniTARS: Hello! How can I help you?")

        else:
            response = execute_tool(intent, user_input)

            if response:
                print("MiniTARS:", response)

            else:
                print("MiniTARS: I can process that as a general question.")


if __name__ == "__main__":
    main()