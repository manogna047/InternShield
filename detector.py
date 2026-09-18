from urllib.parse import urlparse


def analyze_internship(text, website_url=""):
    text = text.lower().strip()
    website_url = website_url.strip()

    indicators = {
        "registration fee": ("Payment request", 25),
        "application fee": ("Application fee requested", 25),
        "training fee": ("Training fee requested", 25),
        "security deposit": ("Security deposit requested", 25),
        "pay money": ("Payment request", 25),

        "guaranteed job": ("Guaranteed job claim", 20),
        "guaranteed placement": ("Guaranteed placement claim", 20),
        "easy money": ("Unrealistic earning claim", 15),

        "limited seats": ("Pressure/urgency language", 10),
        "apply urgently": ("Pressure/urgency language", 10),
        "urgent": ("Urgent language", 10),

        "telegram": ("Telegram communication", 10),
    }

    reasons = []
    score = 0

    # -------------------------
    # TEXT ANALYSIS
    # -------------------------

    for keyword, (reason, points) in indicators.items():

        if keyword in text:

            if reason not in reasons:
                reasons.append(reason)

            score += points


    # -------------------------
    # URL ANALYSIS
    # -------------------------

    url_info = "No website URL provided."

    if website_url:

        url_to_check = website_url.lower()

        if not url_to_check.startswith(("http://", "https://")):
            url_to_check = "https://" + url_to_check

        try:

            parsed = urlparse(url_to_check)
            domain = parsed.netloc.lower()

            if not domain:

                reasons.append("Website URL could not be parsed")
                score += 10
                url_info = "Invalid URL structure."

            else:

                # Google Forms
                if "forms.gle" in domain or "docs.google.com/forms" in domain:

                    url_info = "External Google Form detected."

                    if "Application uses an external Google Form" not in reasons:
                        reasons.append(
                            "Application uses an external Google Form"
                        )

                else:

                    url_info = "Website URL detected."

                # Suspicious URL patterns
                suspicious_url_words = [
                    "internship-free",
                    "job-offer",
                    "joboffer",
                    "registration",
                    "verify-account",
                    "claim-prize"
                ]

                for word in suspicious_url_words:

                    if word in domain:

                        reasons.append(
                            "URL contains a potentially suspicious pattern"
                        )

                        score += 15
                        break

                # Unusual @ symbol
                if "@" in url_to_check:

                    reasons.append(
                        "URL contains an unusual @ symbol"
                    )

                    score += 15

        except ValueError:

            reasons.append("Invalid website URL")
            score += 10
            url_info = "Invalid website URL."


    # -------------------------
    # SCORE
    # -------------------------

    score = min(score, 100)


    # -------------------------
    # RISK LEVEL
    # -------------------------

    if score >= 60:

        risk = "HIGH"
        icon = "🔴"

    elif score >= 30:

        risk = "MEDIUM"
        icon = "🟠"

    else:

        risk = "LOW"
        icon = "🟢"


    # -------------------------
    # MESSAGE
    # -------------------------

    if score >= 60:

        message = (
            "Several warning indicators were detected. "
            "Verify the organization carefully before proceeding."
        )

    elif score >= 30:

        message = (
            "Some warning indicators were detected. "
            "Review the internship details carefully."
        )

    else:

        message = (
            "No major warning indicators were detected. "
            "Independent verification is still recommended."
        )


    # -------------------------
    # CHECKLIST
    # -------------------------

    checklist = [
        "Verify the organization through its official website.",
        "Verify the recruiter's identity and contact details.",
        "Check whether the internship requires payment.",
        "Avoid sharing sensitive personal information unnecessarily.",
        "Look for independent information about the organization."
    ]


    return {
        "score": score,
        "risk": risk,
        "icon": icon,
        "reasons": reasons,
        "message": message,
        "url_info": url_info,
        "checklist": checklist
    }