from tools.college_tool import get_college_information
from tools.weather_tool import get_weather
from tools.robot_tool import execute_robot_command
from tools.camera_tool import take_photo, record_video
from safety.robot_safety import validate_robot_command


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
        if validate_robot_command(intent):
            return execute_robot_command(intent)

        return "Robot command rejected for safety."

    elif intent == "TAKE_PHOTO":
        return take_photo()

    elif intent == "RECORD_VIDEO":
        return record_video(40)

    return None