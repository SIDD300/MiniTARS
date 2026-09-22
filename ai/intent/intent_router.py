def detect_intent(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "GREETING"

    if any(word in user_input for word in [
        "where is",
        "location",
        "department",
        "faculty",
        "hod",
        "office"
    ]):
        return "COLLEGE_INFO"

    if "weather" in user_input:
        return "WEATHER"

    if "photo" in user_input or "picture" in user_input:
        return "TAKE_PHOTO"

    if "record" in user_input or "video" in user_input:
        return "RECORD_VIDEO"

    if "turn left" in user_input:
        return "HEAD_LEFT"

    if "turn right" in user_input:
        return "HEAD_RIGHT"

    if "center" in user_input:
        return "HEAD_CENTER"

    if "wave" in user_input:
        return "WAVE"

    if user_input in ["exit", "quit", "bye"]:
        return "EXIT"

    return "GENERAL_CHAT"