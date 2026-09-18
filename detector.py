def analyze_internship(text):
    text = text.lower()

    indicators = {
        "registration fee": ("Payment request", 25),
        "training fee": ("Training fee requested", 25),
        "security deposit": ("Security deposit requested", 25),
        "pay money": ("Payment request", 25),
        "guaranteed job": ("Guaranteed job claim", 20),
        "guaranteed placement": ("Guaranteed placement claim", 20),
        "easy money": ("Unrealistic earning claim", 15),
        "limited seats": ("Pressure/urgency language", 10),
        "apply urgently": ("Pressure/urgency language", 10),
        "urgent": ("Urgent language", 10),
        "whatsapp": ("WhatsApp-only communication", 10),
        "telegram": ("Telegram communication", 10),
    }

    reasons = []
    score = 0

    for keyword, (reason, points) in indicators.items():
        if keyword in text:
            reasons.append(reason)
            score += points

    score = min(score, 100)

    if score >= 60:
        risk = "HIGH"
        icon = "🔴"
    elif score >= 30:
        risk = "MEDIUM"
        icon = "🟠"
    else:
        risk = "LOW"
        icon = "🟢"

    if not reasons:
        message = "No major warning indicators were detected."
    else:
        message = "Review the warning indicators before applying."

    return {
        "score": score,
        "risk": risk,
        "icon": icon,
        "reasons": reasons,
        "message": message
    }