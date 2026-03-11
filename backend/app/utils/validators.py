import re

def validate_vin(vin: str) -> tuple[bool, str]:
    """Validate VIN format."""
    if not vin:
        return False, "VIN is required"
    
    vin = vin.upper().strip()
    
    if len(vin) != 17:
        return False, f"VIN must be 17 characters, got {len(vin)}"
    
    invalid_chars = ['I', 'O', 'Q']
    for char in invalid_chars:
        if char in vin:
            return False, f"VIN contains invalid character: {char}"
    
    return True, ""

def validate_zip(zip_code: str) -> tuple[bool, str]:
    """Validate US ZIP code."""
    if not zip_code:
        return False, "ZIP code is required"
    
    pattern = r'^\d{5}(-\d{4})?$'
    if not re.match(pattern, zip_code):
        return False, "Invalid ZIP code format"
    
    return True, ""