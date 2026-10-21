import re

def check_email_content(text: str) -> dict:
    issues, suggestions = [], []

    # Suspicious keywords
    keywords = ["urgent", "verify", "lottery", "winner", "account suspended"]
    for word in keywords:
        if word.lower() in text.lower():
            issues.append(f"Contains suspicious keyword: {word}")

    # Suspicious URLs
    urls = re.findall(r"http[s]?://\S+", text)
    for url in urls:
        if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url):
            issues.append(f"Suspicious IP-based URL: {url}")
        if "bit.ly" in url or "tinyurl" in url:
            issues.append(f"Shortened URL: {url}")
        if "@" in url:
            issues.append(f"Obfuscated URL: {url}")

    if issues:
        suggestions.append("Do not click suspicious links")
        suggestions.append("Verify sender identity")
    else:
        suggestions.append("Content looks safe")

    return {
        "text": text,
        "issues": issues,
        "suggestions": suggestions
    }

if __name__ == "__main__":
    samples = [
        "Urgent! Verify your account at http://192.168.0.1/login",
        "Congratulations, you are a lottery winner! Click http://bit.ly/abc123",
        "Hello Naina, meeting at 5 PM"
    ]
    for s in samples:
        result = check_email_content(s)
        print(f"\nText: {s}")
        print(f"Issues: {result['issues']}")
        print(f"Suggestions: {result['suggestions']}")
