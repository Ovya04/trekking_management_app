from flask import current_app
from flask_mail import Message
from extensions import mail


def email_enabled():
    return bool(current_app.config.get('EMAIL_ENABLED', False))


def send_email(subject, recipients, html):
    """Single choke point for all outgoing email. Returns True only if sent."""
    if not email_enabled():
        print(f"[EMAIL DISABLED] Skipped: '{subject}' -> {len(recipients)} recipient(s)")
        return False
    msg = Message(subject=subject, recipients=recipients, html=html)
    mail.send(msg)
    return True
