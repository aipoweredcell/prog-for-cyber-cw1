# prog-for-cyber-cw1
Name: Haseeb Rasool
Campus: New College Lanarkshire
banner ID: B01887873



# program overview
for task 1 i made a modular security tool in python that when you run it, it asks for startup login information to get past the gate. once you are in a menu shows us and shows 4 options : 
1 - event counter - will test password attempts 10 times and flags an alert if you get more than half wrong
2 - brute-force - gives you 3 attempts to guess the password before cutting you off
3 - login check - asks for both a username and password and if you fail 3 times it locks the account for 24 hours
4 - exit - exits the menu
# code logic & features used 
i used conditional statements (if/else), functions, variables and integer/string counters. loops (for/while). for loops i used for i in range(10): a "for" loop that runs a fixed number of times for the event counter. while loops that keeps running as long as the user hasnt hit the 3 attempt limit. while loop for the menu to keep giving the user the option to select an option until they click the exit option. i used inputs to get user inputs so that the program can get the input and check if it is the correct username and password. i used return to exit out of a function when a correct password or login is achieved. break exits out of a while loop. if __name_ _ == "__main_ _": tells the python that this file is meant to be run directly as a script which triggers your main(). function to kick everything off.
# how to run
open in your terminal in the repistory folder. make sure you are on the security tool branch. run the script using '''bash python security_tool.py