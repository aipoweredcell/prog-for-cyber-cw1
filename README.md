# prog-for-cyber-cw1
Name: Haseeb Rasool
Campus: New college lanarkshire
banner id: B01887873

# program overview

i made task 5 as a python program split as into 2 files a main.py and a cyber_security_utilities.py to validate passwords and ip addresses. validate_password(): loops through the password string to check for lowercase, uppercase, digits and punctuation to make sure it hits the 8 character minimum and has proper variety. validate ip splits the ip string by dots into 4 parts and checks that they are all numbers and are between numbers 0 - 255, and blocks invalid leading zeros. generate strong password uses a random.randint10,16 for length and garuntees at least one of each required character type is included and shuffles with random.shuffle so its secure.
main.py imports the cyber_security_utilities module and sks the yser for password and ip address and runs the validation functions top print out clear pass or fails. it calls generate strong password to suggest a secure strong password for the user if their password is weak. uses if __name__ == "__main__":

# how to run
go into terminal in the correct branch and type in the terminal: py main.py

# image
![alt text](image.png)
