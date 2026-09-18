def analyze_internship(text):
    text = text.lower()

    warning_words = {
        "registration fee": "Registration fee requested",
        "training fee": "Training fee requested",
        "security deposit": "Security deposit requested",
        "pay money": "Payment request detected",
        "guaranteed job": "Guaranteed job claim detected",
        "guaranteed placement": "Guaranteed placement claim detected",
        "work from home": "Work-from-home claim detected",
        "urgent": "Urgent/pressure language detected",
        "limited seats": "Pressure language detected",
        "easy money": "Unrealistic earning claim detected"
    }

    reasons = []
    score = 0

    for word, reason in warning_words.items():
        if word in text:
            reasons.append(reason)
            score += 10

    if score >= 40:
        risk = "HIGH"
    elif score >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "score": min(score, 100),
        "risk": risk,
        "reasons": reasons
    }