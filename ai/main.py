def process_command(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! I am MiniTARS. How can I help you?"

    elif "who are you" in user_input:
        return "I am MiniTARS, a modular physical AI assistant."

    elif "where is cse" in user_input:
        return "The Computer Science department is on the second floor."

    elif "weather" in user_input:
        return "I can check the current weather for you."

    elif "turn left" in user_input:
        return "Command detected: HEAD_LEFT."

    elif "turn right" in user_input:
        return "Command detected: HEAD_RIGHT."

    elif "wave" in user_input:
        return "Command detected: WAVE."

    elif user_input in ["exit", "quit", "bye"]:
        return None

    else:
        return "I don't understand that command yet."


def main():
    print("================================")
    print("       MiniTARS AI Engine")
    print("================================")
    print("System status: ONLINE")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        response = process_command(user_input)

        if response is None:
            print("MiniTARS: Goodbye!")
            break

        print("MiniTARS:", response)


if __name__ == "__main__":
    main()