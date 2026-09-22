from intent.intent_router import detect_intent
from tools.robot_tool import execute_robot_command
from tools.college_tool import get_college_information
from tools.weather_tool import get_weather


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

        elif intent == "COLLEGE_INFO":
            response = get_college_information(user_input)
            print("MiniTARS:", response)

        elif intent == "WEATHER":
            response = get_weather()
            print("MiniTARS:", response)

        elif intent in [
            "HEAD_LEFT",
            "HEAD_RIGHT",
            "HEAD_CENTER",
            "WAVE"
        ]:
            response = execute_robot_command(intent)
            print("MiniTARS:", response)

        elif intent == "TAKE_PHOTO":
            print("MiniTARS: Camera command detected.")

        elif intent == "RECORD_VIDEO":
            print("MiniTARS: Video recording command detected.")

        else:
            print("MiniTARS: I can process that as a general question.")


if __name__ == "__main__":
    main()