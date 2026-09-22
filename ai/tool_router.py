from tools.college_tool import get_college_information
from tools.weather_tool import get_weather
from tools.robot_tool import execute_robot_command


def execute_tool(intent, user_input):

    if intent == "COLLEGE_INFO":
        return get_college_information(user_input)

    elif intent == "WEATHER":
        return get_weather()

    elif intent in [
        "HEAD_LEFT",
        "HEAD_RIGHT",
        "HEAD_CENTER",
        "WAVE"
    ]:
        return execute_robot_command(intent)

    elif intent == "TAKE_PHOTO":
        return "Camera command detected."

    elif intent == "RECORD_VIDEO":
        return "Video recording command detected."

    return None