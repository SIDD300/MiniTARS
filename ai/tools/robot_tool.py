def execute_robot_command(command):

    if command == "HEAD_LEFT":
        return "Command detected: HEAD_LEFT."

    elif command == "HEAD_RIGHT":
        return "Command detected: HEAD_RIGHT."

    elif command == "HEAD_CENTER":
        return "Command detected: HEAD_CENTER."

    elif command == "WAVE":
        return "Command detected: WAVE."

    return "Unknown robot command."