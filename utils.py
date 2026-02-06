import bleach

def sanitize_input(text):
    """Sanitize input to prevent XSS attacks."""
    allowed_tags = ['b', 'i', 'u', 'strong', 'em']  # Allow basic formatting if needed
    return bleach.clean(text, tags=allowed_tags, attributes={}, strip=True)