ALLOWED_COMMANDS = {
    "HEAD_LEFT",
    "HEAD_RIGHT",
    "HEAD_CENTER",
    "WAVE"
}


def validate_robot_command(command):
    if command not in ALLOWED_COMMANDS:
        return False

    return True