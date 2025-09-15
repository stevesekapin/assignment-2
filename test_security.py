# test_security.py
import uuid
import importlib
import security  # security.py in the same folder

# Ensure latest code if you edit security.py while testing
importlib.reload(security)

def test_check_password_valid():
    assert security.check_password("Valid123!") is True

def test_check_password_too_short():
    assert security.check_password("Ab1!") is False

def test_check_password_missing_upper():
    assert security.check_password("valid123!") is False

def test_check_password_missing_lower():
    assert security.check_password("VALID123!") is False

def test_check_password_missing_digit():
    assert security.check_password("Valid!!!") is False

def test_generate_uuid_v4_format_and_version():
    u = security.generate_uuid_v4()
    parsed = uuid.UUID(u)  # raises if not a valid UUID
    assert parsed.version == 4
    assert str(parsed) == u

def test_check_password_non_string():
    assert security.check_password(None) is False  # covers isinstance guard
