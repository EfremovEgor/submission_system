import secrets


def generate_base64_url_safe_string():
    return secrets.token_urlsafe(64)
