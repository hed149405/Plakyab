"""Custom Validators"""

import re
from typing import Optional

from app.utils.constants import VIN_LENGTH, VIN_PATTERN, VIN_WEIGHTS, VIN_TRANSLITERATION


class VINValidator:
    """VIN (Vehicle Identification Number) Validator"""

    @staticmethod
    def validate_format(vin: str) -> bool:
        """Validate VIN format (17 alphanumeric characters, no I, O, Q)"""
        if not vin or len(vin) != VIN_LENGTH:
            return False
        return bool(re.match(VIN_PATTERN, vin.upper()))

    @staticmethod
    def validate_checksum(vin: str) -> bool:
        """Validate VIN checksum according to ISO 3779"""
        vin = vin.upper()
        
        if not VINValidator.validate_format(vin):
            return False

        # Calculate checksum
        transliterated = ""
        for char in vin:
            if char.isdigit():
                transliterated += char
            else:
                transliterated += str(VIN_TRANSLITERATION.get(char, 0))

        # Calculate weighted sum
        weighted_sum = 0
        for i, digit in enumerate(transliterated):
            weighted_sum += int(digit) * VIN_WEIGHTS[i]

        # Check digit (position 9, 0-indexed)
        check_digit = weighted_sum % 11
        if check_digit == 10:
            check_digit = "X"
        else:
            check_digit = str(check_digit)

        return vin[8] == check_digit

    @staticmethod
    def validate(vin: str) -> bool:
        """Complete VIN validation (format + checksum)"""
        return VINValidator.validate_format(vin) and VINValidator.validate_checksum(vin)


class EmailValidator:
    """Email Validator"""

    EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    @staticmethod
    def validate(email: str) -> bool:
        """Validate email format"""
        if not email or len(email) > 255:
            return False
        return bool(re.match(EmailValidator.EMAIL_PATTERN, email))


class PlateValidator:
    """License Plate Validator"""

    @staticmethod
    def validate(plate: str) -> bool:
        """Validate license plate format (basic validation)"""
        if not plate or len(plate) < 3 or len(plate) > 20:
            return False
        return bool(re.match(r"^[A-Z0-9-]{3,20}$", plate.upper()))


class PasswordValidator:
    """Password Validator"""

    @staticmethod
    def validate(password: str) -> tuple[bool, Optional[str]]:
        """Validate password strength
        
        Requirements:
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
        """
        if not password:
            return False, "Password cannot be empty"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter"
        
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r"[0-9]", password):
            return False, "Password must contain at least one digit"
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character"
        
        return True, None
