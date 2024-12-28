class Solution:
    def strongPasswordCheckerII(self, password):
        # Check for minimum length requirement
        has_length = len(password) >= 8  # Password must be at least 8 characters long

        # Validate other password conditions
        has_lower = any(c.islower() for c in password)  # At least one lowercase letter
        has_upper = any(c.isupper() for c in password)  # At least one uppercase letter
        has_digit = any(c.isdigit() for c in password)  # At least one digit
        has_special = any(c in "!@#$%^&*()-+" for c in password)  # At least one special character

        # Check for no adjacent repeating characters
        no_adjacent_repeats = all(password[i] != password[i + 1] for i in range(len(password) - 1))

        # Return True only if all conditions are met
        return has_length and has_lower and has_upper and has_digit and has_special and no_adjacent_repeats
