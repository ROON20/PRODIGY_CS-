import re

def assess_password_strength(password):
    """Assess the strength of the given password and provide feedback."""
    
    min_length = 8
    max_length = 20
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    
    length = len(password)
    length_criteria = min_length <= length <= max_length

    
    if length_criteria and has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Strong: Your password meets all the criteria."
    elif length_criteria and (has_uppercase or has_lowercase) and (has_digit or has_special_char):
        return "Moderate: Your password could be improved by adding more criteria."
    elif length_criteria or (has_uppercase or has_lowercase) or (has_digit or has_special_char):
        return "Weak: Your password does not meet enough criteria. Consider making it longer and adding more diverse characters."
    else:
        return "Very Weak: Your password is too short and lacks complexity. Make sure it's at least 8 characters long and includes a mix of uppercase letters, lowercase letters, digits, and special characters."

def main():
    password = input("Enter the password to assess: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == '__main__':
    main()
