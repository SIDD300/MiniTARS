COLLEGE_DATA = {
    "cse": {
        "name": "Computer Science and Engineering",
        "location": "second floor"
    },
    "hod": {
        "name": "Head of Department",
        "location": "CSE department office"
    }
}


def get_college_information(user_input):
    user_input = user_input.lower().strip()

    if "cse" in user_input or "computer science" in user_input:
        data = COLLEGE_DATA["cse"]
        return f"The {data['name']} department is on the {data['location']}."

    if "hod" in user_input:
        data = COLLEGE_DATA["hod"]
        return f"The {data['name']} office is at the {data['location']}."

    return "I don't have that college information yet."