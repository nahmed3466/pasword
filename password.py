import streamlit as st

class PasswordValidator:
    """
    A class to validate passwords based on specific criteria:
    1. At least 8 characters long.
    2. Contains at least one uppercase letter.
    3. Contains at least one lowercase letter.
    4. Contains at least one digit.
    """

    def __init__(self, password):
        self.password = password
        self.errors = []

    def validate(self):
        """Validates the password and populates the errors list."""
        self.errors.clear()  # Clear errors before validation

        # Check password length
        if len(self.password) < 8:
            self.errors.append("Password must be at least 8 characters long.")

        # Check for character types
        if not any(char.isupper() for char in self.password):
            self.errors.append("Password must have at least one uppercase letter.")
        if not any(char.islower() for char in self.password):
            self.errors.append("Password must have at least one lowercase letter.")
        if not any(char.isdigit() for char in self.password):
            self.errors.append("Password must have at least one digit.")

        return not self.errors

    def get_errors(self):
        """Returns a list of validation error messages."""
        return self.errors

# Streamlit app
st.title("Password Validator")

# Input for the password
password = st.text_input("Enter your password:", type="password")

if password:
    # Create a validator instance
    validator = PasswordValidator(password)

    # Validate the password
    if validator.validate():
        st.success("Password is valid.")
    else:
        st.error("Password validation failed:")
        for error in validator.get_errors():
            st.write(f"- {error}")
