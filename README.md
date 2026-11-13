# prog-for-cyber-cw1

Name : Haseeb Rasool 
Campus : New College Lanarkshire
banner ID : B01887873 

## Program overview
for task 2 i made a security event logger in python that continously asks the user to enter a username and password until they get it right. for every single try the program generates an event log even if the attempt failed and prints out a detailed event log showing a random 4 digit event ID, the entered username, event status and whether it failed/suceeded for the login, and the exact timestamp 

## Code features
i used built in python modules like:
random - i used the 'random.randint(1000, 9999) to automatically generate a 4 digit event ID for every try.
datetime - i used the 'datetime.now()strftime("%Y-%m-%d %H:%M:%S) formatting function to capture the current date and time into a readable string.
socket - i used the socket library to create a connection function that looks up the local system's ip address. i put this inside a try-except block so that if there is any network error it wouldnt crash the program and will just fall back to 127.0.0.1 .
i used a while loop to keep the login prompt to keep running continously until the correct credentials are inputted, using if/else statements to check everything and break out of the loop on success. 

## how to run

open the terminal in the repository folder and make sure you are in the security-event-logger branch. run the script using: py security_event_logger.py

## Output image

![alt text](image.png)