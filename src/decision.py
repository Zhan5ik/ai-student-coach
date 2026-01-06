def decision_logic(shap_row, features, prob):
    actions = []
    priority = "LOW"

    if prob >= 0.85:
        priority = "CRITICAL"
    elif prob >= 0.7:
        priority = "HIGH"
    elif prob >= 0.55:
        priority = "MEDIUM"

    for value, feature in zip(shap_row, features):
        if value <= 0:
            continue

        if feature == "failures":
            actions.append("Academic counseling")

        elif feature == "studytime":
            actions.append("Structured study plan")

        elif feature == "absences":
            actions.append("Attendance monitoring")

        elif feature == "goout":
            actions.append("Lifestyle balance coaching")

    if priority == "CRITICAL":
        actions.append("URGENT academic intervention")

    return {
        "priority": priority,
        "actions": list(set(actions))
    }
