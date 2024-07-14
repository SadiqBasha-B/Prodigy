import re
def check_password_complexity(password):
   
    criteria = [
        {"regex": r".{8,}", "message": "Password must be at least 8 characters long."},
        {"regex": r"[A-Z]", "message": "Password must contain at least one uppercase letter."},
        {"regex": r"[a-z]", "message": "Password must contain at least one lowercase letter."},
        {"regex": r"[0-9]", "message": "Password must contain at least one digit."},
        {"regex": r"[@$!%*?&]", "message": "Password must contain at least one special character (@, $, !, %, *, ?, &)."}
    ]
    
    feedback = []
    for criterion in criteria:
        if not re.search(criterion["regex"], password):
            feedback.append(criterion["message"])

    if len(feedback) == 0:
        return "Strong password!"
    elif len(feedback) <= 2:
        return "Moderate password. Suggestions to improve:\n" + "\n".join(feedback)
    else:
        return "Weak password. Suggestions to improve:\n" + "\n".join(feedback)


