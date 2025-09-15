def check_password(password: str) -> bool:
    """
    Check if the given password meets security requirements.

    Summary:
        Verify whether `password` satisfies a set of basic security rules:
        - Minimum length 8
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        - Contains at least one special character (punctuation)

    Parameters:
        password (str): The password string to validate.

    Returns:
        bool: True if the password meets all the rules, False otherwise.
    """
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    import string
    if not any(c in string.punctuation for c in password):
        return False
    return True
