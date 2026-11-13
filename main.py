import cyber_security_utilities

def main():
    print(" === Cyber security utility toools ---")

    user_password=input("Please enter a password to validate: ")
    user_ip = input("Enter an Ip address to validate: ")

    print("\n--- Validation results")

    is_password_valid=cyber_security_utilities.validate_password(user_password)
    if is_password_valid:
        print(f"Password '{user_password}': VALID (Strong)")
    else:
        print(f"Password '{user_password}': INVALID (weak or too short)")
        suggested_password=cyber_security_utilities.generate_strong_password()
        print(f"P-> Suggested strong password: {suggested_password}")

    is_ip_valid=cyber_security_utilities.validate_ip(user_ip)
    if is_ip_valid:
        print(f"IP address '{user_ip}': VALID format")
    else:
        print(f"IP address '{user_ip}': INVALID format")



if __name__=="__main__":
    main()
