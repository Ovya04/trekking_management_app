    # ---- Email feature flag (OFF unless explicitly set to "true") ----
    EMAIL_ENABLED = os.environ.get('EMAIL_ENABLED', 'false').strip().lower() == 'true'
    MAIL_SUPPRESS_SEND = not EMAIL_ENABLED   # Flask-Mail: never opens an SMTP connection

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Credentials are only loaded when email is enabled; no placeholder defaults
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') if EMAIL_ENABLED else None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') if EMAIL_ENABLED else None
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
