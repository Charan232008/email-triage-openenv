def grade(task_name, actions):
    correct = {
        "easy": {1: "spam", 2: "important"},
        "medium": {1: "important", 2: "spam", 3: "important"},
        "hard": {
            1: "important",
            2: "spam",
            3: "important",
            4: "ignore"
        }
    }

    total = len(correct[task_name])
    score = 0

    for action in actions:
        if correct[task_name].get(action.email_id) == action.label:
            score += 1

    return score / total