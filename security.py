# security.py
import re
import uuid

def check_password(pw: str) -> bool:
    if not isinstance(pw, str):
        return False
    if len(pw) < 8:
        return False
    if not re.search(r"[a-z]", pw):
        return False
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"\d", pw):
        return False
    return True

def generate_uuid_v4() -> str:
    return str(uuid.uuid4())
