#Email Slicer

""""
accept email, separate username from domain name

"""

def email_slicer(email):
    if "@" in email and "." in email.split("@")[1]:
        username, domain_name = email.split("@")
        return username, domain_name
    else:
        return None, None

try:    
    email = input("Please enter your email address: ").strip()
    username, domain_name = email_slicer(email)

    if username and domain_name:
        print(f"Your user name is: {username}, \nyour domain name is: {domain_name}")

        if "org" or "edu" or "ng" in domain_name:
            print(f"{email} is a corporate email.")
        else:
            print(f"{email} is a personal email.")

    else:
        print("Invalid email format, please try again.")

except Exception:
    print("Invalid email.")


