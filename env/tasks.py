from env.models import Email

def get_tasks():
    return {
        "easy": [
            Email(id=1, subject="Free iPhone", body="Click now"),
            Email(id=2, subject="Meeting", body="Team meeting"),
        ],
        "medium": [
            Email(id=1, subject="Urgent bank update", body="Verify account"),
            Email(id=2, subject="Big Sale Offer", body="Discount"),
            Email(id=3, subject="Daily Standup", body="Meeting"),
        ],
        "hard": [
            Email(id=1, subject="Invoice attached", body="Review"),
            Email(id=2, subject="Lottery Winner", body="Claim prize"),
            Email(id=3, subject="Client escalation", body="Urgent issue"),
            Email(id=4, subject="Newsletter", body="Weekly update"),
        ]
    }