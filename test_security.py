import re

def test_check_password():
    # Valid password
    assert check_password("Valid123") is True
    # Too short
    assert check_password("Va1") is False
    # Missing uppercase
    assert check_password("valid123") is False
    # Missing lowercase
    assert check_password("VALID123") is False
    # Missing digit
    assert check_password("ValidPass") is False

def test_generate_uuid_v4():
    uuid_value = generate_uuid_v4()
    # Check format using regex (UUID v4 format)
    pattern = re.compile(
        r'^[a-f0-9]{8}-'
        r'[a-f0-9]{4}-'
        r'4[a-f0-9]{3}-'
        r'[89ab][a-f0-9]{3}-'
        r'[a-f0-9]{12}$'
    )
    assert pattern.match(uuid_value)
